<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Meu app</title>
</head>
<body>
    <h1>Meu app!</h1>

    <h2>Escreva sua mensagem</h2>
    <!-- form para envio de mensagens -->
    <form action="process.php" method="post">
        <input type="text" name="message" id="message">
        <input type="submit" value="Enviar">
    </form>
</body>
</html>