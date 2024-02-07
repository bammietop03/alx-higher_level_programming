$(document).ready(function() {
    $('INPUT#btn_translate, INPUT#language_code').on('click keypress', function(event) {
        if (event.type === 'click' || (event.type === 'keypress' && event.which === 13)) {
            const languageCode = $('INPUT#language_code').val();
            const apiUrl = `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`;

            $.get(apiUrl, function(data) {
                $('DIV#hello').text(data.hello);
            });
        }
    });
});
