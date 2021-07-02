$(function () {
    $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            },
            dataSrc: ""
        },
        columns: [
            { "data": "id"},
            { "data": "agua"},
            { "data": "renta"},            
            { "data": "luz"},
            { "data": "internet"},
            { "data": "fecha_pago"},
            { "data": "fecha_pago"},            
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/main/expenses/update/' + row.id + '/" type="button" class="btn btn-warning btn-xs"><i class="fas fa-edit"></i></a>';
                    buttons += '<a href="/main/expenses/delete/' + row.id + '/" type="button" class="btn btn-danger btn-xs"><i class="fas fa-trash"></i></a>'
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });
});