(function () {
    'use strict'

    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    var forms = document.querySelectorAll('.needs-validation')

    // Loop over them and prevent submission
    Array.prototype.slice.call(forms)
      .forEach(function (form) {
        form.addEventListener('submit', function (event) {
          if (!form.checkValidity()) {
            event.preventDefault()
            event.stopPropagation()
            
          }

          form.classList.add('was-validated')
        }, false)
      })
  })()

  // match password 
  var check = function () {
    if (document.getElementById('password').value ==
      document.getElementById('confirm_password').value) {
      document.getElementById('message').style.color = 'green';
      document.getElementById('confirm_password').style.border = '2px solid green';
      document.getElementById('password').style.border = '2px solid green';
      document.querySelector('.needs-validation button').removeAttribute('disabled', '')
      

    } else {
      document.getElementById('message').style.color = 'red';
      document.getElementById('confirm_password').style.border = '2px solid red';
      document.getElementById('password').style.border = '2px solid red';
      document.querySelector('.needs-validation button').setAttribute('disabled', '')

    }
  }

