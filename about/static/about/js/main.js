function pageScroll() {
    window.scrollBy(0,1);
    scrolldelay = setTimeout(pageScroll,10);
}

function stopScroll() {
    clearTimeout(scrolldelay);
}

function validateForm(){
    var x = document.forms["searchform"]["searchbox"].value;
    if (x == "") {
        alert("Name must be filled out");
        return false;
    }
}