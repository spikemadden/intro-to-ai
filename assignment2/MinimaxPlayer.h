/*
 * MinimaxPlayer.h
 *
 *  Created on: Apr 17, 2015
 *      Author: wong
 */

#ifndef MINIMAXPLAYER_H
#define MINIMAXPLAYER_H

#include "OthelloBoard.h"
#include "Player.h"
#include <vector>

/**
 * This class represents an AI player that uses the Minimax algorithm to play the game
 * intelligently.
 */
class MinimaxPlayer : public Player {
public:

	/**
	 * @param symb This is the symbol for the minimax player's pieces
	 */
	MinimaxPlayer(char symb);

	/**
	 * Destructor
	 */
	virtual ~MinimaxPlayer();

	/**
	 * @param b The board object for the current state of the board
	 * @param col Holds the return value for the column of the move
	 * @param row Holds the return value for the row of the move
	 */
    void get_move(OthelloBoard* b, int& col, int& row);

	/*
	A helper struct that contains a board, and the column and row
	of the latest move
	*/
	struct TreeNode
	{
		int col;
		int row;
		OthelloBoard b;
	};

    /**
     * @return A copy of the MinimaxPlayer object
     * This is a virtual copy constructor
     */
    MinimaxPlayer* clone();
private:
	/*
	The function takes the current board and returns
	an vector of TreeNodes containing all successors that can be reached in
	one move
	*/
	std::vector<TreeNode> successor(OthelloBoard b, char symb);

	/*
	The maximizing function. Returns the MaxValue of a board.
	*/
	int MaxValue(OthelloBoard b);

	/*
	The miimizing function. Returns the MaxValue of a board.
	*/
	int MinValue(OthelloBoard b);

	/**
	This function takes the current board, and returns the "goodness"
	The goodness is in regards to the maximizing player.
	The maximizing player is whoever moves first.
	**/
	int utility(OthelloBoard b);

	/*
	Determines if a board is in a end state.
	It is if neither player can make a move
	*/
	bool GameOver(OthelloBoard b);
};


#endif
