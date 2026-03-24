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
        str_bytes = encrypted_text.encode("utf-8")
        decrypted = self.cipher.decrypt(str_bytes)
        return decrypted.decode("utf-8")
    
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