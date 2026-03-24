from encryptor import Encryptor
import secrets
import string

def menu():
    usr_inp = None
    while usr_inp != "4":
        print("\n" + "#"*30)
        print("# 1 - Encrypt")
        print("# 2 - Decrypt")
        print("# 3 - Generate Secure Password")
        print("# 4 - Exit")
        print("#"*30)
    
        usr_inp = input("\nEnter 1, 2, 3, or 4: ")
        match usr_inp:
            case "1":
                encrypt_submenu()
            case "2":
                decrypt_submenu()
            case "3":
                gen_sec_pass_submenu()
            case _:
                print("\n[-] Invalid option. Please select 1, 2, 3, or 4.")

def encrypt_submenu():    
    usr_inp = None
    while usr_inp != "3":
        print("\n#####Encrypt Menu#####")
        print("# 1 - Encrypt string")
        print("# 2 - Encrypt file")
        print("# 3 - Return to previous menu")
        print("#"*22)
        usr_inp = input("\nEnter choice: ")
        match usr_inp:
            case "1":
                encrypt_string_submenu()
            case "2":
                ...

def encrypt_string_submenu():
    usr_inp = None
    while usr_inp != "4":
        print("\n#####Encrypt String#####")
        print("# 1 - Provide your own key.")
        print("# 2 - Load a previous key.")
        print("# 3 - Generate a new key.")
        print("# 4 - Return to previous menu")
        usr_inp = input("\nEnter choice: ")
        match usr_inp:
            case "1":
                usr_key = input("\nEnter your key: ").encode("utf-8") # have to encode the user input for Fernet to handle a key properly
                my_tool = Encryptor(usr_key)
                usr_str = input("Enter message to encrypt: ")
                print(f"Encrypted message: \n{my_tool.encrypt(usr_str)}")
                return
            case "2":
                my_tool = Encryptor(load_key=True)
                usr_str = input("Enter message to encrypt: ")
                print(f"Encrypted message: \n{my_tool.encrypt(usr_str)}")
                return
            case "3":
                my_tool = Encryptor()
                print("[+] Generated and saved new key.")
                print(f"Your new key is: {my_tool.key.decode('utf-8')}")
                usr_str = input("Enter message to encrypt: ")
                print(f"Encrypted message: \n{my_tool.encrypt(usr_str)}")
                return
            case _: 
                print("\n[-] Invalid option. Please select 1, 2, 3, or 4.")
    return


def decrypt_submenu(): 
    usr_inp = None
    while usr_inp != "3":
        print("\n#####Decrypt Menu#####")
        print("# 1 - Decrypt string")
        print("# 2 - Decrypt file")
        print("# 3 - Return to previous menu")
        print("#"*22)
        usr_inp = input("\nEnter choice: ")
        match usr_inp:
            case "1":
                decrypt_string_submenu()
            case "2":
                ...

def decrypt_string_submenu():
    usr_inp = None
    while usr_inp != "3":
        print("\n#####Decrypt String#####")
        print("# 1 - Provide your own key.")
        print("# 2 - Load key from file 'key.key'.")
        print("# 3 - Return to previous menu")
        usr_inp = input("\nEnter choice: ")
        match usr_inp:
            case "1":
                usr_key = input("\nEnter your key: ").encode("utf-8") # have to encode the user input for Fernet to handle a key properly
                my_tool = Encryptor(usr_key)
                usr_str = input("Enter message to decrypt: ")
                try:
                    print(f"Decrypted message: \n{my_tool.decrypt(usr_str)}")
                except Exception:
                    print("\n[-] Decryption failed! Check your key or message.")
                return
            case "2":
                my_tool = Encryptor(load_key=True)
                usr_str = input("Enter message to decrypt: ")
                try:
                    print(f"Decrypted message: \n{my_tool.decrypt(usr_str)}")
                except Exception:
                    print("\n[-] Decryption failed! Check your key or message.")
                return
            case _: 
                print("\n[-] Invalid option. Please select 1, 2, 3, or 4.")
    return

def gen_sec_pass_submenu():
    print("\n#####Secure Password Menu#####")
    usr_inp = None
    
    while True:
        try:
            usr_inp = int(input('Enter length of password(8 to 30) or "0" to return to previous menu: '))
        except ValueError:
            print("\n[-] Invalid value. Please enter a number.\n")
            continue
            
        if usr_inp == 0:
            return
        elif 8 <= usr_inp <= 30:       
            print(f"\n[+] Generated Password: {secure_pass(usr_inp)}")
            return
        else:
            print("\n[-] Password must be between 8 and 30 characters.")

def secure_pass(length):
    strong_pass = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation)
    ]
    for _ in range(length - 4):
        strong_pass.append(secrets.choice(string.ascii_letters + string.digits + string.punctuation))
    secrets.SystemRandom().shuffle(strong_pass)
    return(f'{"".join(strong_pass)}\n')
    
def main():
    menu()
    
if __name__ == "__main__":
    main()