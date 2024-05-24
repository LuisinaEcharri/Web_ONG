<?php
// save_news.php

ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

$dbhost= "localhost";
$dbuser= "root";
$dbpass= "";
$dbname= "reinvent__reinventar";

// Crear la conexión
$conn = new mysqli($dbhost, $dbuser, $dbpass, $dbname);

// Verificar la conexión
if ($conn->connect_error) {
    die("Conexión fallida: " . $conn->connect_error);
}

// Obtener el contenido del cuerpo de la petición HTTP
$input = json_decode(file_get_contents('php://input'), true);

$id = $input['Id'];
$titulo = $input['Titulo'];
$epigrafe = $input['Epigrafe'];
$imagen = 'https://ibb.co/yRTy210';
$cuerpo = $input['Cuerpo'];


// Preparar y ejecutar la consulta
$sql = "INSERT INTO noticia (titulo, epigrafe, imagen, cuerpo) VALUES ( ?, ?, ?, ?)";
$stmt = $conn->prepare($sql);
$stmt->bind_param("ssss", $titulo, $epigrafe, $imagen, $cuerpo);

if ($stmt->execute()) {
    echo json_encode(["success" => true, "message" => "Noticia guardada correctamente"]);
} else {
    echo json_encode(["success" => false, "message" => "Error al guardar la noticia"]);
}

$stmt->close();
$conn->close();
?>