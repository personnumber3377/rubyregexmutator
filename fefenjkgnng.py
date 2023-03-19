


'''


import random


COMMANDS = [
    b"GET",
    b"PUT",
    b"DEL",
    b"AAAAAAAAAAAAAAAAA",
]


def init(seed):
    """
    Called once when AFLFuzz starts up. Used to seed our RNG.

    @type seed: int
    @param seed: A 32-bit random value
    """
    random.seed(seed)


def deinit():
    pass


def fuzz(buf, add_buf, max_size):
    """
    Called per fuzzing iteration.

    @type buf: bytearray
    @param buf: The buffer that should be mutated.

    @type add_buf: bytearray
    @param add_buf: A second buffer that can be used as mutation source.

    @type max_size: int
    @param max_size: Maximum size of the mutated output. The mutation must not
        produce data larger than max_size.

    @rtype: bytearray
    @return: A new bytearray containing the mutated data
    """
    ret = bytearray(100)

    ret[:3] = random.choice(COMMANDS)

    return ret




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

'''

import random
from regex_generator import *

def init(seed):
	random.seed(seed)


def deinit():
	pass

TRIM_CHANCE = 0.5

def fuzz(buf, add_buf, max_size):
    
    # basically the plan is to just get a random place in the string and place a randomly generated regex there:

    # out_string = generate_expr(random.randrange(MIN_LEN, MAX_LEN-1))

    max_size = 110

    max_add_size = max_size-len(buf)
    replace_mode = random.random() < 0.3  # replace mode chance is 30 percent
    


    if max_add_size <= 0:
        replace_mode = True
    if not replace_mode:

        add_string = generate_expr(random.randrange(0, max_add_size))

        random_index = random.randrange(0,len(buf))
        
        add_string = bytes(add_string, encoding="utf-8")

        final_buf = buf[:random_index]+add_string+buf[random_index+1:]
        if len(final_buf) == 0:
            return b"a"
        return final_buf
    else:
        # replace mode:

        random_index = random.randrange(0,len(buf))

        # cut the string at random_index and then take out x chars and replace those.

        max_replace_len = len(buf)- random_index

        replace_length = random.randrange(0,max_replace_len)

        replacement_string = generate_expr(replace_length)


        replacement_string = bytes(replacement_string, encoding="utf-8")
        #print("Add string: "+str(replacement_string))

        # this part is a trim thing

        num_of_trim_bytes = 0
        if random.random() < TRIM_CHANCE:

            #print("len(buf) == "+str(len(buf)))
            #print("random_index :_ "+str(random_index))
            #print("len(replacement_string) == "+str(len(replacement_string)))

            num_of_trim_bytes = random.randrange(len(buf)-random_index-len(replacement_string))


        final_buf = buf[:random_index]+replacement_string+buf[random_index+num_of_trim_bytes+replace_length:]
        if len(final_buf) == 0:
            return b"a"
        return final_buf
    return buf


if __name__=="__main__":


    original_buf = bytes('abcdefg', encoding="utf-8")
    length_thing = len("abcdefg")

    for _ in range(1000):

        string = fuzz(original_buf, None, length_thing)
        print(string)





