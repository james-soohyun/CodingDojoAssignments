function randomChance(totalQuarters)
{
	var chance = Math.floor(Math.random()*100) + 1;
	if (chance == 1)
	{
		totalQuarters+=(Math.floor(Math.random()*51) + 50);
	}
	else
		totalQuarters-=1;
}