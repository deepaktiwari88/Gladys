function pageScroll() {
    window.scrollBy(0,1);
    scrolldelay = setTimeout(pageScroll,10);
}

function stopScroll() {
    clearTimeout(scrolldelay);
}

