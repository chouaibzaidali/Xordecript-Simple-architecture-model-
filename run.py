import numpy as np
import tensorflow as tf

# Parameters
text_length = 8     # Length of each text (in characters)
key = 42            # XOR key for encryption

def encrypt_xor(plaintext, key):
    return np.bitwise_xor(plaintext, key)

if __name__ == "__main__":
    # Load the pre-trained model
    model = tf.keras.models.load_model('trained_model.h5')

    # Get user input (plaintext)
    user_input = input("Enter a plaintext of length {} (characters 0-255 separated by spaces): ".format(text_length))
    user_input = list(map(int, user_input.split()))
    
    if len(user_input) != text_length:
        print(f"Error: Input must be exactly {text_length} characters long.")
        exit(1)
    
    # Validate and normalize the input
    test_plaintext = []
    for char in user_input:
        if 0 <= char <= 255:
            test_plaintext.append(char)
        else:
            print(f"Error: Invalid character {char}. Must be between 0 and 255.")
            exit(1)
    
    test_plaintext = np.array([test_plaintext], dtype=np.uint8)

    # Encrypt the plaintext
    test_ciphertext = encrypt_xor(test_plaintext, key) / 255.0
    test_ciphertext = test_ciphertext.reshape((1, text_length, 1))

    # Predict the decrypted text
    predicted_plaintext = model.predict(test_ciphertext)

    # Convert predictions to integer format for comparison
    predicted_plaintext = np.round(predicted_plaintext * 255).astype(int)

    print("Original Plaintext:", test_plaintext[0])
    print("Encrypted Ciphertext:", (test_ciphertext.reshape((text_length,)) * 255).astype(int))
    print("Predicted Plaintext:", predicted_plaintext[0])