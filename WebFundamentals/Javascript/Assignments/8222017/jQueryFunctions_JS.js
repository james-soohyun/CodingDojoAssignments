$(document).ready(function(){

			$("#hide_p").click(function(){
				$("#hide_show p").hide()
			})

			$("#show_p").click(function(){
				$("#hide_show p").show()
			})

			$("#toggle button").click(function(){
				$("#toggle p").toggle()
			})

			$("#slideUp").click(function(){
				$("#slideDownUp p").slideUp()
			})

			$("#slideDown").click(function(){
				$("#slideDownUp p").slideDown()
			})

			$("#slideToggle button").click(function(){
				$("#slideToggle p").slideToggle()
			})

			$("#fadeIn").click(function(){
				$("#fade p").fadeIn()
			})

			$("#fadeOut").click(function(){
				$("#fade p").fadeOut()
			})

			$("#addClass button").click(function(){
				$("#addClass p").addClass("makePink")
			})

			$("#before button").click(function(){
				$("#before p").before("<a href='www.facebook.com'>Click Me for Facebook!</a>")
			})

			$("#after button").click(function(){
				$("#after p").after("<a href='www.google.com'>Click Me for Google!</a>")
			})

			$("#append button").click(function(){
				$("#append p").append(" My name is James.")
			})

			$("#html button").click(function(){
				$("#html p").html("I have been changed forever....")
			})

			$("#attr button").click(function(){
				var p_class = $("#attr p").attr("class");
				$("#attr p").append( p_class )
			})

			$("#val button").click(function(){
				var multipleValues = $("#multiple").val();
				$("#val p").append(multipleValues.join( ", "));
			})

			$("#text button").click(function(){
				$("#text p").text("Good job I guess...")
			})
		});






































