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
            { "data": "sku"},
            { "data": "nombre_prod"},
            { "data": "categoria"},
            //{ "data": "descripcion"},
            { "data": "cotizacion"},
            { "data": "precio_de_venta"},
            { "data": "costo_unitario"},
            { "data": "costo_paquete"},
            { "data": "costo_paquete"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/main/products/update/' + row.id + '/" type="button" class="btn btn-warning btn-xs"><i class="fas fa-edit"></i></a>';
                    buttons += '<a href="/main/products/delete/' + row.id + '/" type="button" class="btn btn-danger btn-xs"><i class="fas fa-trash"></i></a>'
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });
});