import string

def vigenere(message, key, encrypt=True):
    """
    Encrypts or decrypts a message using the Vigenère cipher.
    
    Parameters:
        message (str): The plaintext or ciphertext.
        key (str): The encryption/decryption key.
        encrypt (bool): True to encrypt, False to decrypt.
    
    Returns:
        str: The encrypted or decrypted message.
    """
    alphabet = string.ascii_lowercase
    key = key.lower()
    key_index = 0
    result = []

    for char in message:
        if char.lower() in alphabet:
            shift = alphabet.index(key[key_index % len(key)])
            if not encrypt:
                shift = -shift
            new_index = (alphabet.index(char.lower()) + shift) % len(alphabet)
            new_char = alphabet[new_index]
            # Preserve original case
            result.append(new_char.upper() if char.isupper() else new_char)
            key_index += 1
        else:
            # Keep non-alphabet characters as they are
            result.append(char)
    
    return ''.join(result)

def encrypt_message():
    message = input("🔑 Enter the message to encrypt: ")
    key = input("🔐 Enter the encryption key: ")
    encrypted = vigenere(message, key, encrypt=True)
    print(f"\n✅ Encrypted text: {encrypted}")

def decrypt_message():
    message = input("🔑 Enter the message to decrypt: ")
    key = input("🔐 Enter the decryption key: ")
    decrypted = vigenere(message, key, encrypt=False)
    print(f"\n✅ Decrypted text: {decrypted}")

def main():
    print("=== 🔐 Vigenère Cipher Tool ===")
    print("1️⃣ Encrypt a message")
    print("2️⃣ Decrypt a message")
    print("0️⃣ Exit")

    while True:
        choice = input("\nChoose an option (1/2/0): ")
        if choice == '1':
            encrypt_message()
        elif choice == '2':
            decrypt_message()
        elif choice == '0':
            print("👋 Exiting the program. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice! Please enter 1, 2, or 0.")

if __name__ == "__main__":
    main()
