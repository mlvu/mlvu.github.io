$(document).ready(function()
{
    // $('.slides nav.menu li a').eq(1).addClass('active');

    // - animated slides
    $('.slides .anim img').click(function() {

        target = $(this)
        frames = target.data('images').split(',')

        current = target.attr('src');
        idx = frames.indexOf(current) + 1;

        if (idx >= frames.length)
            idx = 0;

        target.attr('src', frames[idx]);

        if (idx == frames.length -1)
            target.parent().addClass('done');
        else
            target.parent().removeClass('done');
    });

});

$(window).on('load', function()
{

    // work out the positions of all targets in the menu
    let previous = null;
    let first = true;
    $('.slides nav.menu li a').each(function()
    {
        current = $(this)
        target = current.attr('href')

        if (target.startsWith('#'))
        {
            if (first)
            {
                first = false;
                current.data('from', 0);
            } else
            {
                let top = $(target).position().top;
                console.log(top);

                current.data('from', top);
                previous.data('to', top);
            }
            previous = current;
        }
    });

    previous.data('to', Number.POSITIVE_INFINITY);

    $(window).on("scroll", function()
    {

        let offset = $('header').height() + $('.slides nav.menu').height();
        let current = $(window).scrollTop() + offset;

        $('.slides nav.menu li a').each(function()
        {

            let a = $(this);
            console.log(a.attr('href'), a.data('from'), a.data('to'), current);

            let from = a.data('from');
            let to = a.data('to');

            // subtract the navbar height from the top of the section
            if(from < current && current < to)
            {
                a.parent().addClass('active');
            } else
            {
                a.parent().removeClass('active');
            }
        });
    });

    $(window).scroll();

});
