import socket

host = '127.0.0.1' # Standard loopback interface address
port = 12345 # Define the port on which you want to connect

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server on local computer
client.connect((host, port))


# Get user keyboard input
Input = input('Input the Number: ')

# message sent to the server
#client.send(Input)
client.send(str(Input).encode('utf8'))


client.close()
print("All are Okay - Connection Terminated !")


