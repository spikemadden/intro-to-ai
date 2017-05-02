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

std::vector<OthelloBoard> MinimaxPlayer::successor(OthelloBoard b)
{
	std::vector<OthelloBoard> validMoves;
	char symb = get_symbol();

	for(int row = 0; row < b.get_num_rows(); row++)
	{
		for(int col = 0; col < b.get_num_cols(); col++)
		{
			if(b.is_legal_move(col, row, symb))
			{
				OthelloBoard temp = b;

				temp.play_move(col, row, symb);
				validMoves.push_back(temp);
			}
		}
	}
	std::vector<OthelloBoard>::iterator iter;
	for(iter = validMoves.begin(); iter != validMoves.end(); iter++)
	{
		(*iter).display();
	}

	return validMoves;
}

int MinimaxPlayer::MaxValue(OthelloBoard b)
{
	std::vector<OthelloBoard> children;
	std::vector<OthelloBoard>::iterator iter;
	if(!b.has_legal_moves_remaining(b.get_p1_symbol()))
	{
		return utility(b);
	}
	// Slides say v should be initialized to -infinity???
	int v =  -100;
	children = successor(b);
	printf("(got successors in Max)\n");
	for(iter = children.begin(); iter != children.end(); iter++)
	{
		// (*iter).display();
		int min = MinValue(*iter);

		if(min > v)
		{
			v = std::max(v, min);
			*currentBestMove = (*iter);
		}
	}

	return v;
}

int MinimaxPlayer::MinValue(OthelloBoard b)
{
	std::vector<OthelloBoard> children;
	std::vector<OthelloBoard>::iterator iter;
	if(!b.has_legal_moves_remaining(b.get_p2_symbol()))
	{
		return utility(b);
	}

	int v = 100;
	children = successor(b);

	for(iter = children.begin(); iter != children.end(); iter++)
	{
		int max = MaxValue(*iter);

		if(max < v)
		{
			v = std::min(v, max);
			*currentBestMove = (*iter);
		}
	}

	return v;
}

OthelloBoard* MinimaxPlayer::MiniMaxDecision(OthelloBoard* b)
{
	MaxValue(*b);

	return currentBestMove;
}

void MinimaxPlayer::get_move(OthelloBoard* b, int& col, int& row) {
	OthelloBoard* initial = b;
	OthelloBoard* miniMax = MiniMaxDecision(b);
	// b->display();
	//miniMax->display();
	printf("(Got minimax decision)\n");
	char symbol = get_symbol();

	// find the move
	for(int curRow = 0; curRow < b->get_num_rows(); curRow++)
	{
		for(int curCol = 0; curCol < b->get_num_cols(); curCol++)
		{
			// printf("%c\n", initial->get_cell(curCol, curRow));
			// printf("%c\n", miniMax->get_cell(curCol, curRow));

			// printf("%s %s\n", initial->get_cell(curCol, curRow), miniMax->get_cell(curCol, curRow));
			if(initial->get_cell(curCol, curRow) != miniMax->get_cell(curCol, curRow))
			{
				col = curCol;
				row = curRow;
				return;
			}
		}
	}
}

MinimaxPlayer* MinimaxPlayer::clone() {
	MinimaxPlayer* result = new MinimaxPlayer(symbol);
	return result;
}
