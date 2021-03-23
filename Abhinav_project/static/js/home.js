var request = new XMLHttpRequest();
if (String(window.performance.getEntriesByType("navigation")[0].type) === "back_forward") {
    window.location.reload();
}
request.onreadystatechange = function(){
	if(this.readyState == 4 && this.status == 200){
		document.getElementsByClassName("inner_articles")[0].innerHTML = this.responseText;
	}
};
request.open("GET", "get_articles/1", true);
request.send();

document.getElementsByClassName("inner_number")[0].style.backgroundColor = "black";

function page_change(ele){
	window.scrollTo({
  		top: 0,
  		left: 0,
  		behavior: 'smooth'
	});
	var http_request = new XMLHttpRequest();
	http_request.onreadystatechange = function(){
		if(this.readyState == 4 && this.status == 200){
			document.getElementsByClassName("inner_articles")[0].innerHTML = this.responseText;
		}
	}
	http_request.open("GET", "get_articles/" + ele.innerHTML, true);
	http_request.send();
	elements = ele.parentElement.getElementsByClassName("inner_number");
	for(var i = 0; i < elements.length; i++){
		elements[i].style.backgroundColor = "grey";
	}
	ele.style.backgroundColor = "black";
}
var wrapper = document.getElementsByClassName("Outer_wrapper")[0];
var brief_articles = document.getElementsByClassName("brief_articles")[0];
var top_articles = document.getElementsByClassName("top_articles")[0];

if(window.innerWidth < 800 || screen.width < 800){
	wrapper.style.flexDirection = "column-reverse";
	wrapper.style.margin = "0 20px 0 20px";
	brief_articles.style.margin = "0";
	top_articles.style.margin = "0";
	brief_articles.style.width = "100%";
	top_articles.style.width = "100%";
}
else{
	wrapper.style.flexDirection = "row";
	brief_articles.style.width = "50%";
	top_articles.style.width = "40%";
}


window.addEventListener('resize', () =>{
	if(window.innerWidth < 800 || screen.width < 800){
		wrapper.style.flexDirection = "column-reverse";
		wrapper.style.margin = "0 20px 0 20px";
		brief_articles.style.margin = "0";
		top_articles.style.margin = "0";
		brief_articles.style.width = "100%";
		top_articles.style.width = "100%";
	}
	else{
		wrapper.style.flexDirection = "row";
		brief_articles.style.width = "50%";
		top_articles.style.width = "40%";
	}
});

function starring(ele, pk){	
	var request = new XMLHttpRequest();
	if(ele.dataset.choice == "2"){
		request.onreadystatechange = function(){
			if(this.readyState == 4 && this.status == 200){
				ele.innerHTML = "<i class='fas fa-star'></i>";
				var message_container = document.getElementById("messages");
				while(message_container.firstChild){
					 message_container.removeChild(message_container.firstChild);
				}
				var message = document.createElement("div");
				message.classList.add("message");
				message.innerHTML = "" + this.responseText + "<span class='delete_message' onclick='delete_message(this)''>X</span>";
				message_container.appendChild(message);
				var bottom_container = document.getElementById('bottom_messages');
				var bottom_message = document.createElement("div");
				bottom_message.innerHTML = "" + this.responseText + "<span class='delete_message' onclick='delete_message(this)''>X</span>";
				bottom_message.classList.add("bottom_message");
				bottom_container.appendChild(bottom_message);
				ele.dataset.choice = "1";
			}
		}
		request.open("GET", "starring/" + pk, true);
		request.send();
	}
	else if(ele.dataset.choice == "1"){
		request.onreadystatechange = function(){
			if(this.readyState == 4 && this.status == 200){
				console.log(this.responseText);
				var message_container = document.getElementById("messages");
				while(message_container.firstChild){
					 message_container.removeChild(message_container.firstChild);
				}
				var message = document.createElement("div");
				message.classList.add("message");
				message_container.appendChild(message);
				var bottom_container = document.getElementById('bottom_messages');
				var bottom_message = document.createElement("div");
				bottom_message.classList.add("bottom_message");
				bottom_container.appendChild(bottom_message);
				bottom_message.innerHTML = message.innerHTML = "" + this.responseText + "<span class='delete_message' onclick='delete_message(this)''>X</span>";
				message.innerHTML = "" + this.responseText + "<span class='delete_message' onclick='delete_message(this)''>X</span>";
				ele.dataset.choice = "2";
				ele.innerHTML = "<i class='far fa-star'></i>";
			}
		}
		request.open("GET", "unstarring/" + pk, true);
		request.send();
	}
}

function delete_message(ele){
	ele.parentElement.remove();
}