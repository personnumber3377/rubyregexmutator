
import string
import random


'''
.	Match any character
|	An OR operator, match either the sequence before or after this
( )	Start and end a subsequence (grouping)
[ ]	Start and end a character class
{ }	Match intervals:
{a,b}: Match at least a characters, at most b.
{a,}: Match at least a characters and more.
{a}: Match exactly a characters.
\	Escape character
^	Match the beginning of a line. When used at the beginning of a character class, negates it.
$	Match the end of a line
+	Match one or more times ({1,})
+?	Match one or more times ({1,}) (Non greedy: match the smallest pattern)
*	Matches zero ore more ({0,})
*?	Matches zero ore more ({0,}) (Non greedy: match the smallest pattern)
?	Match zero or one time ({0,1})

[0-9]	\d	Decimal digit character
[^0-9]	\D	Not a decimal digit character
[\s\t\r\n\f]	\s	Whitespace character
[^\s\t\r\n\f]	\S	Not a whitespace character
[A-Za-z0-9_]	\w	Word character (alpha, numeric, and underscore)
[^A-Za-z0-9_]	\W	Not a word character
[:alnum:]		Alpha numeric ([A-Za-z0-9])
[:alpha:]		Uppercase and lowercase letters ([A-Za-z])
[:blank:]		Blank or tab character
[:space:]		Whitespace characters
[:digit:]		Decimal digit characters
[:lower:]		Lowercase letters ([a-z])
[:upper:]		Uppercase characters
[:print:]		Any printable character, including space
[:graph:]		Printable characters excluding space
[:punct:]		Punctuation characters: any printable character excluding aplhanumeric or space
[:cntrl]		Chontrol characters (0x00 to 0x1F and 0x7F)
[:xdigit:]		Hexadecimal digits ([0-9a-fA-F])







===============NEW LOOP===============
Subexpr
Expre tuefweweew
Passed 5 as length.
Subexpr
Lengt oof shit : 7
Subexpr
Subexpr
Original length thing : 2
Traceback (most recent call last):
  File "regex_generator.py", line 314, in <module>
    string = generate_expr(10)
  File "regex_generator.py", line 302, in generate_expr
    return simple_expr(length)
  File "regex_generator.py", line 274, in simple_expr
    random_length = random.randrange(2,length+1)
  File "/usr/lib/python3.8/random.py", line 226, in randrange
    raise ValueError("empty range for randrange() (%d, %d, %d)" % (istart, istop, width))
ValueError: empty range for randrange() (2, 1, -1)











'''

alphabet = list(string.ascii_letters)

START_SPECIAL_CHARS = [".", "*", "+", "?", "\\"]  #     \     is a special character which escapes the next character, so we technically can do \[ and it will match the "[" character.

special_chars_no_slash = [".", "*", "+", "?"]

chars_no_slash = special_chars_no_slash + alphabet



start_chars = START_SPECIAL_CHARS + alphabet


SPECIAL_CHAR_CHANCE = 0.95
SUBEXPR_CHANCE = 0.3

def pick_start():

	# pick any possible start character. We can not pick for example "|" as a start character because we will get expressions like [|aaa] which is not valid.

	if random.random() < SPECIAL_CHAR_CHANCE:
		return random.choice(START_SPECIAL_CHARS)
	else:
		return random.choice(alphabet)



def pick_len_one():

	# pick anything from the special characters and alphabet except "\" , because it screws up stuff afterwards .

	if random.random() < SPECIAL_CHAR_CHANCE:
		return random.choice(chars_no_slash) # special char
	else:
		return random.choice(alphabet)



def curly_brace_expr(length):
	expr_type = None

	original_length = length

	if length < 2:
		print("Invalid length for curly_brace_expr: "+str(length))
		exit(1)


	if length == 2:
		length = 0
		return "{}"

	if length == 3:

		# can only do "{1}" or "{2}" etc
		expr_type = 1
	
	elif length == 4:

		# can only do "{1,}" or "{2,}" .
		expr_type = 2
	else:
		# generate random expr_type
		
		expr_type = random.randrange(1,4)
		print("expr_type : "+str(expr_type))

	print("Passed "+str(length)+" as length.")


	return_string = "{"
	
	length -= 1 # {


	print("Length before if expressions: "+str(length))

	if expr_type == 1: # {a}
		length -= 1
		#expression = "{}".format(random.randrange(10**length))
		expression = "{"+str(random.randrange(10**max((length-1),0),10**(length)))+"}"
	
	elif expr_type == 2: # {a,}


		print("Length shitooooooofffff: "+str(length))

		length -= 2


		print("Length shitooooooofffff44444444444: "+str(length))
		#expression = "{}".format(random.randrange(10**length))
		expression = "{"+str(random.randrange(10**max((length-1),0),10**(length)))+",}"





	elif expr_type == 3: # {a,b}

		print("length: "+str(length))

		length -= 2
		#integer1 = random.randrange(min(10**(length-1),0),10**(length)) # length-1 , because we also need the other number to be atleast one char in length
		integer1 = random.randrange(10**max((length-2),0),10**(length-1))

		length -= len(str(integer1))

		print("another length: "+str(length))

		#integer2 = random.randrange(min(10**(length-1),0),10**(length))

		integer2 = random.randrange(10**max((length-1),0),10**(length))


		length -= len(str(integer2))

		expression = "{"+str(integer1)+","+str(integer2)+"}"

	else:
		print("Invalid epression type: "+str(expr_type))
		exit(1)

	if len(expression) != original_length:
		print("Generated an invalid curly brace thing: "+str(expression))
		print("len(expression) == "+str(len(expression)))
		print("original_length: "+str(original_length))
		exit(1)

	return expression

	
	# now try to generate expr

	


