<?php
$response = array();


if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Verifica si se ha subido un archivo
    if (isset($_FILES['image']) && $_FILES['image']['error'] === UPLOAD_ERR_OK) {
        $fileTmpPath = $_FILES['image']['tmp_name'];
        $fileName = $_FILES['image']['name'];
        $fileSize = $_FILES['image']['size'];
        $fileType = $_FILES['image']['type'];
        $fileNameCmps = explode(".", $fileName);
        $fileExtension = strtolower(end($fileNameCmps));

        // Sanitiza el nombre del archivo
        $newFileName = md5(time() . $fileName) . '.' . $fileExtension;

        // Carpetas de subida
        $uploadFileDir = '../img/noticias/';
        $dest_path = $uploadFileDir . $newFileName;

        // Crea la carpeta si no existe
        if (!is_dir($uploadFileDir)) {
            mkdir($uploadFileDir, 0777, true);
        }

        // Mueve el archivo subido a la carpeta de destino
        if(move_uploaded_file($fileTmpPath, $dest_path)) {
            $response['message'] = 'File is successfully uploaded.';
            $response['file'] = $dest_path;
        } else {
            $response['message'] = 'There was some error moving the file to upload directory. Please make sure the upload directory is writable by the web server.';
        }
    } else {
        $response['message'] = 'No file uploaded or there was an upload error.';
    }
} else {
    $response['message'] = 'Invalid request method.';
}

// Devuelve la respuesta en formato JSON
echo json_encode($response);
?>