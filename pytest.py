import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models

# Parameters
num_samples = 100000  # Number of samples for training
text_length = 8     # Length of each text (in characters)
key = 42            # XOR key for encryption
epochs = 100        # Increased epochs for more thorough training

# Step 1: Generate random plaintext data
def generate_plaintext_samples(num_samples, text_length):
    return np.random.randint(0, 256, (num_samples, text_length))

# Step 2: Encrypt the plaintext using XOR cipher
def encrypt_xor(plaintext, key):
    return np.bitwise_xor(plaintext, key)

# Generate dataset
plaintext_samples = generate_plaintext_samples(num_samples, text_length)
ciphertext_samples = encrypt_xor(plaintext_samples, key)

# Normalize data to range [0, 1] for neural network input
plaintext_samples = plaintext_samples / 255.0
ciphertext_samples = ciphertext_samples / 255.0

# Step 3: Build the optimized LSTM model
model = models.Sequential([
    layers.Input(shape=(text_length, 1)),
    layers.LSTM(256, activation='relu', return_sequences=True),
    layers.Dropout(0.2),
    layers.LSTM(128, activation='relu', return_sequences=True),
    layers.Dropout(0.2),
    layers.Dense(1, activation='sigmoid')  # Output single value per position in sequence
])

# Compile with mean squared error
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])

# Reshape data for LSTM input
ciphertext_samples = ciphertext_samples.reshape((num_samples, text_length, 1))
plaintext_samples = plaintext_samples.reshape((num_samples, text_length, 1))

# Step 4: Train the model
history = model.fit(ciphertext_samples, plaintext_samples, epochs=epochs, batch_size=32, validation_split=0.2)
# Save the model
model.save('trained_model.h5')
# Step 5: Test the model
# Generate a new sample to test the decryption
test_plaintext = generate_plaintext_samples(1, text_length)
test_ciphertext = encrypt_xor(test_plaintext, key) / 255.0  # Normalize for input
test_ciphertext = test_ciphertext.reshape((1, text_length, 1))

# Predict the decrypted text
predicted_plaintext = model.predict(test_ciphertext)

# Convert predictions to integer format for comparison
predicted_plaintext = np.round(predicted_plaintext * 255).astype(int)
print("Original Plaintext:", test_plaintext)
print("Encrypted Ciphertext:", test_ciphertext.reshape((text_length,)) * 255)  # Denormalize to original scale
print("Predicted Plaintext:", predicted_plaintext.reshape((text_length,)))
