/*RemoveFront is a function that deletes the first index in an array arr and shifts values over accordingly */
function RemoveFront(arr)
{
	for (var i=0;i<arr.length;i++)
	{
		arr[i]=arr[i+1];
	}
	arr.pop();
	return console.log(arr);
}

/*AddFront takes a value Val and places it at index 0 of array arr and shifts values to the right */
function AddFront(arr, val)
{
	arr.push(0);
	for (var i=1;i<arr.length;i++)
	{
		arr[arr.length-i]=arr[arr.length-i-1];
	}
	arr[0]=val;
	return console.log(arr);
}

/*RemoveAt takes an array arr and an inded value idx and removes the value at arr[idx] */
function RemoveAt(arr, idx)
{
	for (var i=idx;i<arr.length;i++)
	{
		arr[i]=arr[i+1]
	}
	arr.pop();
	return console.log(arr);
}

/*InsertAt takes an array arr, index idx, and a value val and sets the value at arr[idx] equal to val */
function InsertAt(arr, idx, val)
{
	arr.push(0);
	for (var i=arr.length-1;i<idx;i--)
	{
		arr[i]=arr[i-1];
	}
	arr[idx]=val;
	return console.log(arr);
}

/* RevArr takes an array arr and reverses the array */
function RevArr(arr)
{
	for (var idx = 0; idx < arr.length/2; idx++)
	{
		var temp = arr[idx];
		arr[idx] = arr[arr.length-1-idx];
		arr[arr.length-1-idx] = temp;
	}
	return console.log(arr);
}

/* DoubleTrouble will take an array and duplicate the index values adjacent to the originals */
function DoubleTrouble(arr)
{
	var OrigLen = arr.length -1;
	arr.length = arr.length * 2;
	for (var idx = OrigLen; idx>=0; idx--)
	{
		arr[idx * 2] = arr[idx];
		arr[idx * 2 + 1] = arr[idx];
	}
	return console.log(arr);
}

/* RemDupes will remove any duplicate values in an array and return the shortened array */
function RemDupes(arr)
{

}









