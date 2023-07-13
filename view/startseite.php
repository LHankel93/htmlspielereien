<p>--startseite anfang--</p>
<div class="d-flex flex-column flex-md-row p-4 gap-4 py-md-5 align-items-center justify-content-center">
    <div class="list-group">
        <ul>
            <li class="list-group-item list-group-item-action d-flex gap-3 py-3"><a class="btn btn-primary" href="./index.php?site=gitpull&dew=it">Git Pull ausführen</a></li>
            <li class="list-group-item list-group-item-action d-flex gap-3 py-3"><a class="btn btn-danger" href="./index.php?site=gitpush&dew=it">Git Push ausführen</a></li>
        </ul>

    </div>

</div>
<div class="d-flex flex-column flex-md-row p-4 gap-4 py-md-5 align-items-center justify-content-center">
    <div class="list-group">
        <ul>
            <form id="startseite_form" action="./view/pythonwrapper.php" method="post" aria-label="Web-API Links" aria-description="Form mit Buttons als Links zu den einzelnen Funktionen der Web-API">
                <li class="list-group-item list-group-item-action d-flex gap-3 py-3"><input class="btn btn-primary" type="submit" name="foo" value="Button 1 gedrückt" /></li>
                <li class="list-group-item list-group-item-action d-flex gap-3 py-3"><input class="btn btn-primary" type="submit" name="foo" value="Button 2 gedrückt" /></li>
            </form>
        </ul>
    </div>

</div>
<div class="d-flex flex-column flex-md-row p-4 gap-4 py-md-5 align-items-center justify-content-center">
    <div class="list-group">
        <div class="list-group-item list-group-item-action d-flex gap-3 py-3">
            <h6 class="mb-0 opacity-75">Hier wird ein Python Skript angesprochen und der Input Wert +1 gerechnet.</h6>
            <form id="startseite_form_python" action="./view/pythonwrapper.php" method="get" aria-label="Python in PHP aufrufen." aria-description="Form um ein Python Skript zu testen">
                <br>
                <input type="number" name="value" value="1" />
                <input type="submit" class="btn btn-primary" name="operation" value="add1" />
            </form>
        </div>
        <div class="list-group-item list-group-item-action d-flex gap-3 py-3">
            <h6 class="mb-0 opacity-75">Hier wird ein Integer zum Binär-Zahlensystem umgewandelt.</h6>
            <p class="mb-0 opacity-75">

            <form id="startseite_form_python_int2bin" action="./view/pythonwrapper.php" method="get" aria-label="Python in PHP aufrufen." aria-description="Form um ein Python Skript auszuführen.">
                <br>
                <input type="number" name="value" value="1" />
                <input type="submit" class="btn btn-primary" name="operation" value="dec2bin" />
            </form>
            </p>

        </div>

    </div>
</div>


<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.14.7/dist/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
<script src="./assets/bootstrap-4.3.1-dist/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
<p>--startseite ende--</p>