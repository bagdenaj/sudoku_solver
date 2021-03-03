import numpy as np
import pandas as pd

sudoku = 	[[0,0,0,0,0,0,0,0,0],
			[0,0,0,9,8,0,4,0,0],
			[0,0,4,0,0,5,0,0,0],
			[4,0,0,3,0,0,0,0,2],
			[3,0,0,5,0,0,0,0,1],
			[0,9,0,1,7,0,6,0,8],
			[0,0,0,0,0,1,0,2,0],
			[0,0,0,0,0,9,0,7,0],
			[1,6,9,0,0,0,0,0,0]]

pf = pd. DataFrame(sudoku)

def possible(y,x,n):
	global sudoku
	for i in range(0,9):
		if sudoku[y][i] == n:
			return False
	for i in range(0,9):
		if sudoku[i][x] == n:
			return False
	y0 =(y//3)*3
	x0 =(x//3)*3
	for i in range(0,3):
		for j in range(0,3):
			if sudoku[y0+i][x0+j] == n:
				return False
	return True

def check_if_full():
	global sudoku
	zero_counter= 0
	for i in range(0,9):
		zero_counter = zero_counter + sudoku[i].count(0)
	if zero_counter == 0:
		return True
	else:
		return False

def fill_sudoku():
	global sudoku
	for x in range(0,9):
		for y in range(0,9):
			if sudoku[y][x] == 0:
				for n in range(1,10):
					if possible(y,x,n):
						sudoku[y][x] = n
						fill_sudoku()
						sudoku[y][x] = 0
				return
	print(np.matrix(sudoku))
	if input('Want another solution? [Yes] [No]') == 'No':
		exit()

print(fill_sudoku())
