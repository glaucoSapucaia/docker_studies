<?php
    // recuperando dados do form
    $message = $_POST['message'];

    // diretorio de dados (mensagens)
    $files = scandir('./messages');

    // - 2 -> 2 arquivos sao gerados automaticamente na criação do diretorio
    $num_files = count($files) - 2;

    // nome dinamico de arquivos
    $file_name = "msg-{$num_files}.txt";

    // fopen() -> abre arquivo ou URL
    // "x" -> permissão de execução
    $file = fopen("./messages/{$file_name}", "x");

    // criando arquivo de mensagem
    // fwrite() -> cria arquivo
    fwrite($file, $message);

    // fechando arquivo
    fclose($file);

    // redirecionando usuario
    header('Location: index.php');
?>