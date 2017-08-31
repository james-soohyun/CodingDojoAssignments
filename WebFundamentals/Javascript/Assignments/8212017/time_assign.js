function whatTime(hour, min, period)
{
	var hourPart = "";
	var minPart= "";	
	var periodPart = "";
	if (min==0)
	{
		if (hour==12&&min==0)
		{
			if (period=="AM")
			{
				return console.log("It is midnight.");
			}
			else if (period=="PM")
			{
				return console.log("It is noon.");
			}
		}
		else
		{
			if (period=="AM")
			{
				periodPart=" in the morning.";
			}
			else if (period=="PM")
			{
				periodPart=" in the evening.";
			}
			hourPart+=hour;
		}
	}
	else if (min==5)
	{


	}
	else if (min==15)
	{

	}
	else if (min==30)
	{

	}
	else if (min==45)
	{

	}
	else if (min<30)
	{

	}
	else if (min>30)
	{

	}

	if (period == AM)
	{
		var thirdPart = "in the morning";
	}
	else (period == PM)
	{
		var thirdPart = "in the evening";
	}
	console.log("It is " + firstPart + secondPart + thirdPart);
}





// function whatTime(hour, min, period)
// {
// 	if (min<30)
// 	{
// 		if (period == "AM")
// 		{
// 			console.log("It's just after " + hour + " in the morning");
// 		}
// 		else if (period =="PM")
// 		{
// 			console.log("It's just after " + hour + " in the evening");
// 		}
// 	}
// 	else
// 	{
// 		if (period == "AM")
// 		{
// 			console.log("It's almost " + (hour + 1) + " in the morning");
// 		}
// 		else if (period == "PM")
// 		{
// 			console.log("It's almost " + (hour + 1) + " in the evening");
// 		}
// 	}
// }