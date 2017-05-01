/*
 * MinimaxPlayer.cpp
 *
 *  Created on: Apr 17, 2015
 *      Author: wong
 */
#include <iostream>
#include <assert.h>
#include <algorithm>
#include "MinimaxPlayer.h"

using std::vector;

MinimaxPlayer::MinimaxPlayer(char symb) :
		Player(symb) {

}

MinimaxPlayer::~MinimaxPlayer() {

}

std::vector<OthelloBoard*> MinimaxPlayer::successor(OthelloBoard* b)
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

int MinimaxPlayer::MaxValue(OthelloBoard* b)
{
	std::vector<OthelloBoard*> children;
	std::vector<OthelloBoard*>::iterator iter;
	if(!b->has_legal_moves_remaining(get_symbol()))
	{
		return utility(b);
	}
	// Slides say v should be initialized to -infinity???
	int v =  0;
	children = successor(b);

	for(iter = children.begin(); iter != children.end(); iter++)
	{
		v = std::max(v, MinValue(*iter));
	}

	return v;
}

int MinimaxPlayer::MinValue(OthelloBoard* b)
{
	std::vector<OthelloBoard*> children;
	std::vector<OthelloBoard*>::iterator iter;
	if(!b->has_legal_moves_remaining(get_symbol()))
	{
		return utility(b);
	}

	int v = 0;
	children = successor(b);

	for(iter = children.begin(); iter != children.end(); iter++)
	{
		v = std::min(v, MaxValue(*iter));
	}

	return v;
}

void MinimaxPlayer::get_move(OthelloBoard* b, int& col, int& row) {
	// To be filled in by you
}

MinimaxPlayer* MinimaxPlayer::clone() {
	MinimaxPlayer* result = new MinimaxPlayer(symbol);
	return result;
}
