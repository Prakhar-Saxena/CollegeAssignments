#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <time.h>
#include <sys/types.h>
#include <semaphore.h>
#include <signal.h>

extern const int DIR_LEFT;
extern const int DIR_RIGHT;

typedef struct square_struct {
  int value;
} Square;

typedef struct row_struct {
  int* squares;
} Row;

typedef struct board_struct {
  int finished;
	int dimension;
  Row* rows;
} Board;

typedef struct game_move {
  int row;
  int col;
} GameMove;

const int DIR_LEFT = 0;
const int DIR_RIGHT = 1;

void generate_board(Board** board, int dimension) {
	int i, j;
  *board = (Board*) malloc(sizeof(Board));
  (*board)->dimension = dimension;
  (*board)->finished = 0;
  (*board)->rows = (Row*) malloc(sizeof(Row) * dimension);
  for (i = 0; i < dimension; i++) {
    (*board)->rows[i].squares = (int*) malloc(sizeof(int) * dimension);
    for(j = 0; j < dimension; j++) {
      (*board)->rows[i].squares[j] = 0;
    }
  }
}

void dealloc(Board* board) {
  int i;
  for (i = 0; i < board->dimension; i++) {
    free(board->rows[i].squares);
  }
  free(board->rows);
  free(board);
}

GameMove* placePieceAtPosition(Board* board, int pieceValue, int row, int col) {
  if((row < 0 || row > board->dimension) || (col < 0 || col > board->dimension)) return NULL;
  if(pieceValue < 0 || pieceValue > 2) return NULL;
  int topRow = findFirstOpenPosition(board, col);
  if (topRow == -1) {
    return NULL;
  }
  board->rows[topRow].squares[col] = pieceValue;
  GameMove* move = (GameMove*) malloc(sizeof(GameMove));
  move->row = topRow;
  move->col = col;
  return move;
}

GameMove* placePieceInColumn(Board* board, int pieceValue, int col) {
  return placePieceAtPosition(board, pieceValue, 0, col);
}

GameMove* findPieceAtBestPosition(Board* board, int pieceValue) {
  srand((unsigned int) time(NULL));
  int best_row = board->dimension - 1, best_col = rand() % (board->dimension);
  int current_lowest_moves = 4;
  int i, j, k;
  for (i = 0; i < board->dimension; i++) {
    int firstOpen = findFirstOpenPosition(board, i);
    if(firstOpen != (board->dimension - 1)) {
      int minimum_moves = 4;
      // check down
      for(j = firstOpen; j < board->dimension; j++) {
        if(board->rows[j].squares[i] == pieceValue) {
          minimum_moves--;
        } else {
          break;
        }
      }
      if(minimum_moves < current_lowest_moves) {
        current_lowest_moves = minimum_moves;
        best_row = j;
        best_col = i;
      }
      // check down - right
      minimum_moves = 4;
      for (j = firstOpen, k = i;
           j < board->dimension && k < board->dimension;
           j++, k++) {
        if(board->rows[j].squares[k] == pieceValue) {
          minimum_moves--;
        } else {
          break;
        }
      }
      if(minimum_moves < current_lowest_moves) {
        current_lowest_moves = minimum_moves;
        best_row = j;
        best_col = i;
      }
      // check down - left
      minimum_moves = 4;
      for (j = firstOpen, k = i;
           j < board->dimension && k > -1;
           j++, k--) {
        if(board->rows[j].squares[k] == pieceValue) {
          minimum_moves--;
        } else {
          break;
        }
      }
      if(minimum_moves < current_lowest_moves) {
        current_lowest_moves = minimum_moves;
        best_row = j;
        best_col = i;
      }
    }
    if(i != 0) {
      int minimum_moves = 4;
      // check  left
      for(j = i - 1; j > -1; j--) {
        if(board->rows[firstOpen].squares[j] == pieceValue) {
          minimum_moves--;
        } else {
          break;
        }
      }
      if(minimum_moves < current_lowest_moves) {
        current_lowest_moves = minimum_moves;
        best_row = firstOpen;
        best_col = i;
      }
      
    }
    if(i != board->dimension - 1) {
      int minimum_moves = 4;
      // check right
      for(j = i + 1; j < board->dimension; j++) {
        if(board->rows[firstOpen].squares[j] == pieceValue) {
          minimum_moves--;
        } else {
          break;
        }
      }
      if(minimum_moves < current_lowest_moves) {
        current_lowest_moves = minimum_moves;
        best_row = firstOpen;
        best_col = i;
      }
    }
  }
  GameMove* bestMove = (GameMove*) malloc(sizeof(GameMove));
  bestMove->row = best_row;
  bestMove->col = best_col;
  return bestMove;
}

