<?php 

    $to = "Reinventar Tandil <info@reinventartandil.com>"; // TODO Own Email address Reinventar Tandil <info@reinventartandil.com>
    $name = $_POST['name'];
    $from = $_POST['email']; // Sender Email address
    $message = $_POST['message'];
    $subject = $name . " envio una consulta";
    $subject2 = "Enviaste una consulta";
    $headers = "From:" . $from;
    $headers2 = "From:" . $to;

    $message = $name . " envio el siguiente mensaje: " . "\n\n" . $message;
    $message2 = "Recibimos tu consulta, te la responderemos a la brevedad."; 

    $success = mail($to,$subject,$message,$headers);
        if ($success) {
            mail($from,$subject2,$message2,$headers2);
            echo "<script>
                window.location.href = 'http://www.reinventartandil.com';   
                sessionStorage.setItem('showmsg', '1');
            </script>";
        }
?>