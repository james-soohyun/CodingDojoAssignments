$(document).ready(function(){
	for (var i=1;i<=151;i++)
	{
		$("#pokemon").append("<img src='http://pokeapi.co/media/img/" + i + ".png'>");
	}
})