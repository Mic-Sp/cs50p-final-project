from encryptor import Encryptor
import secrets
import string
import sys

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

def encrypt_submenu():
    print("\n#####Encrypt Menu#####")
    print("# 1 - Encrypt string")
    print("# 2 - Encrypt file")
    print("# 3 - Return to previous menu")
    print("#"*22)
    
    usr_inp = None
    while usr_inp != "3":
        usr_inp = input("\nEnter choice: ")

def decrypt_submenu():
    print("\n#####Decrypt Menu#####")
    print("# 1 - Decrypt string")
    print("# 2 - Decrypt file")
    print("# 3 - Return to previous menu")
    print("#"*22)
    
    usr_inp = None
    while usr_inp != "3":
        usr_inp = input("\nEnter choice: ")

def gen_sec_pass_submenu():
    print("\n#####Secure Password Menu#####")
    usr_inp = None
    
    while True:
        try:
            usr_inp = int(input('Enter length of password(8 to 30) or "0" to return to previous menu: '))
        except ValueError:
            print("Invalid value. Please enter a number.\n")
            continue
            
        if usr_inp == 0:
            return
        elif 8 <= usr_inp <= 30:       
            secure_pass(usr_inp)
            return

def secure_pass(length):
    strong_pass = ""
    for _ in range(length):
        strong_pass += secrets.choice(string.ascii_letters + string.digits + string.punctuation)
    print(f"\n[+] Generated Password: {strong_pass}\n")
    
def main():
    menu()
    
if __name__ == "__main__":
    main()