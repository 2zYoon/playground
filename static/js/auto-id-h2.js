// https://www.geeksforgeeks.org/how-to-dynamically-insert-id-into-table-element-using-javascript/

function autoh2ID(){
    // Getting the h2 element
    var h2s = document
        .getElementsByTagName("h2");

    // Looping over h2s
    for (var i = 0; i < h2s.length; i++) {

        // Get the ith h2
        var h2 = h2s[i];
        h2.setAttribute("id", i)
    }
}

function autolinktoh2(){
    var links = document.getElementsByClassName("link2h2");
    for (var i = 0; i < links.length; i++) {
        var link = links[i];
        link.setAttribute("href", "#" + i)
    }
}

autoh2ID()
autolinktoh2()