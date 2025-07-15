import bcrypt
import getpass
import os

PASSWORD_FILE = "password.txt"

def hash_password(password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)

def check_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed)

def save_password(hashed):
    with open(PASSWORD_FILE, 'wb') as f:
        f.write(hashed)

def load_password():
    with open(PASSWORD_FILE, 'rb') as f:
        return f.read()

#store the hashed pwd in file
def set_new_password():
    print("Create a new password.")
    while True:
        pw1 = getpass.getpass("Enter password: ")
        pw2 = getpass.getpass("Confirm password: ")
        if pw1 != pw2:
            print("Passwords do not match. Try again.")
        else:
            #hash the pwed and store it in file
            hashed = hash_password(pw1)
            save_password(hashed)
            print("Password set successfully!")
            break

#verify password
def verify_existing_password():
    try:
        #get pwd from file
        hashed = load_password()
    except FileNotFoundError:
        print("No password set yet.")
        return

    #pass the new pwd and hashed one to check fn
    pw = getpass.getpass("Enter your password: ")
    if check_password(pw, hashed):
        print("Access granted.")
    else:
        print("Incorrect password.")

#calling the corresponding fn based on file created
def main():
    if not os.path.exists(PASSWORD_FILE):
        set_new_password()
    else:
        verify_existing_password()

if __name__ == "__main__":
    main()
