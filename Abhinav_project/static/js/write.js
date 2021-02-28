var ele = document.getElementById("image");
ele.addEventListener("change", () => {
	var name = ele.files[0].name;
	name = name.slice(-3);
	if(name == 'jpg' && name == 'png'){
		//var image = ele.files[0];
		console.log("this is amazing");
	}
});