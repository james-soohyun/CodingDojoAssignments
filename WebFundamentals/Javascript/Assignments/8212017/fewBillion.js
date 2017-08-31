//For loop to calculate accumulation of reward over 30 days that started with 0.01 on the first day and added double the reward amount of the previous day the next day
var reward = 0;

for (var i=0;i<=29;i++)
{
	reward+=(0.01 * Math.pow(2,i));
}
console.log(reward);


//For loop to calculate how many days it would take to accumulate 10,000+ in reward money
var dayThousands = 1;
for (var rewardThousands=0.01;rewardThousands<10000;rewardThousands+=rewardThousands*2)
{
	dayThousands++;
}
console.log(dayThousands);

//For loop to calculate how many days it would take to accumulate 1,000,000,000+ in reward money
var dayBillion = 1;
for (var rewardBillions=0.01;rewardBillions<1000000000;rewardBillions+=rewardBillions*2)
{
	dayBillion++;
}
console.log(dayBillion);

//For loop to calculate how many days it would take to accumulate JavaScript equivalent of infinite reward money
var dayInfinity = 1;
for (var rewardInfinity=0.01;rewardInfinity<=Infinity;rewardInfinity+=rewardInfinity*2)
{
	dayInfinity++;
}
console.log(dayInfinity);