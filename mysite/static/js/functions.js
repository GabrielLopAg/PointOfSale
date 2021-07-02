
function message_error(obj) {
    var html = '';
    if (typeof (obj) === 'object') {
        html = '<ul style="text-align: left;">';
        $.each(obj, function (key, value) { // key = index
            html += '<li>' + key + ': ' + value + '</li>';
        });
        html += '</ul>';
    } else{
        html = '<p>' + obj + '</p>';
    }
    Swal.fire({ // alerta del error (sweetAlert)
        title: 'Error!',
        html: html,
        icon: 'error'
    });
}