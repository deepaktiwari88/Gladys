function pageScroll() {
    window.scrollBy(0,1);
    scrolldelay = setTimeout(pageScroll,1);
}

function stopScroll() {
    clearTimeout(scrolldelay);
}

