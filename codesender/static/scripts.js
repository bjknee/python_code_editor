let code = ""

function save(){
    var textArea = document.getElementById("coding");
    var output = document.getElementById("save_output");
    code = textArea.value;
    output.innerHTML = "Code snippet has been saved";
}

function pull(){
    var textArea = document.getElementById("coding");
    var output = document.getElementById("save_output");
    textArea.value = code
    output.innerHTML = "<!-- OUTPUT_TWO PLACEHOLDER -->"
}