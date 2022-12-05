function saveTextAsFile(fileNameToSaveAs) {
    textToWrite = editor.getValue();
    var textFileAsBlob = new Blob([textToWrite], {type:'text/plain'});
    var downloadLink = document.createElement("a");
    downloadLink.download = fileNameToSaveAs;
    downloadLink.innerHTML = "Download File";
    if (window.webkitURL != null) {
    downloadLink.href = window.webkitURL.createObjectURL(textFileAsBlob);
    }
    else {
    downloadLink.href = window.URL.createObjectURL(textFileAsBlob);
    downloadLink.onclick = destroyClickedElement;
    downloadLink.style.display = "none";
    document.body.appendChild(downloadLink);
    }

    downloadLink.click();
}
