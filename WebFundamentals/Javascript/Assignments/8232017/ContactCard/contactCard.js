$(document).ready(function(){
	$('#submit').click(function(){
		var name = $("#firstName").val();
		var last = $("#lastName").val();
		var aboutMe = $("#bio").val();
		console.log(name);
		console.log(last);
		console.log(aboutMe);
		$("#contacts").append("<div id='card' style='border: 2px solid black'><p id='front'>" + name + " " + last + "</p><p id='back'>" + aboutMe + "</p></div>");
		$("#firstName").val("");
		$("#lastName").val("");
		$("#bio").val("");
		return false;
	})
	$('#contacts').on('click', '#card', function(){
		$(this).children().toggle();
	})
})