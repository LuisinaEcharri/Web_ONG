<?php

$dbhost= "localhost";
$dbuser= "root";
$dbpass= "contramysql";
$dbname= "reinventar";

$conn = mysqli_connect($dbhost, $dbuser, $dbpass, $dbname);
if (!$conn) 
{
	die("No hay conexión: ".mysqli_connect_error());
}

$nombre = $_POST["input_username"];
$pass = $_POST["input_password"];

$query = mysqli_query($conn,"SELECT * FROM usuario WHERE user = '".$nombre."' AND password = '".$pass."'");
$nr = mysqli_num_rows($query);

if($nr == 1)
{
	header("Location: menu.html");
	//echo "Bienvenido:" .$nombre;
}
else if ($nr == 0) 
{
	echo "<script> alert('Datos incorrectos');window.location= 'login.html' </script>";
    //header("Location: login.html");
	//echo "No ingreso"; 
}

?>