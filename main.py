

infile = open("input.txt", "r")
contents = infile.readlines()
infile.close()

contents = [line.strip() for line in contents]


