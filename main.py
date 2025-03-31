from network import network

infile = open("network.txt", "r")
network = infile.readlines()
infile.close()

print(network)