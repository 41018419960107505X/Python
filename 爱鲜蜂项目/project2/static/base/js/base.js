$(document).ready(function () {
    document.documentElement.style.fontSize = innerWidth / 10 + "px";

    //  http://127.0.0.1:8000/cart/
    var url = location.href;
    var spanID = url.split("/")[3];
    var $span = $(document.getElementById(spanID));
    $span.css("background", "url(/static/base/img/"+spanID+"1.png) no-repeat")
    $span.css("background-size", "0.6rem")
});