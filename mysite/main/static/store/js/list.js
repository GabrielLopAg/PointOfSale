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
            { "data": "municipio"},
            { "data": "colonia"},
            { "data": "calle"},
            { "data": "cantidad"},
            { "data": "cantidad"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/main/store/update/' + row.id + '/" type="button" class="btn btn-warning btn-xs"><i class="fas fa-edit"></i></a>';
                    buttons += '<a href="/main/store/delete/' + row.id + '/" type="button" class="btn btn-danger btn-xs"><i class="fas fa-trash"></i></a>'
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });
});