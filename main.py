import base64

def encode_message(message, key):
    """
    Encode the message using a 6-digit key.
    :param message: str - The message to encode.
    :param key: str - A 6-digit key.
    :return: str - Encoded message.
    """
    if len(key) != 6 or not key.isdigit():
        raise ValueError("Key must be a 6-digit number.")
    
    # XOR encryption
    encoded_chars = [
        chr(ord(char) ^ int(key[i % len(key)])) for i, char in enumerate(message)
    ]
    encoded_message = ''.join(encoded_chars)
    
    # Encode result to base64 for safe transmission
    return base64.urlsafe_b64encode(encoded_message.encode()).decode()

def decode_message(encoded_message, key):
    """
    Decode the encoded message using a 6-digit key.
    :param encoded_message: str - The encoded message.
    :param key: str - A 6-digit key.
    :return: str - Decoded message.
    """
    if len(key) != 6 or not key.isdigit():
        raise ValueError("Key must be a 6-digit number.")
    
    # Decode base64 input
    try:
        decoded_base64 = base64.urlsafe_b64decode(encoded_message).decode()
    except Exception as e:
        raise ValueError("Invalid encoded message format.") from e
    
    # XOR decryption
    decoded_chars = [
        chr(ord(char) ^ int(key[i % len(key)])) for i, char in enumerate(decoded_base64)
    ]
    return ''.join(decoded_chars)

if __name__ == "__main__":
    print("Message Encryption/Decryption Tool")
    action = input("Enter 'E' to encode or 'D' to decode: ").strip().upper()

    if action == 'E':
        message = input("Enter the message to encode: ").strip()
        key = input("Enter a 6-digit key: ").strip()
        try:
            encoded = encode_message(message, key)
            print(f"Encoded Message: {encoded}")
        except ValueError as e:
            print(f"Error: {e}")
    elif action == 'D':
        encoded_message = input("Enter the encoded message: ").strip()
        key = input("Enter the 6-digit key: ").strip()
        try:
            decoded = decode_message(encoded_message, key)
            print(f"Decoded Message: {decoded}")
        except ValueError as e:
            print(f"Error: {e}")
    else:
        print("Invalid action. Please enter 'E' or 'D'.")
