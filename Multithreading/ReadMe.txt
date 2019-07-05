Project Presented: 
Pratik Parekh 801076521
Sakshat Surve 801080533


Computer Communication Networks:

HTTP Client and Server:
This project is built using Python Version 3.6.

This Project has basically two parts of codes:
i) client.py
ii)server.py 

User needs to to create to folders namely Server and Client.
server.py will be stored in Server folder.
client.py will be stored in Client folder
To run the code, the user need to go in the server folder and run server.py.
After running server.py, server will be waiting for connection and then user needs to run client.py
User needs to pass port number as command line argument while running server.py.
User needs to pass command line arguments while running client.py
These arguments are servername, port number, GET/PUT command, file(that needs to be uploaded or downloaded)

Example for running server.py with port 8080
python server.py 8080

Example for running client.py 
python client.py localhost 8080 GET index.html

For testing multiple client request , user needs to run multiple times client.py using command prompt.

When user will give GET command, the mentioned file will be fetched fro server and will be brought to client(Client folder)
If the file doesn't exist in server, server will give error 404.

when user will give PUT command, the mentioned file will be uploaded to server(Server folder) from client.
If that file already exists in server, server will reply with ok 200 message, if file is not present server will reply with 201.
