
$(document).ready(function() {
    $('#contact').on('submit', function(e){
        e.preventDefault();
        $.ajax({
           type: "POST",
           url: "http://reinventartandil.com/contact.php",
           data: $(this).serialize(),
           success: function() {
            alert('Recibimos tu consulta, te la responderemos a la brevedad.'); 
            window.location.href = '/';
           },
           error: function() {
            alert('Intente nuevamente.'); 
            window.location.href = '/';   
            }
        });
    });
});
