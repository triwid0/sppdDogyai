// const button = document.getElementById('triggerAlert');

// button.addEventListener('click', e =>{
//     e.preventDefault();

//     Swal.fire({
//         html: `A SweetAlert content with <strong>bold text</strong>, <a href="hapus/{{data.id_organisasi}}">links</a>
//              or any of our available <span class="badge badge-primary">components</span>`,
//         icon: "info",
//         buttonsStyling: false,
//         showCancelButton: true,
//         confirmButtonText: "Ok, got it!",
//         cancelButtonText: 'Nope, cancel it',
//         customClass: {
//             confirmButton: "btn btn-primary",
//             cancelButton: 'btn btn-danger'
//          }
//    });
// });

// $(document).ready(function () {
//     $(".delete-button").on("click", function (e) {
//         e.preventDefault(); // Mencegah tautan mengarahkan ke URL langsung

//         var getLink = $(this).attr('href', '1');
//                 Swal.fire({
//                     title: "Yakin hapus data?",            
//                     icon: 'warning',
//                     showCancelButton: true,
//                     confirmButtonColor: '#d33',
//                     confirmButtonText: 'Ya',
//                     cancelButtonColor: '#3085d6',
//                     cancelButtonText: "Batal"
//                 }).then(result => {
//                     //jika klik ya maka arahkan ke proses.php
//                     if(result.isConfirmed){
//                         location.assign(getLink);
//                     }
//                 })
                
            
//                 return false;
        
//     });
// });

$(document).ready(function () {
    const registerDeleteItemHandlers = () => {
      $(".delete-button").on("click", function (e) {
        e.preventDefault();
        var form = $(this).parents("form");
        alert('delete').then((result) => {
          if (result.value) {
            form.submit();
          }
        });
      });
    };
  
    registerDeleteItemHandlers();
  
    $(".datatabel")
      .dataTable()
      .on("draw.dt", function () {
        registerDeleteItemHandlers();
      });
  });
  function refreshTable() {
    $('.dataTable').each(function() {
        dt = $(this).dataTable();
        dt.fnDraw();
    })
  }

$(document).ready(function () {
    $(".off-button").on("click", function (e) {
        e.preventDefault(); // Mencegah tautan mengarahkan ke URL langsung

        var getLink = $(this).attr('href');
                Swal.fire({
                    title: "Yakin Non Aktifkan Tahun?",            
                    icon: 'warning',
                    showCancelButton: true,
                    confirmButtonColor: '#d33',
                    confirmButtonText: 'Ya',
                    cancelButtonColor: '#3085d6',
                    cancelButtonText: "Batal"
                
                }).then(result => {
                    //jika klik ya maka arahkan ke proses.php
                    if(result.isConfirmed){
                        location.assign(getLink);
                    }
                })
                return false;
        
    });
});
// $('#orderTable').dataTable({
//     // "sScrollY": "100px",

//     "autoWidth": false,
//     "deferRender": true,
//     //"bPaginate": false,

//     "drawCallback": function() {
//         $('.orderNumber').on('click', function () {
//             var orderNum = $(this).text();
//             console.log(orderNum);
//         });
//     }
// });



// $(document).on("click", ".delete-button", function() {
//     var item_id = $(this).data("id");
//     Swal.fire({
//         title: 'Apakah Anda yakin?',
//         text: "Item ini akan dihapus!",
//         icon: 'warning',
//         showCancelButton: true,
//         confirmButtonColor: '#d33',
//         cancelButtonColor: '#3085d6',
//         confirmButtonText: 'Ya, Hapus!',
//         cancelButtonText: 'Batal'
//     }).then((result) => {
//         if (result.isConfirmed) {
//             $.ajax({
//                 type: 'POST',
//                 url: `/delete/${item_id}/`, // Ganti dengan URL yang sesuai
//                 data: {
//                     csrfmiddlewaretoken: '{{ csrf_token }}'
//                 },
//                 success: function(data) {
//                     if (data.message === 'Item berhasil dihapus') {
//                         Swal.fire(
//                             'Terhapus!',
//                             'Item telah dihapus.',
//                             'success'
//                         );
//                         // Lakukan refresh DataTable setelah penghapusan
//                         $('#item-table').DataTable().ajax.reload();
//                     } else {
//                         Swal.fire(
//                             'Gagal!',
//                             'Gagal menghapus item.',
//                             'error'
//                         );
//                     }
//                 },
//                 error: function() {
//                     Swal.fire(
//                         'Gagal!',
//                         'Terjadi kesalahan saat menghapus item.',
//                         'error'
//                     );
//                 }
//             });
//         }
//     });
// });

