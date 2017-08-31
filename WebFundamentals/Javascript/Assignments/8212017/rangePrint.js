function printRange(start=0, stop, skip=1)
{
	for (start; start<stop; start+=skip)
	{
		console.log(start);
	}
}

printRange(2, 10, 2);
printRange(2,6);