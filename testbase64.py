import base64

str = "dW5pdHk="

print(base64.b64decode(str).decode('utf-8'))