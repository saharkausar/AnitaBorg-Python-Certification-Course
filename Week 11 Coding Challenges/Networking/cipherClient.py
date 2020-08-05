#   SCRIPT: cipherClient.py
#   AUTHOR: Sahar Kausar
#   CONTACT: saharkausar@gmail.com
#
#   Anita Borg - Python Certification Course
#
#   DESCRIPTION: A Python program that decodes hidden messages, specifically - Caesar Ciphers utilizing the standard English alphabet.
#                Our Caesar Cipher will be based on shifting all the letters to the right by three positions.
#                So the encryption translates as follows:
#                Plain English Alphabet: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
#                Cipher: X Y Z A B C D E F G H I J K L M N O P Q R S T U V W
#                In our code the word “CAT” becomes “ZXQ” and “HELLO” becomes “EBIIL”.
#
#   NOTE: This file is the client file (cipherClient.py) that should be used in tandem with the server file (cipherServer.py)

"""
Sample Scenario 1:
        	Client sends: Jlkqv Mvqelk
        	Server sends back:
                    	Received: Jlkqv Mvqelk
      	Translation: monty python

Sample Scenario 2:
        	Client sends:
        	        	QEXKH VLR XKFQXYLOD
        	Server sends back:
                    	Received: QEXKH VLR XKFQXYLOD
      	Translation: thank you anitaborg

      	Received: f zlria dl clo pljb QXZLP
      	Translation: I COULD GO FOR SOME TACOS
"""

#Imports the socket module
import socket

client_socket = socket.socket()

#Binds the socket object to local host 4000 as a socket server
client_socket.connect(("localhost", 4000))

#Input taken from the user to store in a variable 'init_msg'
init_msg = input("Please enter a string of text to decode: ")

#Sends the 'init_msg' string to the server to begin the caesar cipher shift
client_socket.send(init_msg.encode())

#Output from the server that is received as a response (input into the client socket)
new_msg = client_socket.recv(1024)

#Prints out the decrypted message
print(new_msg.decode())

#Closes the connection
client_socket.close()
