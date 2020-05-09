# Game-Protocol
Introduction.
The program defines an application layer client server protocol providing online game playing on windows operating system. 
The application is version 1.0 and hence is nowhere close to a finished protocol implementation. 
The protocol was implemented using Python Sockets.
pygame module was used to create a sample game and will be required to run the protocol successfully.

What is functional.

The client is able to connect to the server and exchange data.
2 clients are able to connect to the server at a time and hence 1 instance of a game (with 2 client connections) can be run.
The server can be run on any machine and the clients can be run to find the server on the same local network.

What is yet to be implemented.

The PDU for the message is not implemented yet.
Messages are not defined explicitly.
States are not defined explicitly.
No encryption over the data.
Global accessibility of the server to the client.
User authentication.

How to start application.
After extraction, run <cmd> through the address bar on top of project folder window.
Input the following in the cmd to start the server instance… ..\project>python server.py 
Input the following in a new command window opened using step  ..\project>python client.py
Open another instance of a client using the same command as 3
2 player game is now functional.
