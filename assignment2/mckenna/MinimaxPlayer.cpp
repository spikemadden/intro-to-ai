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

std::vector<MinimaxPlayer::TreeNode> MinimaxPlayer::successor(OthelloBoard b, char symb)
{
	std::vector<MinimaxPlayer::TreeNode> validMoves;

	for(int row = 0; row < b.get_num_rows(); row++)
	{
		for(int col = 0; col < b.get_num_cols(); col++)
		{
			if(b.is_legal_move(col, row, symb) && b.is_cell_empty(col, row))
			{
				OthelloBoard temp = b;
				temp.play_move(col, row, symb);
				TreeNode toAdd = {col, row, temp};
				validMoves.push_back(toAdd);
			}
		}
	}
	return validMoves;
}

int MinimaxPlayer::MaxValue(OthelloBoard b)
{
	std::vector<TreeNode> children;
	if(GameOver(b))
	{
		return utility(b);
	}

	int v = -9999;

	// p1 is always maximizing
	char symb = b.get_p1_symbol();
	children = successor(b, symb);

	for(int i = 0; i < children.size(); i++)
	{
		v = std::max(v, MinValue(children[i].b));
	}

	return v;
}

int MinimaxPlayer::MinValue(OthelloBoard b)
{
	std::vector<TreeNode> children;
	if(GameOver(b))
	{
		return utility(b);
	}

	int v = 9999;

	// p2 is always minimizing
	char symb = b.get_p2_symbol();
	children = successor(b, symb);

	for(int i = 0; i < children.size(); i++)
	{
		v = std::min(v, MaxValue(children[i].b));
	}

	return v;
}

void MinimaxPlayer::get_move(OthelloBoard* b, int& col, int& row) {
	TreeNode bestBoard = {-1, -1, *b};
	int minBest = 9999;
	int maxBest = -9999;

	// Get first level of successors here.
	std::vector<TreeNode> children = successor(*b, get_symbol());

	for(int i = 0; i < children.size(); i++)
	{
		if(b->get_p1_symbol() == get_symbol())
		{
			int v = MinValue(children[i].b);
			if(v > maxBest)
			{
				maxBest = v;
				bestBoard = children[i];
			}
		}
		// For the puroses of testing this assignment
		// we will always end up in this block
		else
		{
			int v = MaxValue(children[i].b);
			if(v < minBest)
			{
				minBest = v;
				bestBoard = children[i];
			}
		}
	}
	col = bestBoard.col;
	row = bestBoard.row;
}

bool MinimaxPlayer::GameOver(OthelloBoard b)
{
	if(!b.has_legal_moves_remaining(b.get_p2_symbol()) && !b.has_legal_moves_remaining(b.get_p1_symbol()))
	{
		return true;
	}
	else
	{
		return false;
	}
}

int MinimaxPlayer::utility(OthelloBoard b)
{
	int p1Score = b.count_score(b.get_p1_symbol());
	int p2Score = b.count_score(b.get_p2_symbol());

	return p1Score - p2Score;
}

MinimaxPlayer* MinimaxPlayer::clone() {
	MinimaxPlayer* result = new MinimaxPlayer(symbol);
	return result;
}
