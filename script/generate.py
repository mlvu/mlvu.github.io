# inspiration https://gist.github.com/cyli/4644918

import fire
from mako.template import Template

import os, subprocess, sys, glob
from os import sep as S

import re
import random
import string, urllib.parse
import shutil

import subprocess
from subprocess import PIPE

from PyPDF2 import PdfFileReader, PdfFileWriter

from lxml import etree, html

# Plan:
# Slide images
# - Use applescript to export to PDF, one slide at a time, naming the file after the slide ID
# -- Split the PDF files into multiple pages (some cli tool? python?)
# - Use command line calls (svg2pdf) to convert to svg

# Animation
# -- Gather stages into a sequence of SVGs.

# Presenter notes with basic styling
# - Use applescript to export all keynote files to keynote 09 format (or do this manually if necessary)
# - Use the basic idea of the script below to extract presenter notes with styling.
# - Convert all basic apple tags to styling manually, or use xslt.

# Convert to website:
# - make a list with lectures and their html file names
# - Invent some code to insert video & section delimiters

def inner(node):
    return (node.text or '') + ''.join([html.tostring(child, encoding="unicode") for child in node.getchildren()])

def generate(
        dst="/Users/peter/Dropbox/gits/git-sakhmet/mlvu.github.io/lecture01",
        workdir="/Users/peter/Desktop/mlvu-export",
        source='/Users/peter/Desktop/test.key',
        title='Lecture 1: Introduction',
        base_url='mlvu.github.io/lecture01/',
        pdf_link='...'):
    """
    Takes a single keynote file, extracts SVGs of the slides (including all build stages) and a markdown version of the
    presenter notes preserving the main rich text as stylable HTML.

    :param dst: Where the final files end up.
    :param workdir: The directory on the desktop where the script dumps the PDFs and keynote 09 version (hardcoded in the applescript as mlvu export)
    :param source: The original keynote file.
    :return:
    """

    # clear the working directory
    if os.path.exists(workdir):
        shutil.rmtree(workdir)
    os.makedirs(workdir)

    # clear the destination direction
    if os.path.exists(dst):
        shutil.rmtree(dst)
    os.makedirs(dst)

    docId = os.path.basename(source)

    ## Call the applescript (Extract slide PDFs and Keynot 09 version of file)
    print('Extracting slide PDFs')
    process = subprocess.check_call(['osascript', 'kn.scpt', source])

    ## Split the multistage PDFs into multiple pages
    print('Splitting PDFs')
    for file in glob.glob(workdir + os.sep + '*stage*.pdf'):

        pdf = PdfFileReader(file)
        if pdf.getNumPages() > 1:
            for p in range(pdf.getNumPages()):
                pdfr = PdfFileWriter()
                pdfr.addPage(pdf.getPage(p))

                sp = file.rsplit('.',  1)
                newfile = f'{sp[0]}anim{p}.{sp[1]}'

                with open(newfile, 'wb') as outfile:
                    pdfr.write(outfile)
            os.remove(file)

    ## Loop through the pages of the main PDF and assign the name of the stage file
    pdf = PdfFileReader(workdir + S + docId + '.pdf')
    # assert pdf.getNumPages() == len(glob.glob(workdir + os.sep + '*stage*.pdf')), f'number of pages in main pdf {pdf.getNumPages()}, number of stage files {len(glob.glob(workdir + os.sep + "*stage*.pdf"))}'
    # should be true for the final run

    for p, file in enumerate(sorted(glob.glob(workdir + os.sep + '*stage*.pdf'))):
        print(p, file)

        os.remove(file)

        pdfr = PdfFileWriter()
        pdfr.addPage(pdf.getPage(p))

        with open(file, 'wb') as outfile:
            pdfr.write(outfile)

    # Convert to SVG, delete PDF
    print('Converting to SVGs')
    images = []
    for file in sorted(glob.glob(workdir + S + '*stage*.pdf')):
        sp = file.rsplit('.', 1)

        process = subprocess.check_call(['/usr/local/bin/pdf2svg', file, sp[0]+'.svg'])

        os.remove(file)

        # Convert any svg larger than 1mb to a png instead
        if os.path.getsize(sp[0]+'.svg') > 1_000_000:
            process = subprocess.check_call(['/usr/local/bin/inkscape',
                                             '--export-type=png',
                                             sp[0] + '.svg'])
            os.remove(sp[0] + '.svg')

            images.append(sp[0] + '.png')
        else:
            images.append(sp[0] + '.svg')

    images = [urllib.parse.quote_plus(os.path.basename(i)) for i in images]
    grouped, group = [], []
    lastpref = ''

    for image in images:

        thispref = re.search('(.+?)(anim|\\.svg|\\.png)', image).group(1)
        print('-- ', thispref)

        if thispref == lastpref:
            group.append(image)
        else:
            if len(group) > 0: grouped.append(group)
            group = [image]

        lastpref = thispref

    grouped.append(group)
    images = grouped

    tempdir = workdir + os.sep + 'k09'

    if not os.path.exists(tempdir):
        os.mkdir(tempdir)

    # keynote file is a giant compressed xml file - uncompress it
    print('Extracting presenter notes')
    try:
        subprocess.check_call(['unzip', '-o', workdir + S + docId + '.k09.key', '-d', tempdir])
    except subprocess.CalledProcessError as ex:
        print('Error in unzipping. Tyring to continue.')
        print(ex)

    xml = etree.parse(tempdir + '/index.apxl')
    root = xml.getroot()

    # Find the character styles that map to the styling elements we want to extract (bold, italic, particular colors)
    # -- very much best effort, but it should work for the basics

    bold = set()
    italic = set()
    sup = set()
    sub = set()

    orange = set()
    blue   = set()
    green  = set()
    red    = set()

    videos = []

    styles = root.xpath('.//sf:characterstyle', namespaces=root.nsmap)
    for note in styles:

        id = note.attrib['{http://developer.apple.com/namespaces/sfa}ID']
        strnote = str(etree.tostring(note))

        if '<sf:bold>' in strnote:
            bold.add(id)

        if '<sf:italic>' in strnote:
            italic.add(id)

        if 'sf:superscript' in strnote:
            if 'sf:number sfa:number="2" sfa:type="i"' in strnote:
                sub.add(id) # weird behavior
            else:
                sup.add(id)

        if 'sf:subscript' in strnote:
            sub.add(id)

        if 'sfa:r="0.041535880416631699" sfa:g="0.30631634593009949" sfa:b="0.70056915283203125"' in strnote:
            blue.add(id)
        if 'sfa:r="0.72908496856689453" sfa:g="0.069717332720756531" sfa:b="0.037668853998184204"' in strnote or \
            'sfa:r="0.83242297172546387" sfa:g="0.33357393741607666" sfa:b="0.061638608574867249"' in strnote:
            orange.add(id)
        if 'sfa:r="0.061777830123901367" sfa:g="0.47138708829879761" sfa:b="0.12690891325473785"' in strnote:
            green.add(id)
        if 'sfa:r="0.72908496856689453" sfa:g="0.069717332720756531" sfa:b="0.037668853998184204"' in strnote:
            red.add(id)

    # Check the paragraph styles for list items

    # -- Find all list styles that actually represent lists
    listyles = set()
    styles = root.xpath('.//sf:liststyle', namespaces=root.nsmap)
    for note in styles:

        id = note.attrib['{http://developer.apple.com/namespaces/sfa}ID']
        strnote = str(etree.tostring(note))

        if ('sf:labelCharacterStyle1' in strnote) or ('sf:type="bullet"' in strnote):
            listyles.add(id)

    # -- Find all paragraphstyles that reference these list styles
    li = set()

    styles = root.xpath('.//sf:paragraphstyle', namespaces=root.nsmap)
    for note in styles:

        id = note.attrib['{http://developer.apple.com/namespaces/sfa}ID']
        strnote = str(etree.tostring(note, encoding='unicode'))

        for listyle in listyles:
            if f'"{listyle}"' in strnote:
                li.add(id)

    # get all the presenter note xml elements
    slides = root.xpath('.//key:slide', namespaces=root.nsmap)

    # replace all the funky keynote tags with html tags
    sf_namespace = '{{{0}}}'.format(root.nsmap['sf'])

    def replace_node(node):

        classes = []
        attribs = {}

        if node.tag.startswith(sf_namespace):

            node.tag = node.tag.replace(sf_namespace, '')

            # check for color
            if '{http://developer.apple.com/namespaces/sf}style' in node.attrib:
                if node.attrib['{http://developer.apple.com/namespaces/sf}style'] in blue:
                    classes.append('blue')
                if node.attrib['{http://developer.apple.com/namespaces/sf}style'] in orange:
                    classes.append('orange')
                if node.attrib['{http://developer.apple.com/namespaces/sf}style'] in green:
                    classes.append('green')
                if node.attrib['{http://developer.apple.com/namespaces/sf}style'] in red:
                    classes.append('red')

            # replace node tag with html equivalent
            if node.tag == 'link':
                node.tag = 'a'
                attribs['href'] = node.attrib['href']
            elif node.tag == 'text-body':
                node.tag = 'div'
            elif node.tag == 'span':
                if node.attrib['{http://developer.apple.com/namespaces/sf}style'] in bold:
                    node.tag = 'strong'
                if node.attrib['{http://developer.apple.com/namespaces/sf}style'] in italic:
                    node.tag = 'em'
                if node.attrib['{http://developer.apple.com/namespaces/sf}style'] in sup:
                    node.tag = 'sup'
                if node.attrib['{http://developer.apple.com/namespaces/sf}style'] in sub:
                    node.tag = 'sub'

            elif node.tag == 'p':
                if node.attrib['{http://developer.apple.com/namespaces/sf}style'] in li:
                    classes.append('list-item')
                else:
                    pass
            else:
                #pass
                node.tag = etree.QName(node).localname

        for child in node.getchildren():
            replace_node(child)

        node.attrib.clear()
        node.nsmap.clear() # -- this does fuck all

        if len(classes) > 0:
            node.attrib['class'] = ' '.join(classes)

        for k, v in attribs.items():
            node.attrib[k] = v

    hkey = '{http://developer.apple.com/namespaces/keynote2}hidden'
    id = 0

    annotations = []
    menu = []

    for slide in slides:

        if hkey not in slide.attrib or slide.attrib[hkey] != 'true':
            id += 1 # this should match the id

            notes = slide.xpath('.//key:notes/sf:text-storage', namespaces=root.nsmap)

            if len(notes) > 0:
                pnote = notes[0]

                replace_node(pnote)
                etree.cleanup_namespaces(pnote)

                pnote.attrib['id'] = f'slide-{0}'

                for div in pnote.xpath('.//div', namespaces=root.nsmap):

                    anno = inner(div)

                    # some minor cleaning up
                    anno = anno.replace('\n',  '')

                    # hack to get rid of namespace crap
                    anno = re.sub('xmlns:[^\\s]*="[^\\s]*"', '', anno)

                    # check for youtube video link
                    vmatch1 = re.search('\\|video\\|([^\\|^\\s]*)\\|', anno)
                    # -- video should replace slide
                    vmatch2 = re.search('\\|video-slide\\|([^\\|^\\s]*)\\|', anno)

                    if vmatch1 is not None:
                        videos.append(vmatch1.group(1))
                        anno = re.sub('\\|video\\|([^\\|^\\s]*)\\|', '', anno)

                    elif vmatch2 is not None:
                        videos.append('inline:' + vmatch2.group(1))
                        anno = re.sub('\\|video-slide\\|([^\\|^\\s]*)\\|', '', anno)

                    else:
                        videos.append(None)

                    # check for section head
                    match = re.search('\\|section\\|([^\\|]*)\\|', anno)

                    if match is not None:
                        stitle = match.group(1)
                        menu.append((id, stitle))

                        anno = re.sub('\\|section\\|([^\\|]*)\\|', '', anno)

                    annotations.append(anno)

    print('Rendering HTML')
    lecture_tpl = Template(filename='lecture.tpl')

    content = [{'annotation': a, 'image': i, 'video': v} for a, i, v in zip(annotations, images, videos)]
    rendered = lecture_tpl.render(title=title, content=content, menu=menu, base_url=base_url, pdf_link=pdf_link)

    with open(workdir + S + 'index.md', 'w') as file:
        file.write(rendered)

    # Copy to target dir

    files = []
    files += glob.glob(workdir + '/' + '*.md')
    files += glob.glob(workdir + '/' + '*.svg')
    files += glob.glob(workdir + '/' + '*.png')

    for file in files:
        shutil.copy(file, dst)


if __name__ == '__main__':
    fire.Fire(generate)