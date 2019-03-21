# BRR
# MSAW

import random
	
	
def start_game():
	print("""
					---------------------------------------------------
	
						Welcome to the number guessing game
	
					---------------------------------------------------
	""")
	

	solution=random.randint(1,10)
		
	attempts = []
	def attempt(guess):
		attempts.append(guess)
		
	
	while True:
		
		prompt=input("Pick a number between 1 and 10  ")
				
		try:
			
			prompt=int(prompt)
			
			if prompt>10 or prompt<1:
				
				print("""	
								!!!!!!!!!!!!!!!!!!!!!!!!!
									NOT TEXT
							!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
								   NOT NUMBERS HIGHER THAN 10
								!!!!!!!!!!!!!!!!!!!!!!!!!!!		
								   NOT NUMBERS LOWER THAN 1
								!!!!!!!!!!!!!!!!!!!!!!!!!!!
								
							Plese only enter numeric value between 1 and 10
							
								 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
							""")
				continue
		
			elif prompt < solution:
				attempt(prompt)
				print("It is higher")
			
			elif prompt > solution:
				attempt(prompt)
				print("It is lower")
			
			elif prompt==solution:
				attempt(prompt)
				print("""
			~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
			
			You've got it
			
			~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
			""")
				print("""
			^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
			
			It took you {} attempts to guess the correct number
			
			^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^""".format(len(attempts)))
			
				break
		except ValueError:
			print("""	
								!!!!!!!!!!!!!!!!!!!!!!!!!
									NOT TEXT
							!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
								   NOT NUMBERS HIGHER THAN 10
								!!!!!!!!!!!!!!!!!!!!!!!!!!!		
								   NOT NUMBERS LOWER THAN 1
								!!!!!!!!!!!!!!!!!!!!!!!!!!!
								
							Plese only enter numeric value between 1 and 10
							
								 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
							""")
			pass
		
				
			
def play_again():
	while True:
		
		play_again=input("""


Would you like to play again? [y]es/[no]   """)
		play_again=play_again.lower()
		if play_again == 'y':
			start_game()
			
		elif play_again == 'n':
			print("""
		==========================================
		
				THE GAME IS OVER THEN
				
		==========================================
		""")
			break
		else:
			print("                					Excuse me?            ")
			print("				   Please say yes or no, pressing 'y' or 'n' respectively          ")
	
  

start_game()

play_again()
