<?php
if (isset($_GET)) {
    print_r($_GET);
    $a = $_GET['dew'];
    $command = "git push";
    echo ("<br>Das Kommando das ausgeführt wird: $command<br>");
    $output = shell_exec($command);
    echo ('<br>');
    echo $output;
    echo "\n";
    echo "<a class=\"btn btn-primary\" href=\"./index.php\">Zurück zur Startseite</a>";
}
?>