#simple password hashing
import bcrypt

#function to hash password
def hashPassword(pwd):
    salt= bcrypt.gensalt()
    hashedPassword = bcrypt.hashpw(pwd.encode("utf-8"),salt)
    return hashedPassword

#function to verify the hashed password
def verify_pwd(incoming_pwd,hashed_password):
    return bcrypt.checkpw(incoming_pwd.encode("utf-8"),hashed_password)

if __name__ == "__main__":
    password = "my_secret_password"

#hash password
hashed_password  = hashPassword(password)
print(f"Hashed Password: {hashed_password.decode()}")


#verify password
match = verify_pwd(password,hashed_password)
print(f"Password Match: {match}")