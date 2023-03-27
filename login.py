
def open_file():
    '''Open text file and return the data list
    '''
    file_data = open("user_details.txt", "r").readlines()
    return file_data


def info_split(data):
    '''Split items in file and return split list
    '''
    split_code = data.split(" - ")
    return split_code


def user_info(file_data):
    '''Add file data to a dictionay, key: username, value: email address,
    return dictionary.
    '''

    user_details = {}

    for item in range(len(file_data)):

        data =  info_split(file_data[item])

        if data[0] not in user_details:
            
            user_details[data[0]] = data[1].replace("\n", "")
            
    return user_details


def main():
    '''Check if user input is in the dictionary (data from text file)
    in order for user to login.
    '''

    file_data = open_file()

    print(user_info(file_data))

    check_data = user_info(file_data)

    print("********************* LOGIN *********************")
    
    while True:

        username = input("Username: ")
        userEmail = input("Email address: ")

        if username in check_data and userEmail == check_data[username]:
            print("Successfully logged in.")
            break
        else:
            print("Incorrect login details, please try again.")
            continue



if __name__ == "__main__":

    main()


