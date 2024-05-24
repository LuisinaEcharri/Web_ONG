<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "reinvent_reinventar";

// Crear conexión
$conn = new mysqli($servername, $username, $password, $dbname);

// Verificar conexión
if ($conn->connect_error) {
    die("Conexión fallida: " . $conn->connect_error);
}

// Recibir datos del formulario
$nombre = $_POST['nombre'];
$apellido = $_POST['apellido'];
$telefono = $_POST['telefono'];
$email = $_POST['email'];
$tipo = $_POST['tipo'];

// Preparar y bindear
$stmt = $conn->prepare("INSERT INTO inscripto (nombre, apellido, telefono, email, estado, fecha_inscripcion) VALUES (?, ?, ?, ?, ?, NOW())");
$stmt->bind_param("sssss", $nombre, $apellido, $telefono, $email, $tipo);

// Ejecutar la consulta
if ($stmt->execute()) {
    echo "Nuevo registro creado exitosamente";
} else {
    echo "Error: " . $stmt->error;
}

// Cerrar la conexión
$stmt->close();
$conn->close();
?>