$(document).ready(function()
{
	var nyancat = {y:10, x:19};
	var count=0;
	var board =
		[	[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
			[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
			[1,0,1,0,1,0,1,1,1,1,1,0,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,0,1,1,1,1,1,0,1,0,1,0,1],
			[1,0,1,0,1,0,1,1,1,1,1,0,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,0,1,1,1,1,1,0,1,0,1,0,1],
			[1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1],
			[1,0,1,0,1,1,1,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,0,1,1,1,1,0,1,0,1],
			[1,0,1,0,1,1,1,1,0,1,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,1,0,1,1,1,1,0,1,0,1],
			[1,0,0,0,0,0,0,0,0,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,0,0,0,0,0,0,0,0,1],
			[1,1,1,1,1,1,1,1,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,1,1,1,1,1,1,1,1],
			[1,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,1],
			[1,1,1,1,1,1,1,1,0,1,0,1,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,1,0,1,0,1,1,1,1,1,1,1,1],
			[1,1,1,1,1,1,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,1,5,5,5,5,5,5,5,5,5,5,5,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[1,1,1,1,1,1,1,1,0,1,0,1,0,1,5,5,5,5,5,5,5,5,5,5,5,1,0,1,0,1,0,1,1,1,1,1,1,1,1],
			[1,1,1,1,1,1,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1],
			[1,1,1,1,1,1,1,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,1,1,1,1,1,1,1],
			[1,1,1,1,1,1,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1],
			[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
			[1,0,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,0,1],
			[1,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,1],
			[1,1,1,1,1,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1],
			[1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
			[1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1],
			[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
			[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
		];

		console.log("The board is 39 units wide and 25 units tall");
		console.log("There are 436 coins");

	function DrawWorld()
	{
		var htmlStr = "";
		for (var y=0;y<board.length;y++)
		{
			for (var x=0;x<board[y].length;x++)
			{
				if (board[y][x]==1)
				{
					htmlStr+='<div class="wall"></div>';
				}
				else if (board[y][x]==0)
				{
					htmlStr+='<div class="floor"><img class="coin" src="coin.gif" alt="Cat Coin"></div>';
				}
				else if (board[y][x]==2)
				{
					htmlStr+='<div class="floor"><img id="cat" src="cat.gif" alt="Nyan Cat"></div>';
				}
				else if (board[y][x]==3)
				{
					htmlStr+='<div class="floor"></div>';
				}
				else if (board[y][x]==5)
				{
					htmlStr+='<div class="floor"></div>';
				}
			}
		}
		$("#world").html(htmlStr);
	}
	DrawWorld();

	$(document).on("keydown", "body", function(e){

			//Commands for moving left
			if(e.keyCode == 37 && board[nyancat.y][nyancat.x-1]!==1)
			{
				if (nyancat.x==0)
				{
					board[nyancat.y][nyancat.x]=3;
					nyancat.x=39;
					board[nyancat.y][nyancat.x]=2;
					DrawWorld();
				}
				board[nyancat.y][nyancat.x]=3;
				nyancat.x-=1;
				board[nyancat.y][nyancat.x]=2;
				DrawWorld();
			}

			//Commands for moving up
			if(e.keyCode == 38 && board[nyancat.y-1][nyancat.x]!==1)
			{
				board[nyancat.y][nyancat.x]=3;
				nyancat.y-=1;
				board[nyancat.y][nyancat.x]=2;
				DrawWorld();
			}

			//Commands for moving right
			if(e.keyCode == 39 && board[nyancat.y][nyancat.x+1]!==1)
			{
				if (nyancat.x==39)
				{
					board[nyancat.y][nyancat.x]=3;
					nyancat.x=0;
					board[nyancat.y][nyancat.x]=2;
					DrawWorld();
				}
				board[nyancat.y][nyancat.x]=3;
				nyancat.x+=1;
				board[nyancat.y][nyancat.x]=2;
				DrawWorld();
			}

			//Commands for moving down
			if(e.keyCode == 40 && board[nyancat.y+1][nyancat.x]!==1)
			{
				board[nyancat.y][nyancat.x]=3;
				nyancat.y+=1;
				board[nyancat.y][nyancat.x]=2;
				DrawWorld();
			}
})







})