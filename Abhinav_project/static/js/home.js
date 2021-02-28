var request = new XMLHttpRequest();
request.onreadystatechange = function(){
	if(this.readyState == 4 && this.status == 200){
		console.log(this.responseText);
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
	console.log(ele.innerHTML);
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