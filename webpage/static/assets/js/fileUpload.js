(function() {
	document.getElementById("file_input").onchange = function() {
		var files = document.getElementById("file_input").files;
		var file = files[0];
		if (!file) {
			return alert("File has not been selected.");
		}
		getSignedRequest(file);
	};
})();

function getSignedRequest(file){
	var xhr = new XMLHttpRequest();
	xhr.open("GET", "/account/sign_s3?file_name=" + file.name + "&file_type=" + file.type);
	xhr.onreadystatechange = function() {
		if (xhr.readyState === 4) {
			if (xhr.status === 200) {
				var response = JSON.parse(xhr.responseText);
				uploadFile(file, response.data, response.rul);
			} else {
				// alert("Could not get signed URL.");
			}
		}
	}
	xhr.send();
}

function uploadFile(file, s3Data, url) {
	var xhr = new XMLHttpRequest();
	xhr.open("POST", s3Data.url);

	var postData = new FormData();
	for (key in s3Data.fields) {
		postData.append(key, s3Data.fields[key]);
	}
	postData.append('file', file);

	xhr.onreadystatechange = function() {
		if (xhr.readyState === 4) {
			if (xhr.status === 200 || xhr.status === 204) {
				// document.getElementById("file-url").value = url;
				bug = "https://s3-us-west-2.amazonaws.com/cs408bucket/dazzled-bug-by-azzza.png"
				document.getElementById("file-url").value = bug;
			} else {
				alert("Could not upload file!");
			}
		}
	}
	xhr.send(postData);
}