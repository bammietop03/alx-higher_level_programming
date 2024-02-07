$(document).ready(function() {
    $('DIV#add_item').click(function() {
        $('<li>Item</li>').appendTo('.my_list');
    });

    $('DIV#remove_item').click(function() {
        $('.my_list li:last-child').remove();
    });

    $('DIV#clear_list').click(function() {
        $('.my_list').empty();
    });
});

