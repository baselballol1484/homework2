import socket
# Server address and port
address = ('localhost', 1234)
# Create a client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to the server
client_socket.connect(address)
# Receive quiz questions and send answers
while True:
    # Receive the question
    question = client_socket.recv(1024).decode()
    # Print the question
    print(question)
    if question == "end":
        break
    # Get the answer from the user
    client_answer = input("Answer: ")
    # Send the answer to the server
    client_socket.sendall(client_answer.encode())

# Receive the result
result = client_socket.recv(1024).decode()
print("Your result: ", result)
# Close the client connection
client_socket.close()