<?php
if (isset($_GET)) {
    // GET ausgeben für Debugging
    print_r($_GET);
    // a wird der Wert value zugewiesen
    $a = $_GET['value'];

    // Prüfen welche Operation angefordert wurde (add1, dec2bin, etc...)
    if ($_GET['operation'] == 'add1') {
        $command = "python ../pyscripts/add1.py " . $a;
        echo ("<br>Das Kommando das ausgeführt wird: $command<br>");
        $output = shell_exec($command);
        echo ('<br>');
        echo $output;
    }

    if ($_GET['operation'] == 'dec2bin') {
        $command = "python ../pyscripts/decimal2bin.py " . $a;
        echo ("<br>Das Kommando das ausgeführt wird: $command<br>");
        $output = shell_exec($command);
        echo ('<br>');
        echo $output;
    }
}
