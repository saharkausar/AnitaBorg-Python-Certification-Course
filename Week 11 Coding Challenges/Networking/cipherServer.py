#   SCRIPT: cipherServer.py
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
#   NOTE: This file is the server file (cipherServer.py) that should be used in tandem with the client file (cipherClient.py)

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

host = 'localhost'
port = 4000

#Builds and initializes the socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Binds the socket object to local host 4000 as a socket server
server_socket.bind((host, port))

print("Server listening on port: ", port)

#Configures how many clients that the server can listen to actively
server_socket.listen(1)

#Accepts a new connection to the server
conn, addr = server_socket.accept()

#Receives the data stream with a data packet of 1024 bytes or less and decodes the data from bytes back into a string
rcv_msg = conn.recv(1024).decode()

#Prints out the message received from the client
print("Received:", rcv_msg)

#Function that decrypts the caesar cipher by accepting two parameters (3 as the key for our desired shift in the caesar cipher, and the message to decrypt)
def decrypt(unit, message):
    #Sets the characters in the string to uppercase
    message = message.upper()

    #Sets a key to include the letters of the alphabet
    key = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    #Initializes an empty string that we can store our decrypted characters into (will be returned as the result)
    result = ""

    #Parses through each letter in our message
    for letter in message:
        #Checks if each letter character is a letter of the alphabet
        if letter in key:
            #If it is, then we find the corresponding ciphertext letter in the alphabet (Shifts the character by our desired unit = 3)
            letter_index = (key.find(letter) + unit) % len(key)
            result = result + key[letter_index]

        else:
            #If not, we simply return the value
            result = result + letter

    #Returns the result
    return result

#Prints out the translated message by passing in the message received from the client into our decrypt method
print("Translation:", decrypt(3, rcv_msg))

#Closes the connection
conn.close()
