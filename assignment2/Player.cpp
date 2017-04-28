#include "Player.h"

Player::Player(char symb) : symbol(symb) {

}

Player::~Player() {

}

int Player::utility(OthelloBoard* b)
{
	int columns = b->get_num_cols();
	int rows = b->get_num_rows();
	char symb = get_symbol();
	char otherSymb;

	unsigned int xCount = 0;
	unsigned int oCount = 0;

	if (symb == 'O')
	{
		otherSymb = 'X';
	}
	else
	{
		otherSymb = 'O';
	}

	for(int col = 0; col < columns; col++)
	{
		for(int row = 0; row < rows; row++)
		{
			if(b->get_cell(col, row) == 'X')
			{
				xCount++;
			}
			else if(b->get_cell(col, row) == 'O')
			{
				oCount++;
			}
		}
	}

	int goodness = 0;
	if(symb == 'X')
	{
		goodness = xCount - oCount;
	}
	else
	{
		goodness = oCount - xCount;
	}

	return goodness;
}
