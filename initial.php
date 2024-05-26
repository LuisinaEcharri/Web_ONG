<?php

$dbhost= "localhost";
$dbuser= "root";
$dbpass= "";
$dbname= "reinvent_reinventar";
// $dbhost= "149.56.87.21:3306";
// $dbuser= "reinvent_admin";
// $dbpass= "xu@xDR_;9kpO";
// $dbname= "reinvent_reinventar";

try {
    // Crear una nueva conexión PDO
    $pdo = new PDO("mysql:host=" . $dbhost, $dbuser, $dbpass);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Crear la base de datos si no existe
    $pdo->exec("CREATE DATABASE IF NOT EXISTS " . $dbname);

    // Cerrar la conexión inicial
    $pdo = null;

    // Volver a conectar con la nueva base de datos
    $pdo = new PDO("mysql:host=" . $dbhost . ";dbname=" . $dbname, $dbuser, $dbpass);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Verificar si las tablas existen
    $tables = array("usuario", "inscripto", "noticia");

    foreach ($tables as $table) {
        $checkTable = $pdo->query("SHOW TABLES LIKE '$table'");

        if ($checkTable->rowCount() == 0) {
            // Si la tabla no existe, leer el archivo SQL y ejecutarlo
            $sql = file_get_contents('reinvent_reinventar.sql');
            $pdo->exec($sql);
            break;
        }
    }
} catch (PDOException $e) {
    die("Error: " . $e->getMessage());
}
?>
