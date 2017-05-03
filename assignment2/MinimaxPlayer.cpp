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

int MinimaxPlayer::utility(OthelloBoard b) {

	return b.count_score(b.get_p1_symbol()) - b.count_score(b.get_p2_symbol());
}

std::vector<OthelloBoard> MinimaxPlayer::successor(OthelloBoard b, char symbol) {

	std::vector<OthelloBoard> validMoves;

	for(int row = 0; row < b.get_num_rows(); row++) {
		for(int col = 0; col < b.get_num_cols(); col++) {
			if(b.is_legal_move(col, row, symbol)) {
				OthelloBoard temp = b;
				temp.play_move(col, row, symbol);
				temp.set_row(row);
				temp.set_col(col);
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

int MinimaxPlayer::max_value(OthelloBoard b, char symbol, int& col, int& row) {

	std::vector<OthelloBoard> children;
	std::vector<OthelloBoard>::iterator iter;

	int maximum = -10000;
	int max_row = 0;
	int max_col = 0;

	children = successor(b, symbol);

	if (children.empty()) {
		return utility(b);
	}

	for(iter = children.begin(); iter != children.end(); iter++) {
		int score = std::max(maximum, min_value(*iter, symbol, col, row));
		if (score > maximum) {
			maximum = score;
			max_row = (*iter).get_row();
			max_col = (*iter).get_col();
		}
	}

	row = max_row;
	col = max_col;
	return maximum;
}

int MinimaxPlayer::min_value(OthelloBoard b, char symbol, int& col, int& row) {

	std::vector<OthelloBoard> children;
	std::vector<OthelloBoard>::iterator iter;

	int minimum = 10000;
	int min_row = 0;
	int min_col = 0;

	children = successor(b, symbol);

	if(children.empty()) {
		return utility(b);
	}

	for(iter = children.begin(); iter != children.end(); iter++) {
		int score = std::min(minimum, max_value(*iter, symbol, col, row));
		if (score < minimum) {
			minimum = score;
			min_row = (*iter).get_row();
			min_col = (*iter).get_col();
		}
	}

	row = min_row;
	col = min_col;
	return minimum;
}

void MinimaxPlayer::get_move(OthelloBoard* b, int& col, int& row) {
    // To be filled in by you
		if (symbol == b->get_p1_symbol()) {
			max_value(*b, 'X', col, row);
		}

		else if (symbol == b->get_p2_symbol()) {
			max_value(*b, 'O', col, row);
		}
}

MinimaxPlayer* MinimaxPlayer::clone() {
	MinimaxPlayer* result = new MinimaxPlayer(symbol);
	return result;
}
