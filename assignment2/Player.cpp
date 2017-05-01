#include "Player.h"

Player::Player(char symb) : symbol(symb) {

}

Player::~Player() {

}

int Player::utility(OthelloBoard* b)
{
	char p1Symbol = b->get_p1_symbol();
	char p2Symbol = b->get_p2_symbol();

	int p1Score = b->count_score(p1Symbol);
	int p2Score = b->count_score(p2Symbol);

	int goodness = 0;
	if(p1Score > p2Score)
	{
		goodness = 10;
	}
	else
	{
		goodness = -10;
	}
	return goodness;

	// if (symb == 'O')
	// {
	// 	otherSymb = 'X';
	// }
	// else
	// {
	// 	otherSymb = 'O';
	// }
	//
	// for(int col = 0; col < columns; col++)
	// {
	// 	for(int row = 0; row < rows; row++)
	// 	{
	// 		if(b->get_cell(col, row) == 'X')
	// 		{
	// 			xCount++;
	// 		}
	// 		else if(b->get_cell(col, row) == 'O')
	// 		{
	// 			oCount++;
	// 		}
	// 	}
	// }
	//
	// int goodness = 0;
	// if(symb == 'X')
	// {
	// 	goodness = xCount - oCount;
	// }
	// else
	// {
	// 	goodness = oCount - xCount;
	// }
	//
	// return goodness;
}