def simple_expr(length, poopoo=False):
	

	if length < 0:
		# invalid length
		print("Invalid length: "+str(length))
		exit(1)

	if length == 0:
		return ""

	if length == 1:
		length -= 1
		return pick_len_one()
	
	string = pick_start()
	length -= 1 # length of start char

	if string == "\\": # handle escape character

		# if the character picked was the escape character then we need to add atleast one character before the next subexpression, such that we do not mess up the later stages.

		if length == 0:
			print("Error thing. ")

		string += random.choice(alphabet)

		length -= 1
	print("Length before while loop: "+str(length))

	while length > 0:
		
		if poopoo:
			print("Current length in loop: "+str(length))

		if len(string) != 10 - length and poopoo:
			print("ewwweeeeeeeeeee")
			print(string)
			print("Length : "+str(length))
			exit(1)

		

		if random.random() > 1: # not a subexpr

			if random.random() < SPECIAL_CHAR_CHANCE:
				#print(special_chars_no_slash)
				#original_length = len(string)
				
				string += random.choice(special_chars_no_slash)
				#if len(string) - original_length != 1:
				#	print("bullshit")
				#	exit(1)

				length -= 1
				continue
			else:
				# generate normal character
				#print("alphabet : "+str(alphabet))

				#original_length = len(string)

				string += random.choice(alphabet)

				#if len(string) - original_length != 1:
				#	print("bullshit")
				#	exit(1)

				#length += 1
				length -= 1
				continue
		else:
			if poopoo:
				print("Subexpr")
			if length < 2:
				print("gregregrgr")
				print(length)
				# can not create subexpression when length is less than two (the "(" and ")" characters take up the two characters.) so just create normal chars

				if length == 0:
					continue
				else:
					string += random.choice(alphabet) # append a regular char
					length -= 1
					continue
			else:
				# generate subexpression


				if length < 2:
					print("poopoo")
					exit(1)
				#subexpr_type = random.choice(["bracket", "curly_brace", "normal_brace"])
				subexpr_type = random.choice(["bracket"])


				if subexpr_type == "bracket": # normal subexpression

					#print("Lengt oof shit : "+str(length))
					if length < 2:
						print("Error stuff.")
						exit(1)
					


					#random_length = random.randrange(2,length+1)
					shit_len = len(string)

					
					if poopoo:
						print("111111111111111111111111111111111111111111111111111111111111111111111111")
						print("Len poopoo: "+str(length))
						print("string : "+str(string))
						print("length : "+str(length))
					
					
					if poopoo:
						print("Calling simple_expr with length: "+str(length))
						print("String previously: "+str(string))
						print("length previously : "+str(length))


					print("String before: "+str(string))
					print("Length before: "+str(length))
					old_len = len(string)
					#string += "["
					#string += simple_expr(random_length)
					#string += simple_expr(length)
					#string += "]"
					length -= 2
					print("Calling simple_expr with length: "+str(length))
					new_string = "["+str(simple_expr(length))+"]"
					string += new_string
					length -= (len(new_string)-2)


					print("String after: "+str(string))
					print("Length after:"+str(length))

					if poopoo:
						print("111111111111111111111111111111111111111111111111111111111111111111111111")
						print("After shit: ")
						print("Len poopoo: "+str(length))
						print("string : "+str(string))
						print("length : "+str(length))


					print("Length after: "+str(length))

					#length -= (len(string) - shit_len)
					if poopoo:

						if len(string) - shit_len != len(new_string):
							
							print("feroifjjnrlkgnrkljergre")
							print("string: "+str(string))
							print("shit_len: "+str(shit_len))
							print("length: "+str(length))



							exit(1)

					#length -= random_length
					continue
				elif subexpr_type == "curly_brace":
					
					if length < 3: # if length is less than three then can not really generate a valid curly brace expression .

						for _ in range(length):
							string += random.choice(alphabet)
							length -= 1
						continue

					random_length = random.randrange(2,length+1)

					shit_len = len(string)

					string += curly_brace_expr(random_length)
					

					if len(string) - shit_len != random_length:
						print("errreeeeee")
						print("feroifjjnrlkgnrkljergre")
						exit(1)

					length -= random_length
					continue

				elif subexpr_type == "normal_brace":
					
					print("Original length thing : "+str(length))
					if length < 2:
						print("Error stuff.")
						exit(1)



					


					# this hack is here, because random.randrange(2,2) crashes
					if length == 1:
						random_length = 2
					else:
						print("Length  ffffffffffffffff: "+str(length))
						random_length = random.randrange(2,length+1)
					#length -= 2
					string += "("
					string += simple_expr(random_length-2)
					string += ")"
					length -= random_length

					#length -= random_length
					continue
				else:
					print("Reached the end of the shit.")
					exit(1)

				print("Error thing!")
				exit(1)



			# generate subexpr

	#print("Final length: "+str(length))

	if length < 0:
		print("Fuck")
		exit(1)

	return string






def generate_expr(length):


	return simple_expr(length, poopoo=True)



HOW_MANY_TESTS = 10000

TEST_LEN = 10

if __name__=="__main__":

	for _ in range(HOW_MANY_TESTS):
		print("===============NEW LOOP===============")
		string = generate_expr(10)
		print("======================================")
		if len(string) != 10:
			print("Error. Something went wrong.")
			print("Generated string: "+str(string))
			print("Length: "+str(len(string)))
			exit(1)

	print("[+] Success!")
	exit(0)



	#print(generate_expr(10))



