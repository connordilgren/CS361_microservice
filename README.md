# CS361_microservice

This microservice has three commands: save, load, and close.

To do any of these commands, the main program must first connect to the microservice using python sockets. To do that, the main program must:
1. Open a python socket with the paremeters socket.AF_INET and socket.SOCKET_STREAM
2. Bind the socket to the host and port that the microservice will connect to
3. Listen for a connection request from the microservice
4. Accept the connection request from the microservice, which returns a connection object


The save command is used to save the game state. To save a game state, the main program must connect to the microservice using python sockets and then:
1. Create a dictionary with keys command, game_state, and file, which have values of save, a dictionary with the game state, and the file to save to, respectively. The dictionary with the game state should have keys player_1_score, player_2_score, and board. The first two keys map to integers that represent the number of games won by each player. The board value is a list of lists, where each inner list is row in the tic-tac-toe board. 
2. Use pickle.dumps() to serialize this dictionary as a byte stream.
3. Use the sendall() method of the connection object to send the byte 
stream to the microservice.


The load command is used to load the game state. To load a game state, the main program must connect to the microservice using python sockets and then:
1. Create a dictionary with keys command and file, which have values of 
load and the file to save to, respectively.
2. Use pickle.dumps() to serialize this dictionary as a byte stream.
3. Use the sendall() method of the connection object to send the byte 
stream to the microservice.
4. Use the recv(1024) method of the connection object to receive the 
game state as a byte stream.
5. Use pickle.loads() to convert the byte stream to a dictionary with the 
game state. 

Here is an example of how the main program will request the microservice to load the game state, where conn is the connection object:

    # load game state back in
    load_params = {"command": "load", "file": "game_1.txt"}
    load_params_b = pickle.dumps(load_params)
    conn.sendall(load_params_b)


The close command is used to close the microservice. To close the microservice, the main program must connect to the microservice using python sockets and then:
1. Create a dictionary with a key-value pair of "command": "close". 
2. Use pickle.dumps() to serialize this dictionary as a byte stream.
3. Use the sendall() method of the connection object to send the byte stream to the microservice.


UML sequence diagram:
![alt text](https://github.com/connordilgren/CS361_microservice/blob/main/UML_sequence_diagram.png?)
