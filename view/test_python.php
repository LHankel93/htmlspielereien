<?php
if (isset($_GET)) {
    print_r($_GET);
    $a = $_GET['value'];
    if ($_GET['operation'] == 'add1') {
        $command = "python ../pyscripts/pytest.py " . $a;
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