GameMove* placePieceAtBestPosition(Board* board, int pieceValue) {
  srand((unsigned int) time(NULL));
  int best_row = rand() % (board->dimension), best_col = rand() % (board->dimension);
  int current_lowest_moves = 4;
  int highest_piece_sequence = 0, current_piece_sequence;
  int i, j, k;
  for (i = 0; i < board->dimension; i++) {
    int firstOpen = findFirstOpenPosition(board, i);
    if(firstOpen != (board->dimension - 1)) {
      int minimum_moves = 4;
      // check down
      for(j = firstOpen; j < board->dimension; j++) {
        if(board->rows[j].squares[i] == pieceValue) {
          minimum_moves--;
        } else {
          break;
        }
      }
      if(minimum_moves < current_lowest_moves) {
        current_lowest_moves = minimum_moves;
        best_row = j;
        best_col = i;
      }
      // check down - right
      minimum_moves = 4;
      for (j = firstOpen, k = i;
           j < board->dimension && k < board->dimension;
           j++, k++) {
        if(board->rows[j].squares[k] == pieceValue) {
          minimum_moves--;
        } else {
          break;
        }
      }
      if(minimum_moves < current_lowest_moves) {
        current_lowest_moves = minimum_moves;
        best_row = j;
        best_col = i;
      }
      // check down - left
      minimum_moves = 4;
      for (j = firstOpen, k = i;
           j < board->dimension && k > -1;
           j++, k--) {
        if(board->rows[j].squares[k] == pieceValue) {
          minimum_moves--;
        } else {
          break;
        }
      }
      if(minimum_moves < current_lowest_moves) {
        current_lowest_moves = minimum_moves;
        best_row = j;
        best_col = i;
      }
    }
    if(i != 0) {
      int minimum_moves = 4;
      // check left
      for(j = i - 1; j > -1; j--) {
        if(board->rows[firstOpen].squares[j] == pieceValue) {
          minimum_moves--;
        } else {
          break;
        }
      }
      if(minimum_moves < current_lowest_moves) {
        current_lowest_moves = minimum_moves;
        best_row = firstOpen;
        best_col = i;
      }
      
    }
    if(i != board->dimension - 1) {
      int minimum_moves = 4;
      // check right
      for(j = i + 1; j < board->dimension; j++) {
        if(board->rows[firstOpen].squares[j] == pieceValue) {
          minimum_moves--;
        } else {
          break;
        }
      }
      if(minimum_moves < current_lowest_moves) {
        current_lowest_moves = minimum_moves;
        best_row = firstOpen;
        best_col = i;
      }
    }
  }
  return placePieceAtPosition(board, pieceValue, best_row, best_col);
}

int checkForWin(Board* board, int pieceValue) {
  int matches = 0, topPiece, i, win = 0;
  for (i = 0; i < board->dimension; i++) {
    topPiece = findTopPiecePosition(board, i);
    if (board->rows[topPiece].squares[i] == 0) {
      continue;
    } else {
      if(i >= 3) {
        // check left
        matches = searchHorizontally(board, pieceValue, DIR_LEFT, topPiece, i);
        if(matches == 4) return 1;
        matches = 0;
        // check down - left
        if(topPiece <= (board->dimension - 1) - 3) {
          matches = searchDiagonally(board, pieceValue, DIR_LEFT, topPiece, i);
          if(matches == 4) return 1;
          matches = 0;
        }
        // check down - right
        if(topPiece != board->dimension - 1) {
          matches = searchDiagonally(board, pieceValue, DIR_RIGHT, topPiece, i);
          if(matches == 4) return 1;
          matches = 0;
        }
      }
      // check the right-most column
      if(i <= (board->dimension - 1) - 3) {
        // check right
        matches = searchHorizontally(board, pieceValue, DIR_RIGHT, topPiece, i);
        if(matches == 4) return 1;
        matches = 0;
        // check up - right
        if(topPiece != 0) {
        }
        // check down - right
        if(topPiece != board->dimension - 1) {
        }
      }
      if(topPiece <= (board->dimension - 1)) {
        matches = searchDown(board, pieceValue, topPiece, i);
        if(matches == 4) return 1;
        matches = 0;
      }
    }
  }
  win = matches;
  return win;
}

