$(document).ready(function()
{

    // - animated slides
    $('.slides .anim img').click(function() {

        target = $(this)
        frames = target.data('images').split(',')

        current = target.attr('src');
        idx = frames.indexOf(current) + 1;

        if (idx >= frames.length)
            idx = 0;

        target.attr('src', frames[idx]);
    });

    $(window).on("scroll", function() {

        var currentPos = $(window).scrollTop();

        $('nav li a').each(function()
        {
            var sectionLink = $(this);
            // capture the height of the navbar
            var navHeight = $('#nav-wrapper').outerHeight() + 1;
            var section = $(sectionLink.attr('href'));

            // subtract the navbar height from the top of the section
            if(section.position().top - navHeight  <= currentPos && sectionLink.offset().top + section.height()> currentPos) {
              $('.nav li').removeClass('active');
              sectionLink.parent().addClass('active');
            } else {
              sectionLink.parent().removeClass('active');
            }
        });
    });

});
