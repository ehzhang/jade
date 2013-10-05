var xmlhttp;

function refresh() {
    if (window.XMLHttpRequest) {
        xmlhttp=new XMLHttpRequest();
    }
        xmlhttp.onreadystatechange=function() {
                if (xmlhttp.readyState==4 && xmlhttp.status==200) {
                document.getElementById("myDiv").innerHTML=xmlhttp.responseText; // CHANGE THE DIV ELEMENT
        }
        }
        xmlhttp.open("GET","demo_get.asp",true); // CHANGE THE GET URL
        xmlhttp.send();
}
var int = setInterval(function() {refresh()}, 1000);
