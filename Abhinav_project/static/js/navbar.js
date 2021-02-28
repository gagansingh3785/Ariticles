function change(){
	var ele = document.getElementsByClassName("hidden")[0];
	if(ele.style.display != "none"){
		console.log("inside if");
		ele.style.display = "none";
	}
	else{
		console.log("here");
		ele.style.display = "block";
	}
}

window.addEventListener('resize', () => {
	if(window.innerWidth > 800 || screen.innerWidth > 800){
		document.getElementsByClassName("hidden")[0].style.display = "none";
	}
});