// returns length of piece sequence
int searchHorizontally(Board* board, int search, int direction, int row, int col) {
  int matches = 0, j;
  // search left
  if(direction == DIR_LEFT) {
    for(j = col; j > -1; j--) { // loops through the row using columns/cells
      if(board->rows[row].squares[j] == search) {
        matches++;
      } else {
        break;
      }
    }
  }
  // search right
  else if(direction == DIR_RIGHT) {
    for(j = col; j < board->dimension; j++) {
      if(board->rows[row].squares[j] == search) {
        matches++;
      } else {
        break;
      }
    }
  }
  return matches;
}

// Searches diagonally left-down or right-down
int searchDiagonally(Board* board, int search, int diretion, int row, int col) {
  int matches = 0, j, k;
  if(diretion == DIR_LEFT) {
    for (j = row, k = col;
         j < board->dimension && k > -1;
         j++, k--) { // going down - left
      if(board->rows[j].squares[k] == search) {
        matches++;
      } else {
        break;
      }
    }
  }
  else if(diretion == DIR_RIGHT) {
    for (j = row, k = col;
         j < board->dimension && k < board->dimension;
         j++, k++) { //going down - right
      if(board->rows[j].squares[k] == search) {
        matches++;
      } else {
        break;
      }
    }
  }
  
  return matches;
}

// Searches down, search up not required, since that condition will be covered by the cells on top
int searchDown(Board* board, int search, int row, int col) {
  int j;
  int matches = 0;
  for(j = row; j < board->dimension; j++) { // looping throught the column using rows/cells
    if(board->rows[j].squares[col] == search) {
      matches++;
    } else {
      break;
    }
  }
  return matches;
}

// Finds position of topmost empty space
int findFirstOpenPosition(Board* board, int col) {
  int i = 0;
  for(i = board->dimension - 1; i > -1; i--) {
    if(board->rows[i].squares[col] == 0) break;
  }
  return i;
}

// Similar to above function, but returns position of topmost piece
int findTopPiecePosition(Board* board, int col) {
  int i;
  for(i = 0; i < board->dimension; i++) {
    if(board->rows[i].squares[col] != 0) break;
  }
	i = (i == board->dimension) ? i - 1 : i;
  return i;
}

// Print out the board
// Parent pieces in blue
// Child pieces in yellow
// Because Drexel
void printBoard(Board* board) {
  int i, j;
  for(i = 0; i < board->dimension; i++) {
    printf("%d   ", board->dimension - 1 - i);
    for(j = 0; j < board->dimension; j++) {
      switch (board->rows[i].squares[j]) {
        case 0:
          printf("- ");
          break;
        case 1:
          printf("\033[1;34mX \033[0m");
          break;
        case 2:
          printf("\033[1;31mX \033[0m");
          break;
        default:
          break;
      }
    }
    printf("\n");
  }
  printf("    ");
  for (i = 0; i < board->dimension; i++) {
    printf("%d ", i);
  }
  printf("\n\n");
}


//////////////////////////////////////////////////////////////////////////////////////

// zombie garbage collector!
void reaper(int s) {
	int status = s;
	printf("Killed zombie!\n");
}

int rand_lim(int limit);

