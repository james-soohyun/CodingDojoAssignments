$(document).ready(function(){

	$('#submit').click(function(){
	var name = $("#firstName").val();
	var last = $("#lastName").val();
	var emailAddress = $("#emailInput").val();
	var contact = $("#contactNumber").val();
	console.log(name);
	console.log(last);
	console.log(emailAddress);
	console.log(contact);
		$("table").append("<tr><td>" + name + "</td><td>" + last + "</td><td>" + emailAddress + "</td><td>" + contact + "</td></tr>");
		return false;
	})


})