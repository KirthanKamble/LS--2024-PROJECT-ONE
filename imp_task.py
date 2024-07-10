import base64

# This function performs an important task
def perform_important_task():
    encoded_message = "eW91IGdheSBicm8="
    decoded_message = base64.b64decode(encoded_message).decode('utf-8')
    print(decoded_message)