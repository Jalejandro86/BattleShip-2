from random import randint 
import time

print("====WELCOME TO BATTLESHIP  V6.0====")

Board_Size = 5
min_shipSize = 2
max_shipSize = 5
Max_Turns = 5
min_turns = Max_Turns -1
sleep_time = 5
east_west = 1
north_south = 2


def control():
	play_again = str(input("Would you like to play again Y or N?  "))
	#print(play_again)
	if play_again == str ("y") or play_again == str ("Y"):
		ocean()
		
	else:
		print ("Goodbye !!  ")
		time.sleep(sleep_time)
		raise SystemExit
		
def ocean():
	board = []

	for x in range(Board_Size):
		board.append(["O"] * Board_Size)

	def print_board(board_in):
		for row in board:
			print("   ".join(row))

	print_board(board)


	def random_row(board):
		return randint(1, len(board) )

	def random_col(board):
		return randint(1, len(board[0]) )

	anchor_point = random_row(board), random_col(board)	
	
#def fill_ship():
	ship_size = randint(min_shipSize, max_shipSize, )
	heading = randint(east_west, north_south, )
	ship_pos = []
	ship_pos.append(anchor_point)
	dirc = heading
	explng = ship_size - 1
	expand_p = 1
	expand_n = 1
	
	while explng >= 1 and explng < Board_Size + 1:
	
		if dirc == 1:
			if anchor_point[0] + explng <= Board_Size:
				ship_pos.append((anchor_point[0] + expand_p, anchor_point[1]))
				expand_p += 1
				
			else:
				ship_pos.append((anchor_point[0] - expand_n, anchor_point[1]))
				expand_n += 1
						
		elif dirc == 2:
			if anchor_point[1] + explng <= Board_Size:
				ship_pos.append((anchor_point[0] , anchor_point[1] + expand_p))
				expand_p += 1
				
			
			else:
				ship_pos.append((anchor_point[0] , anchor_point[1] - expand_n))
				expand_n += 1
				
		else:
			print("No Heading Found...")
			
		explng -= 1
			
#def play():
	for turn in range(Max_Turns):
		if turn == 0:
			print("You have" , Max_Turns ,  "Chances to Guess where it is...")
			
		g_row = input("Guess Row: ")
		if g_row.isdigit():
			guess_row = int(g_row)
		else:
			print("ERROR 612: Only INT Values Accepted")
			guess_row = 0
				
		g_col = input("Guess Col: ")
		if g_col.isdigit():
			guess_col = int(g_col)
		else:
			print("ERROR 612: Only INT Values Accepted")
			guess_col = 0
		
		
		
		torpedo = guess_row, guess_col
		print ("torpedo away ..." , torpedo)
		
		if torpedo in ship_pos:
			print ("Hit .....")
			board[guess_row -1][guess_col -1] = "H"
			ship_pos.remove(torpedo)
			
		elif (torpedo[0] <= 0 or torpedo[0] > Board_Size) or (torpedo[1] <= 0 or torpedo[1] > Board_Size):
			print("Oops, that's not even in the ocean.")
				
		elif(board[guess_row -1][guess_col -1] == "X"):
			print("You guessed that one already.")
			
		else:
			print("You missed my battleship!")
			board[guess_row -1][guess_col -1] = "X"
				
		if turn < min_turns:
			print("Try again you have   " +  str(Max_Turns - turn -1) + "  turns left")
		
		else:
			print("Sorry you have no turns left")
			time.sleep(sleep_time)
			control()
			
		print_board(board)
		
		if not ship_pos:
			print("Congratulations , You sank my Battleship..!!!")
			time.sleep(sleep_time)
			control()
			

ocean()