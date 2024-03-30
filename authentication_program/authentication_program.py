# 1. Name:
#      Grant Call
# 2. Assignment Name:
#      Lab 02: Authentication
# 3. Assignment Description:
#      Write a program to read the contents of the file into a list.
#      The program will then prompt the user for a username and password.
#      Finally, we will tell the user whether the user is authenticated.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was figuering out how to autheticate the user.
#      The next hardest thing was fuguering out how to automate the testing.
#      It was more difficult that figuering out how to authenticate the user.
#      The difference was that figuring out how to authenticate the user took
#      longer and was harder for me to grasp the concepts.
#      The testing took more trial and error when I was coding
#      So that was why I considered it one of the most difficult parts.
# 5. How long did it take for you to complete the assignment?
#      It took me close to 12 hours to complete this lab.
#      This included reading documentation and trying to figure out
#      how to impliment what I was reading. I also met with several
#      professors to ask questions so that I would understand the concepts
#      I was using in code.

# Sources:
#      Brother Helfrich, Brother Thompson, Brother Hayes, Brother Macbeth
#      https://www.freecodecamp.org/news/loading-a-json-file-in-python-how-to-read-and-parse-json/
#      Loading a JSON File in Python – How to Read and Parse JSON
#      https://www.w3schools.com/python/python_try_except.asp
#      https://www.w3schools.com/python/python_functions.asp
#      https://www.freecodecamp.org/news/create-a-dictionary-in-python-python-dict-methods/
#      https://www.w3schools.com/python/ref_func_zip.asp


import json

def read_file(file_name):
    try:
        with open(file_name) as file_handle:
            data_text = file_handle.read()
        return data_text
    except:
        print(f"Unable to open file 'Lab02.json' the file that was used is named: {file_name}.")

def load_json(data_text):
    try:
        data_json = json.loads(data_text)
        return data_json
    except:
        print("There is a problem with loading the json data")

def get_lists(data_json):
    usernames_list = data_json["username"]
    passwords_list = data_json["password"]
    return usernames_list, passwords_list

def make_dictionary(usernames_list, passwords_list):
    user_lookup_dict = dict(zip(usernames_list, passwords_list))
    return user_lookup_dict

def get_user_input():  
    username_input = input("username: ")
    password_input = input("password: ")
    return username_input, password_input

def authenticate_user(username_input, password_input, user_lookup_dict):
    if username_input in user_lookup_dict:
        if user_lookup_dict[username_input] == password_input:
            return "You're authenticated"
        
    return "You are not authorized to use the system."

def run_test_case(user_lookup_dict):
    
    test_cases = [
    ["Incorrect username", "John Cheese", "None shall pass", "You are not authorized to use the system."],
    ["Incorrect password", "Black Knight", "Tis but a scratch.", "You are not authorized to use the system."],
    ["Both incorrect", "John Cheese", "Tis but a scratch.", "You are not authorized to use the system."],
    ["Wrong Index", "King Arthur", "Bring out your dead!", "You are not authorized to use the system."],
    ["Valid Black Knight", "Black Knight", "None shall pass", "You're authenticated"],
    ["Valid King Arthur", "King Arthur", "Run away!", "You're authenticated"],
    ["Valid French Soldier", "French Soldier", "I fart in your general direction", "You're authenticated"]
]
    number_test = 0
    for case in test_cases:
        number_test += 1
        title_test = case[0]
        username_test = case[1]
        password_test = case[2]
        expected_result_test = case[3]

        auth = authenticate_user(username_test, password_test, user_lookup_dict)
        

        if expected_result_test == auth:
            result = "The test result matched expected result. The test Passed"
        else:
            result = "The test result does not match expected result. The test Failed"


        print(f"\nTest Case Number: {number_test}")
        print(f"\n\t{title_test}")
        print(f"\tUsername: {username_test}")
        print(f"\tPassword: {password_test}")
        print(f"\t{auth}")
        print(f"\t{result}\n")

def main():
    file_name = 'Lab02.json'
    data_text = read_file(file_name)
    data_json = load_json(data_text)
    usernames_list, passwords_list =  get_lists(data_json)
    user_lookup_dict = make_dictionary(usernames_list, passwords_list)
    run_test_case(user_lookup_dict)
    username_input, password_input = get_user_input()
    auth = authenticate_user(username_input, password_input, user_lookup_dict)
    print(auth)


if __name__ == "__main__":
    main()
