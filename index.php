<?php
session_start();

if (!isset($_SESSION['usuarios'])) {
    $_SESSION['usuarios'] = [];
}

// CREAR
if (isset($_POST['crear'])) {
    $nombre = $_POST['nombre'];
    $email = $_POST['email'];

    if ($nombre != "" && filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $_SESSION['usuarios'][] = ["nombre" => $nombre, "email" => $email];
    }
}

// ELIMINAR
if (isset($_GET['delete'])) {
    $index = $_GET['delete'];
    unset($_SESSION['usuarios'][$index]);
    $_SESSION['usuarios'] = array_values($_SESSION['usuarios']);
}

// EDITAR (CARGAR DATOS)
$editIndex = -1;
$editNombre = "";
$editEmail = "";

if (isset($_GET['edit'])) {
    $editIndex = $_GET['edit'];
    $editNombre = $_SESSION['usuarios'][$editIndex]['nombre'];
    $editEmail = $_SESSION['usuarios'][$editIndex]['email'];
}

// ACTUALIZAR
if (isset($_POST['update'])) {
    $index = $_POST['index'];

    if ($_POST['nombre'] != "" && filter_var($_POST['email'], FILTER_VALIDATE_EMAIL)) {
        $_SESSION['usuarios'][$index] = [
            "nombre" => $_POST['nombre'],
            "email" => $_POST['email']
        ];
    }
}
?>

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>CRUD Usuarios</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

<div class="container">

    <h2>CRUD de Usuarios</h2>

    <!-- FORMULARIO -->
    <form method="POST">
        <input type="hidden" name="index" id="index" value="<?php echo $editIndex; ?>">

        <input type="text" name="nombre" id="nombre" placeholder="Nombre"
               value="<?php echo $editNombre; ?>" required>

        <input type="email" name="email" id="email" placeholder="Email"
               value="<?php echo $editEmail; ?>" required>

        <?php if ($editIndex >= 0): ?>
            <button type="submit" name="update" id="btnUpdate">Actualizar</button>
        <?php else: ?>
            <button type="submit" name="crear" id="btnCrear">Crear</button>
        <?php endif; ?>
    </form>

    <!-- TABLA -->
    <h2>Lista de Usuarios</h2>

    <table>
        <tr>
            <th>Nombre</th>
            <th>Email</th>
            <th>Acciones</th>
        </tr>

        <?php if (empty($_SESSION['usuarios'])): ?>
            <tr>
                <td colspan="3">No hay usuarios registrados</td>
            </tr>
        <?php endif; ?>

        <?php foreach ($_SESSION['usuarios'] as $i => $user): ?>
        <tr>
            <td><?php echo htmlspecialchars($user['nombre']); ?></td>
            <td><?php echo htmlspecialchars($user['email']); ?></td>
            <td>
                <a href="?edit=<?php echo $i; ?>" id="editBtn">Editar</a>
                <a href="?delete=<?php echo $i; ?>" id="deleteBtn">Eliminar</a>
            </td>
        </tr>
        <?php endforeach; ?>
    </table>

</div>

</body>
</html>