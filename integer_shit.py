
import random



def generate_thing(length):
	print("ooofff")
	print(str(10**(length-1)))
	print(10**(length))
	return str(random.randrange(10**max((length-1),0),10**(length)))

if __name__=="__main__":

	for _ in range(1000):
		length = random.randrange(1,10)
		string = generate_thing(length)
		if len(string) != length:
			print("Shit")
			print(string)
			print(str(length))
			print(str(len(string)))
			exit(1)

	print("Done")


