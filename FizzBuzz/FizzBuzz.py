import sys
def main(argv):
	x=int(argv)
	for i in range(1,x+1):
		output=""
		if (i%3==0):output+="Fizz"
		if (i%5==0):output+="Bizz"
		if (output == ""): output=str(i)
		print(output)
if __name__ == "__main__":
	main(sys.argv[1])