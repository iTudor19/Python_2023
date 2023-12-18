import hashlib

hash_initial = None
hash_final = None

def encrypt_decrypt(data, password, mode):
    lines = data.split("\n")
    result = ""
    password_length = len(password)

    for line in lines:
        for i in range(len(line)):
            char = line[i]
            password_char = password[i % password_length]

            if mode == "encrypt":
                encrypted_char = ord(char) + ord(password_char)
                if encrypted_char > 255:
                    encrypted_char &= 0xFF
                result += chr(encrypted_char)
            elif mode == "decrypt":
                decrypted_char = ord(char) - ord(password_char)
                if decrypted_char < 0:
                    decrypted_char += 256
                result += chr(decrypted_char)
        result += "\n"

            

    if mode == "encrypt":
        hashed_data = hashlib.sha256(data.encode()).hexdigest()
        result += f"{hashed_data}"

    return result

def prelucrare(mode, password):
    global hash_initial, hash_final

    file_path = "D:\\PYTHON_2023\\proiect\\abc.exe"

    with open(file_path, "rb") as file:
        data = file.read()

    text = data.decode("utf-8")

    has_hash = "\n" in text and "|" in text.split("\n")[-1]

    if has_hash:
        hash_initial = text.split("|")[-1].strip()

    processed_text = encrypt_decrypt(text, password, mode)

    if mode == "decrypt" and has_hash:
        processed_text = processed_text.rsplit("\n", 1)[0]
        hash_final = hashlib.sha256(processed_text.encode()).hexdigest()
        if hash_final != hash_initial:
            print("Ceva e diferit :/")
            reencrypted_text = encrypt_decrypt(processed_text, password, "encrypt")
            processed_text = reencrypted_text

    processed_data = processed_text.encode("utf-8")

    with open(file_path, "wb") as file:
        file.write(processed_data)

prelucrare("encrypt", "ABCD")