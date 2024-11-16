
# Text Encryption and Decryption using LSTM Model

### Script Description

This script demonstrates how to encrypt and decrypt text using an optimized LSTM model. It follows these steps:

1. **Generate Random Plaintext Data**: Creates a dataset of random plaintext samples.
2. **Encrypt Text with XOR Cipher**: Encrypts each plaintext sample using an XOR cipher with a fixed key.
3. **Build LSTM Model**: Constructs a sequential LSTM model for encryption and decryption.
4. **Train the Model**: Trains the LSTM model on encrypted ciphertext to predict original plaintext.
5. **Test the Model**: Encrypts a new text sample, predicts its decryption, and compares it to the original.

The results are questionable but can be used as a foundation for better results in the future. The project isn't updated often.
## Dependencies
Activate Your Virtual Environment before running the scripts

Windows
```bash
  install_dependencies.bat
```
Unix-like systems
```bash
  install_dependencies.bat
  ```
## Running Tests

To run tests, run the following command

```bash
  python run.py
```

## Input Example

When prompted, enter a plaintext of length 8, where each character is an integer between 0 and 255 separated by spaces.

Example
```bash
  123 456 789 101 112 131 141 151
```




