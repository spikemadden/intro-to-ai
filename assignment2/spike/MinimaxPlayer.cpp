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
	return (b.count_score(b.get_p1_symbol()) - b.count_score(b.get_p2_symbol()));
}

std::vector<OthelloBoard*> MinimaxPlayer::successor(OthelloBoard b, char symbol) {

	std::vector<OthelloBoard*> validMoves;

	for(int row = 0; row < b.get_num_rows(); row++) {
		for(int col = 0; col < b.get_num_cols(); col++) {
			if(b.is_legal_move(col, row, symbol) && b.is_cell_empty(col, row)) {
				OthelloBoard *temp = new OthelloBoard(b);
				temp->play_move(col, row, symbol);
				temp->set_row(row);
				temp->set_col(col);

				validMoves.push_back(temp);
			}
		}
	}

	return validMoves;
}

int MinimaxPlayer::max_value(OthelloBoard b) {

	if(!b.has_legal_moves_remaining(b.get_p1_symbol()) && !b.has_legal_moves_remaining(b.get_p2_symbol())) {
		return utility(b);
	}

	std::vector<OthelloBoard*> children;

	int maximum = -100;

	char symbol = b.get_p1_symbol();
	children = successor(b, symbol);

	for(int i = 0; i < children.size(); i++) {
		maximum = std::max(maximum, min_value(*children[i]));
	}

	return maximum;
}

int MinimaxPlayer::min_value(OthelloBoard b) {

	if(!b.has_legal_moves_remaining(b.get_p1_symbol()) && !b.has_legal_moves_remaining(b.get_p2_symbol())) {
		return utility(b);
	}

	std::vector<OthelloBoard*> children;

	int minimum = 100;

	char symbol = b.get_p2_symbol();
	children = successor(b, symbol);

	for(int i = 0; i < children.size(); i++) {
		minimum = std::min(minimum, max_value(*children[i]));
	}

	return minimum;
}

void MinimaxPlayer::get_move(OthelloBoard* b, int& col, int& row) {
    int best_row = -1;
		int best_col = -1;

		int best_min = 100;

		std::vector<OthelloBoard*> first_children = successor(*b, get_symbol());

		for (int i = 0; i < first_children.size(); i++) {
			int value = max_value(*first_children[i]);
			if (value < best_min) {
				best_min = value;
				best_row = first_children[i]->get_row();
				best_col = first_children[i]->get_col();
			}
		}

		row = best_row;
		col = best_col;
}

MinimaxPlayer* MinimaxPlayer::clone() {
	MinimaxPlayer* result = new MinimaxPlayer(symbol);
	return result;
}
