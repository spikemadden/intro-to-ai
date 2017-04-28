/*
 * MinimaxPlayer.cpp
 *
 *  Created on: Apr 17, 2015
 *      Author: wong
 */
#include <iostream>
#include <assert.h>
#include "MinimaxPlayer.h"

using std::vector;

MinimaxPlayer::MinimaxPlayer(char symb) :
		Player(symb) {

}

MinimaxPlayer::~MinimaxPlayer() {

}

std::vector<OthelloBoard*> MinimaxPlayer::sucessor(OthelloBoard* b)
{
	std::vector<OthelloBoard*> validMoves;
	char symb = get_symbol();

	for(int row = 0; row < b->get_num_rows(); row++)
	{
		for(int col = 0; col < b->get_num_cols(); col++)
		{
			if(b->is_legal_move(col, row, symb))
			{
				OthelloBoard* temp = b;
				temp->play_move(col, row, symb);
				validMoves.push_back(temp);
			}
		}
	}

	return validMoves;
}

void MinimaxPlayer::get_move(OthelloBoard* b, int& col, int& row) {
	// To be filled in by you
}

MinimaxPlayer* MinimaxPlayer::clone() {
	MinimaxPlayer* result = new MinimaxPlayer(symbol);
	return result;
}
