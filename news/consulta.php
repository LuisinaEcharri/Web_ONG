<?php

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

// Verificar conexión
if ($conn->connect_error) {
    die("Conexión fallida: " . $conn->connect_error);
}

// Consulta predefinida
$query = "SELECT * FROM noticia ORDER BY id_noticia DESC LIMIT 5";

// Array para almacenar los resultados
$data = array();

if ($result = $conn->query($query)) {
    while ($row = $result->fetch_assoc()) {
        $data[] = $row;
    }
    $result->free();
} else {
    die("Error en la consulta: " . $conn->error);
}

// Cerrar la conexión
$conn->close();

// Convertir los datos a JSON
$json_data = json_encode($data, JSON_PRETTY_PRINT);

// Guardar los datos JSON en un archivo
file_put_contents('datos.json', $json_data);

// Redirigir a la página de visualización
header('Location: news.php');
exit();
?>