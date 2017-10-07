function NBATeam(name, city, color)
{
	this.name = name;
	this.city = city;
	this.color = color;
	this.players = [];
}

function Player(name, position, jerseyNumber)
{
	this.name = name;
	this.position = position;
	this.jerseyNumber = jerseyNumber;
}

var GSW = new NBATeam("Golden State Warriors", "Oakland", ["blue", "gold"]);
GSW.players.push(new Player("Stephen Curry", "PG", 30));