int main (int argc, char const *argv[])
{
  // Dimension of the boards and number of children to spawn
	int dimension = 8, children = 2, i, j;
  char* env_dimension = getenv("DIMENSION");
  if(env_dimension != NULL) {
    dimension = atoi(env_dimension);
  }
  char* env_children = getenv("GAMES");
  if(env_children != NULL) {
    children = atoi(env_children);
  }
  // Flag for child intelligence
  int child_play_to_win = 0;

  // Multi-dimensional array of file descriptors for pipes
	int fd[children][2][2];
  
  // Array of child process ids
	pid_t childpid[children];
  
  // Array of Boards
	Board** boards = (Board**) malloc(sizeof(Board*) * children);
  
  // Handle child exit
	// signal(SIGCHLD, reaper);
  
  // Only need one move because moves happen sequentially.
  GameMove* lastMove;
  
  // A char buffer used for reading and writing a GameMove through pipes
  char buf[80];
  
	for(i = 0; i < children; i++) {
		generate_board(&(boards[i]), dimension);
    
		pipe(fd[i][0]);
		/** 
      child read     = fd[i][0][0]
      parent write   = fd[i][0][1]
    **/
    
		pipe(fd[i][1]);
		/**
      parent read    = fd[i][1][0]
      child write    = fd[i][1][1]
    **/
    
    childpid[i] = fork();
    
		if(childpid[i] == -1) {
			perror("fork");
			exit(1);
		}
		if(childpid[i] == 0) {
      srand(getpid());
      for (j = 0; j <=i; j++) {
        // close all parent reads
        close(fd[j][0][1]);
        // close all parent writes
        close(fd[j][1][0]);
      }
      long nbytes;
      while(!boards[i]->finished) {
        // Read in move from parent
        nbytes = read(fd[i][0][0], &buf, sizeof(GameMove));
        if(nbytes <= 0) {
          break;
        }
        // cast move to GameMove*
        lastMove = (GameMove*) buf;
        
        // place parent piece at the position read in
        // Because of the while loops in the parent and child processes, this move
        // can always be considered safe and not NULL
        lastMove = placePieceAtPosition(boards[i], 1, lastMove->row, lastMove->col);
        
        // Check for a win. If there is a win, it returns 1
        // else, child makes a move
        if(!(boards[i]->finished = checkForWin(boards[i], 1))) {
          
          // If child is playing to win, like the parent, use a different function
          if(child_play_to_win) {
            
            // NULL case handles in best position function
            lastMove = placePieceAtBestPosition(boards[i], 2);
          }
          else {
            lastMove = placePieceInColumn(boards[i], 2, rand() % boards[i]->dimension);
          }
          
          // After the move check for a win again.
          boards[i]->finished = checkForWin(boards[i], 2);

          // write move back to parent
          write(fd[i][1][1], lastMove, sizeof(GameMove));

          // If the board is finished (there was a win),
          if (boards[i]->finished) {
            close(fd[i][0][0]); // Child wins, close child read fd
            close(fd[i][1][1]); // close child write fd
            break;
          }
        }
        else {
          write(fd[i][1][1], lastMove, sizeof(GameMove)); // Parent won
          close(fd[i][0][0]); // close child read fd
          close(fd[i][1][1]); // close child write fd
          break;
        }
      }
      dealloc(boards[i]);
			exit(0);
		}
	}
	
  // When this hits children amount, all games are done
  int games_complete = 0, error = 0;
  long nbytes;
  GameMove* tmpMove;
  
  // Make first move to all children
  for (i = 0; i < children; i++) {
    close(fd[i][0][0]);
    close(fd[i][1][1]);
    lastMove = placePieceAtBestPosition(boards[i], 1);
    write(fd[i][0][1], lastMove, sizeof(GameMove));
  }
  while (games_complete != children && !error) {
    for (i = 0; i < children; i++) {
      
      if(!boards[i]->finished) { // Read move from child
        nbytes = read(fd[i][1][0], &buf, sizeof(GameMove));
        if(nbytes < 0) {
          printf("\033[1;32mRead child[%d] error in parent.\033[0m\n\n", childpid[i]);
          error = 1;
          exit(1);
        }
        else if(nbytes == 0) {
          games_complete++;
          break;
        }

        // Cast child move to GameMove*
        tmpMove = (GameMove*) buf;
        if(tmpMove->row == lastMove->row && tmpMove->col == lastMove->col) {
          kill(childpid[i], SIGKILL);
        }

        // place child piece
        placePieceAtPosition(boards[i], 2, lastMove->row, lastMove->col);
        
        // Check for a child win...
        boards[i]->finished = checkForWin(boards[i], 2);
        if (!boards[i]->finished) {
          
          // No win, place piece at best position
          lastMove = placePieceAtBestPosition(boards[i], 1);
          // check for win after the move
          boards[i]->finished = checkForWin(boards[i], 1);
          // Write move back to child
          write(fd[i][0][1], lastMove, sizeof(GameMove));
          
          // If won, close everything and increment
          // the games_complete counter.
          if(boards[i]->finished) {
            close(fd[i][1][0]); // close parent read fd
            close(fd[i][0][1]); // close parent write fd
            printf("\033[1;3%dmParent wins against child[%d]!\033[0m\n", i + 1, childpid[i]);
            games_complete++;
            printBoard(boards[i]);
          }
        } else {
          printf("Parent wins against child[%d]!\n", childpid[i]);
          // write winning move back to child
          write(fd[i][0][1], lastMove, sizeof(GameMove));
          // close parent write fd
          close(fd[i][0][1]);
          // close parent read fd
          close(fd[i][1][0]);
          games_complete++;
          printBoard(boards[i]);
        }
      }
    }
  }
  
  for(i = 0; i < children; i++) {
    waitpid(childpid[i], NULL, 0);
  }
  
	// Cleanup
	for(i = 0; i < children; i++) {
		dealloc(boards[i]);
	}
	free(boards);
  free(lastMove);
	return 0;
}

int rand_lim(int limit) {  
  int divisor = RAND_MAX/(limit+1);
  int retval;
  
  do {
    retval = rand() / divisor;
  } while (retval > limit);
  
  return retval;
}
