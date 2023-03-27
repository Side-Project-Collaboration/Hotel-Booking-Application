
def write_info_to_file(name, email):
    '''Wrrte username and login to text file
    '''

    file = open("user_details.txt", "a")

    data = name + " - " + email
    file.write(data + "\n")
    file.close()


def main():
    '''Prompt user to sign up, check if no empty string is entered,
    write details to text file.
    '''

    print("********************* SIGN UP *********************")

    while True:

        username = input("Username: ")
        userEmail = input("Email address: ")

        if username == "" or userEmail == "":
            print("Please enter username or email address.")
            continue
        else:
            print("Thank you for signing up!")
            break

    write_info_to_file(username, userEmail)
    # pass


if __name__ == "__main__":

    main()