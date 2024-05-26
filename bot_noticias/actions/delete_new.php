<?php
// Configuración de la conexión a la base de datos
$dbhost= "localhost";
$dbuser= "root";
$dbpass= "";
$dbname= "reinvent_reinventar";

// Crear la conexión
$conn = new mysqli($dbhost, $dbuser, $dbpass, $dbname);

// Verificar la conexión
if ($conn->connect_error) {
    die("Conexión fallida: " . $conn->connect_error);
}

// Obtener el título de la noticia desde la solicitud POST
$data = json_decode(file_get_contents('php://input'), true);
$titulo = $data['Titulo'];

$response = array();

// Preparar y ejecutar la consulta para eliminar la noticia
$sql = "DELETE FROM noticia WHERE titulo = ?";
$stmt = $conn->prepare($sql);
$stmt->bind_param("s", $titulo);

if ($stmt->execute()) {
    if ($stmt->affected_rows > 0) {
        $response['status'] = 'success';
        $response['message'] = 'Noticia eliminada correctamente.';
    } else {
        $response['status'] = 'error';
        $response['message'] = 'No se encontró una noticia con ese título.';
    }
} else {
    $response['status'] = 'error';
    $response['message'] = 'Error al ejecutar la consulta.';
}

$stmt->close();
$conn->close();

header('Content-Type: application/json');
echo json_encode($response);
?>