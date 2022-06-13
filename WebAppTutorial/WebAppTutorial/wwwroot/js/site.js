// Please see documentation at https://docs.microsoft.com/aspnet/core/client-side/bundling-and-minification
// for details on configuring this project to bundle and minify static web assets.

// Write your Javascript code.

function newColor() {
    document.getElementById("hello_world").style.color = "blue";
}

function oldColor() {
    document.getElementById("hello_world").style.color = "white";
}

var id = null;

function boxMove() {
    var box = document.getElementById("myAnimation");
    /* starting position */
    var pos = 0;
    clearInterval(id);
    id = setInterval(frame, 10);
    /* upon reaching 350px will stop */
    function frame() {
        if (pos == 350) {
            clearInterval(id);
        }
        else {
            pos++;
            box.style.top = pos + 'px';
            box.style.left = pos + 'px';
        }
    }
}