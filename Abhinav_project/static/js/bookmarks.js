var request = new XMLHttpRequest();

if (String(window.performance.getEntriesByType("navigation")[0].type) === "back_forward") {
    window.location.reload();
}

request.onreadystatechange = function() {
	if(this.readyState == 4 && this.status == 200){
		document.getElementsByClassName('outer_articles')[0].innerHTML = this.responseText;
	}
};
request.open("GET", "get_bookmarks/1", true);
request.send();

document.getElementsByClassName("inner_number")[0].style.backgroundColor = "black";

function page_change(ele){
	var http_request = new XMLHttpRequest();
	http_request.onreadystatechange = function(){
		if(this.readyState == 4 && this.status == 200){
			document.getElementsByClassName("outer_articles")[0].innerHTML = this.responseText;
		}
	}
	console.log("here");
	console.log(ele.innerHTML);
	http_request.open("GET", "get_bookmarks/" + ele.innerHTML, true);
	http_request.send();
	elements = ele.parentElement.getElementsByClassName("inner_number");
	for(var i = 0; i < elements.length; i++){
		elements[i].style.backgroundColor = "grey";
	}
	ele.style.backgroundColor = "black";
}

function unmark(ele, id){
	console.log(id);
	let request = new XMLHttpRequest();
	request.onreadystatechange = function(){
		if(this.readyState == 4 && this.status == 200){
			let message = document.createElement("div");
			message.classList.add('message');
			let bottom_message = document.createElement("div");
			bottom_message.classList.add('bottom_message');
			message.innerHTML = "" + this.responseText + "<span class='delete_message' onclick='delete_message(this)''>X</span>";
			bottom_message.innerHTML = "" + this.responseText + "<span class='delete_message' onclick='delete_message(this)''>X</span>";
			document.getElementById("messages").appendChild(message);
			document.getElementById("bottom_messages").appendChild(bottom_message);
			ele.parentElement.parentElement.parentElement.parentElement.remove();
		}
	}
	let csrf = document.getElementsByName('csrfmiddlewaretoken')[0];
	request.open("DELETE", "unstarring/" + id, true);
	request.setRequestHeader('X-CSRFToken', csrf.value);
	request.send();
}

function cancel(ele){
	ele = ele.parentElement.parentElement;
	ele.style.display = "none";
}

function delete_message(ele){
	ele.parentElement.remove();
}