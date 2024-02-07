$(document).ready(function() {
    $('DIV#toggle_header').click(function() {
        const header = $('header');
        if (header.hasClass('red')) {
            header.removeClass('red').addClass('green');
        } else if (header.hasClass('green')) {
            header.removeClass('green').addClass('red');
        } else {
            header.addClass('red');
        }
    });
});

