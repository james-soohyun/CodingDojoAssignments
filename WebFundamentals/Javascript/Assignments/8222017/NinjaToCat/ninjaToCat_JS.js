$(document).ready(function(){
	$("img").click(function(){
		var ninja = $(this).attr("data-alt-src");
		$(this).attr("src",ninja);
	})
})