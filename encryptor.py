from cryptography.fernet import Fernet

class Encryptor:
    def __init__(self, key=None, load_key=False):
        if key is None and load_key:
            self.load_key()        
        elif key:
            self.key = key
        else:
            self.key = Fernet.generate_key()
            self.save_key()

        self.cipher = Fernet(self.key)
        
    def encrypt(self, plain_text:str):
        str_bytes = plain_text.encode("utf-8") # encode string to bytes
        encrypted = self.cipher.encrypt(str_bytes) # use Fernet engine to encrypt string
        return encrypted.decode("utf-8") # decode puts it back to a string
    
    def decrypt(self, encrypted_text:str):
        try:
            str_bytes = encrypted_text.encode("utf-8")
            decrypted = self.cipher.decrypt(str_bytes)
            return decrypted.decode("utf-8")
        except Exception:
            return "[-] Decryption failed. Invalid key or corrupted data."
    
    def encrypt_file(self, filename):
        try:
            with open(filename, "rb") as file: #"rb" is for read binary
                data = file.read()
            
            encrypted_data = self.cipher.encrypt(data)
            
            with open(f"{filename}.encrypted", "wb") as file:
                file.write(encrypted_data)
            
            print(f"[+] {filename} encrypted successfully.\nEncrypted file: {filename}.encrypted")
        except FileNotFoundError:
            print(f"[-] Error: '{filename}' not found.")
    
    def decrypt_file(self, filename):
        try:
            with open(filename, "rb") as file: #"rb" is for read binary
                data = file.read()
            
            decrypted_data = self.cipher.decrypt(data)
            
            with open(f"{filename}.decrypted", "wb") as file:
                file.write(decrypted_data)
            
            print(f"[+] {filename} decrypted successfully.\nFile saved as: {filename}.decrypted")
        except (FileNotFoundError, Exception):
            print(f"[-] Error: '{filename}' not found or wrong key.")
    
    def save_key(self):
        with open("key.key", "wb") as file:
            file.write(self.key)
    
    def load_key(self):
        try:
            with open("key.key", "rb") as file:
                self.key = file.read()
        except FileNotFoundError:
            print("[-] File not found. Generating new key.")
            self.key = Fernet.generate_key()
            self.save_key()