<?php
// get_inscriptos.php

header('Content-Type: application/json');

$dbhost= "localhost";
$dbuser= "root";
$dbpass= "";
$dbname= "reinvent_reinventar";
// $dbhost= "149.56.87.21:3306";
// $dbuser= "reinvent_admin";
// $dbpass= "xu@xDR_;9kpO";
// $dbname= "reinvent_reinventar";

// Crear la conexión
$conn = new mysqli($dbhost, $dbuser, $dbpass, $dbname);

// Verificar la conexión
if ($conn->connect_error) {
    die("Conexión fallida: " . $conn->connect_error);
}

// Consultar los datos de los inscriptos
$sql = "SELECT nombre, apellido, telefono, email, fecha_inscripcion, estado FROM inscripto";
$result = $conn->query($sql);

$inscriptos = array();

if ($result->num_rows > 0) {
    while($row = $result->fetch_assoc()) {
        $inscriptos[] = $row;
    }
}

$conn->close();

// Devolver los datos en formato JSON

echo json_encode($inscriptos);
?>