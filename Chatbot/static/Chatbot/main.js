function showmessage() {

    document.getElementById('chatwindow').innerHTML += "<li> \
								<div class=\"rightside-right-chat\"> \
									<span><i class=\"fa fa-circle\" aria-hidden=\"true\"></i> Gladys </span><br><br> \
									<p> Restaurant </p> \
								</div> \
							</li>"

}

function validateForm() {
    var x = document.forms["myForm"]["message"].value;
    if (x == "") {
        alert("Please Enter Something!");
        return false;
    }

    return true;
}
