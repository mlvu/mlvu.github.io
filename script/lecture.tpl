---
title: "${title}"
slides: true
---
<nav class="menu">
    <ul>
        <li class="home"><a href="/">Home</a></li>
        <li class="name">${title}</li>
        % for (id, stitle) in menu:
            % if stitle.startswith('nv:'):
                <li><a href="#slide-${f'{id:03}'}">${stitle[3:]}</a></li>
            % else:
                <li><a href="#video-${f'{id-1:03}'}">${stitle}</a></li>
            % endif
        % endfor
        <li class="pdf"><a href="${pdf_link}">PDF</a></li>
    </ul>
</nav>

<article class="slides">
% for i, slide in enumerate(content):

    % if slide['video'] is not None and not slide['video'].startswith('inline:'):

       <section class="video" id="video-${f'{i:03}'}">
           <a class="slide-link" href="${base_url}#video-${i}">link here</a>
           <iframe
                src="${slide['video']}"
                title="YouTube video player"
                frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen>
           </iframe>

       </section>

    % endif

    % if slide['video'] is not None and slide['video'].startswith('inline:'):

       <section id="slide-${f'{i+1:03}'}">
            <a class="slide-link" href="${base_url}#slide-${f'{i+1:03}'}" title="Link to this slide.">link here</a>
            <iframe
                src="${slide['video'][7:]}"
                title="YouTube video player"
                frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen>
            </iframe>

            <figcaption>
            ${slide['annotation']}
            </figcaption>
       </section>

    % elif len(slide['image']) == 1:

       <section id="slide-${f'{i+1:03}'}">
            <a class="slide-link" href="${base_url}#slide-${f'{i+1:03}'}" title="Link to this slide.">link here</a>
            <img src="${slide['image'][0]}" class="slide-image" />

            <figcaption>
            ${slide['annotation']}
            </figcaption>
       </section>

    % else:

       <section id="slide-${f'{i+1:03}'}" class="anim">
            <a class="slide-link" href="${base_url}#slide-${f'{i+1:03}'}" title="Link to this slide.">link here</a>
            <img src="${slide['image'][0]}" data-images="${','.join(slide['image'])}" class="slide-image" />

            <figcaption>
            ${slide['annotation']}
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>

    % endif

% endfor
</article>
