#! creates a server
# server methods:
# bind() -- binds to a specific ip and port so that it can listen to 
	# incoming requests on that ip and port.
# listen() -- puts the server into listen mode to listen to incoming connections.
#  accept() -- initiates a connection with the client 
#  close() -- closes the conneciton with the client.


import socket

# create a socket object from the socket function

s = socket.socket()

print("socket successfully created")

# next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network

# notice the double brackets?! cause the function takes one arg

port = 12345
s.bind(('', port))

print('socket binded to %s' %(port))

# put the socket into listening mode
# 5 means that 5 connections are kept waiting if the server
# is busy and if a 6th socket trys to connect then the 
# connection is refused

s.listen(5)
print('socket is listening')

# a forever loop until we interrupt it or an error occurs

while True:
	# Establish connection with client

	c, addr = s.accept()

	print('got connection from ', addr)

	# send a thank you message to the client.

	c.send('Thank you for connecting \n')

	# close the connection with the client

	c.close()

