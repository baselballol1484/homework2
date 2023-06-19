import socket
import threading

# Define quiz questions
math_questions = {
"7*8": "56",
"25/5": "5",
"9+6-2": "13",
"4^2": "16",
"10*2+5": "25",
"34+56": "42",
"100-25*3": "25",
"1/4+1/2": "0.75",
"2^3+4^2": "20",
"2*8-12/3": "12",
}

# Define function to handle client
def handle_client(client_socket,client_address):
    score = 0
    # Send quiz questions to the client
    for question, answer in math_questions.items():
        client_socket.sendall(f"What is {question}?\n".encode())

        # Wait for the client's answer and check if it's correct
        client_answer = client_socket.recv(1024).decode()
        if client_answer == answer:
            score += 1
    print("Result of",client_address,"is",score)
    # Close the client connection
    client_socket.send("end".encode())
    msg="Your score is "+str(score)
    client_socket.send(msg.encode())
    client_socket.close()

# Create server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 1234))
server_socket.listen()

while True:
    # Wait for a new client connection
    client_socket, client_address = server_socket.accept()
    print(f"New client connected from {client_address}")

    # Create a new thread to handle the client
    client_thread = threading.Thread(target=handle_client, args=(client_socket,client_address))
    client_thread.start()