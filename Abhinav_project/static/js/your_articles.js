var request = new XMLHttpRequest();

request.onreadystatechange = function() {
	if(this.readyState == 4 && this.status == 200){
		document.getElementsByClassName('outer_articles')[0].innerHTML = this.responseText;
	}
};
request.open("GET", "get_my_articles/1", true);
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
	http_request.open("GET", "get_my_articles/" + ele.innerHTML, true);
	http_request.send();
	elements = ele.parentElement.getElementsByClassName("inner_number");
	for(var i = 0; i < elements.length; i++){
		elements[i].style.backgroundColor = "grey";
	}
	ele.style.backgroundColor = "black";
}

function article_delete(ele){
	ele = ele.parentElement.parentElement.parentElement.parentElement;
	ele.getElementsByClassName("model")[0].style.display = "flex";
}

function cancel(ele){
	ele = ele.parentElement.parentElement;
	ele.style.display = "none";
}