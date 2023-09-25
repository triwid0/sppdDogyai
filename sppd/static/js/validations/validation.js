
function validation() {
    var numberInput = document.getElementB("tahun");
    var errorMessage = document.getElementById("error-message");

    var inputValue = numberInput.value;

    // Validasi tidak boleh kosong
    if (inputValue.trim() === "") {
        errorMessage.innerHTML = "Masukkan tidak boleh kosong.";
        return false;
    }

    // Validasi hanya berisi angka
    var regex = /^[0-9]+$/;
    if (!regex.test(inputValue)) {
        errorMessage.innerHTML = "Masukkan hanya boleh berisi angka.";
        return false;
    }

    return true;
}













// $(document).ready(function () {
//     $('#formTahun').submit(function(event){
//         event.preventDefault();

//         $.validator.addMethod("valueNotEquals", function(value, element, arg){
//             return arg != value;
//         },"value must not equal arg.");

//         $("#formTahun").validate({
//             highlight : function(input){
//                 $(input).para
//             }
//         })

//     })
// });


// function validation(){
//     var validasiHuruf = /^[a-zA-Z ]+$/;
//     var nama = document.getElementById("nama");
//     if (nama.value.match(validasiHuruf)) {
//        alert("Nama Anda adalah " + nama.value);
//     } else {
//        alert("Masukkan nama Anda!\nFormat wajib huruf!");
//        nama.value="";
//        nama.focus();
//        return false;
//     }
//   }


