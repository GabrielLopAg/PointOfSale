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
            //{ "data": "id"},
            { "data": "nombre_comercial"},
            { "data": "nombre_representante"},
            { "data": "tel_movil"},
            { "data": "tel_fijo"},
            { "data": "correo"},
            { "data": "municipio"},
            { "data": "colonia"},
            { "data": "calle"},
            { "data": "pagina_web"},
            { "data": "pagina_web"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/main/providers/update/' + row.id + '/" type="button" class="btn btn-warning btn-xs"><i class="fas fa-edit"></i></a>';
                    buttons += '<a href="/main/providers/delete/' + row.id + '/" type="button" class="btn btn-danger btn-xs"><i class="fas fa-trash"></i></a>'
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });
});