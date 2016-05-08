def morse_code():
	print "Enter a sentence to be translated (*** to end)"
	sentence = raw_input()
	sentence = sentence.upper() #makes all letters uppercase so you can test them with the letters in the morse code list

	if sentence == "***":
		print "Program has ended"
		exit()   #quits the program if the user enters stars

	code_info = [['A','.-'], ['B','-...'], ['C', '-.-.'], 
				 ['D', '-..'], ['E', '.'], ['F', '..-.'], 
				 ['G', '--.'], ['H', '....'], ['I', '..'], 
				 ['J', '.---'], ['K', '-.-'], ['L', '.-..'], 
				 ['M', '--'], ['N', '-.'], ['O', '---'], 
				 ['P', '.--.'], ['Q', '--.-'], ['R', '.-.'], 
				 ['S', '...'], ['T', '-'], ['U', '..-'], 
				 ['V', '...-'], ['W', '.--'], ['X', '-..-'], 
				 ['Y', '-.--'], ['Z', '--..']]

	sentence_letters = []
	for i in sentence:   #adds each letter in the sentence to a list
		sentence_letters.append(i)

	code = [] #holds the code you want to print out
	for letter in sentence_letters:
		for j in code_info:
			if letter == j[0]: 
				code.append(j[1] +" ") #adds the morse code and a space for each letter to the code list


	final_code = "".join(code) #turns the code into a string
	return final_code

	
print morse_code()