from databaseHandler import register, update_firstName, update_lastName, update_username, update_password, deleteData, login, get_accountInfo
from datetime import datetime

# Additional module:
import maskpass
import base64

def encode_pw(password):

    encrypt = base64.b64encode(password.encode("utf-8"))
    return encrypt

def loginRights(username, password):
    while True:
        print("What do you want to do?")
        print("1. Change First Name")
        print("2. Change Last Name")
        print("3. Change Username")
        print("4. Change Password")
        print("5. Show Data")
        print("6. Delete Account")
        print("7. Logout")
        
        try:
            user_input = int(input(">>> "))

            if user_input >= 1 and user_input <= 7:
                if user_input == 1:
                    new_firstName = input("Enter new first name: ")
                    update_firstName(username, password, new_firstName)
                    print("")
                    print(f"First name changed to {new_firstName}")
                    print("")

                elif user_input == 2:
                    new_lastName = input("Enter new last name: ")
                    update_lastName(username, password, new_lastName)
                    print("")
                    print(f"Last name changed to {new_lastName}")
                    print("")

                # Username
                elif user_input == 3:
                    new_user = input("Enter new Username: ")
                    update_username(username, password, new_user)
                    username = new_user
                    print("")
                    print(f"Username changed to {new_user}")
                    print("")

                elif user_input == 4:
                    new_pass = maskpass.askpass(prompt="Enter new password: ", mask="*")
                    encnpw = encode_pw(new_pass)
                    update_password(username, password, encnpw)
                    password = new_pass
                    print("")
                    print(f"Password changed to {encnpw}")
                    print("")

                elif user_input == 5:
                    accInfo = get_accountInfo(username, password)
                    print("")
                    print("-"*40)
                    print(f"First name: {accInfo[0]}")
                    print(f"Last name: {accInfo[1]}")
                    print(f"Username: {accInfo[2]}")
                    print(f"Password: {accInfo[3]}")
                    print(f"Date Registered: {accInfo[4]}")
                    print("-"*40)
                    print("")

                elif user_input == 6:
                    username = input("Enter Username: ")
                    password = maskpass.askpass(mask="*")
                    encpw_d = encode_pw(password)
                    print("")

                    if login(username, password=encpw_d):
                        deleteData(username, password=encpw_d)
                        print("Account Deleted")
                        print("")
                    else:
                        print("Invalid Username/Password")
                        print("")

                elif user_input == 7:
                    print("")
                    print("Logged out")
                    print("")
                    break
            
            else:
                print("")
                print("ONLY 1-7 CAN BE USE")
                print("")

        except:
            print("")
            print("ONLY 1-7 CAN BE USE")
            print("")


def main():
    while True:
        print("Welcome to Login System!")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        
        try:
            user_input = int(input(">>> "))
        
            if user_input == 1 or user_input == 2 or user_input == 3: 
                if user_input == 1:
                    while True:
                        print("")
                        first = input("First Name: ")
                        last = input("Last Name: ")
                        user = input("Username: ")
                        pw = maskpass.askpass(prompt="Password: ", mask="*") # Hide pw using maskpass
                        encpwd = encode_pw(pw) # Encode pw using base64
                        date = datetime.strftime(datetime.now(), "%m/%d/%Y %I:%M:%p")
                        print("")
                        
                        sure = input("Are you sure (Y/N)? ")
                        if sure.lower() == "y":
                            register(first, last, user, encpwd, date)
                            print(user, "Registered")
                            print("")
                            break
                        elif sure.lower() == "n":
                            continue
                
                elif user_input == 2:
                    username = input("Enter Username: ")
                    password = maskpass.askpass(mask="*")
                    encpwd = encode_pw(password)
                    print("")

                    if login(username, password=encpwd):
                        print("You are now logged in")
                        print("")
                        loginRights(username, password=encpwd)
                    else:
                        print("There is no account in the database with those credentials")
                        print("")
                        continue

                elif user_input == 3:
                    print("")
                    print("Program Terminated")
                    print("")
                    break
            else:
                print("")
                print("ONLY 1,2,3 CAN BE USE")
                print("")

        except:
            print("")
            print("ONLY 1,2,3 CAN BE USE")
            print("")
                    
if __name__ == "__main__":
    main()