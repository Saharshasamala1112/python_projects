🔐 Vigenère Cipher – Python Encryption & Decryption
This project implements the Vigenère cipher, a classical cryptographic algorithm used for text encryption and decryption. It allows users to securely encrypt and decrypt messages using a keyword-based shifting technique.

🚀 Features
✅ Encrypt and decrypt text messages

✅ Preserves uppercase and lowercase letters

✅ Keeps spaces and punctuation unchanged

✅ Interactive CLI with menu options

✅ Beginner-friendly, modular Python code

📂 Project Structure
bash
Copy
Edit
python_projects/
│── vigenere_cipher/
│   ├── main.py       # Main encryption/decryption script
│   └── README.md     # Project documentation
🛠️ Usage
Run the program:

bash
Copy
Edit
python main.py
💻 Example Output:
pgsql
Copy
Edit
=== 🔐 Vigenère Cipher Tool ===
1️⃣ Encrypt a message
2️⃣ Decrypt a message
0️⃣ Exit

Choose an option (1/2/0): 1
🔑 Enter the message to encrypt: Programming is Fun!
🔐 Enter the encryption key: Python

✅ Encrypted text: Evdtymyyywv wg Jhx!
🖼️ Preview Screenshot

🧠 How It Works
The Vigenère cipher shifts each letter of the plaintext
based on the corresponding letter in the key.

Non-alphabetic characters are not modified.

Encryption and decryption use the same function
with positive or negative shifts.

🤝 Contributing
Pull requests and feature suggestions are welcome!
Possible future improvements:

🔑 Add file-based encryption/decryption

🖼️ GUI version with Tkinter

📦 Packaging as a Python module

📜 License
This project is licensed under the MIT License.
