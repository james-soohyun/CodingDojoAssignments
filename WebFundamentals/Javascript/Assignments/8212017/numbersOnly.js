function numbersOnly(arr)
{
	var newArray = [];
	for (var i=0;i<arr.length;i++)
	{
		if (typeof arr[i] === "number")
		{
			newArray.push(arr[i]);
		}
	}
	return newArray;
}

var arr = [1, "apple", -3, "orange", 0,5];
console.log(numbersOnly(arr));

