$(document).ready(function() {
    $('INPUT#btn_translate').click(function() {
        const languageCode = $('INPUT#language_code').val();
        const apiUrl = `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`;
        
        $.get(apiUrl, function(data) {
            $('DIV#hello').text(data.hello);
        });
    });
});
