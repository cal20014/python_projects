# 1. Name:
#      Grant Call
# 2. Assignment Name:
#      Lab 06: Advanced Search
# 3. Assignment Description:
#      This program is designed to facilitate searching for a specific name
#      within the contents of a file. It prompts the user to enter a filename
#      and proceeds to read the file's contents, storing them in a list.
#      The user is then prompted to enter a name. Afterwards, the program
#      determines whether the entered name exists within the list of file
#      contents and provides the user with the corresponding result.
# 4. Algorithmic Efficiency
#      It is O(log n) it is that way because of the arch type it makes.
#      You can see from the graph my program plotted and from the table
#      My code generated for every doubling of the input size the efficency
#      decreases exponentially. It looks like a steaper arch that plateaus.
# 5. What was the hardest part? Be as specific as possible.
#      the hardest part for me was both the refaxctoring to functions so that
#      I could impliment automated testing and the calculating of the
#      algorithmic efficiency. It was hard for me to wrap my head around.
#      especially since I was sick and not able to make it to class this week.
# 6. How long did it take for you to complete the assignment?
#      15 hours

import json
import math
import matplotlib.pyplot as plt

# Global variables
filename = ""
counter = 0
lengths = []
iterations = []


def get_file():
    """
    Prompts the user to enter the name of the file.
    Returns:
        str: The name of the file entered by the user.
    """
    filename = input("What is the name of the file? ")
    return filename


def read_file(filename):
    """
    Reads the contents of the file.
    Args:
        filename (str): This is the name of the file that will be read.
    Returns:
        file_data (str): The text content of the file.
    """
    try:
        with open(filename, "r") as file:
            file_data = file.read()
        return file_data
    except:
        print(f"Unable to open file '{filename}'")
        print("The file was not found it is most likely not spelled correctly.")


def load_data(file_data):
    """
    Loads data from the file data as JSON.
    Args:
        file_data (str): The text content of the file.
    Returns:
        list: The list of names extracted from the JSON data.
    """
    try:
        data_json = json.loads(file_data)
        names_list = data_json["array"]
        return names_list
    except:
        print("There is a problem with loading the json data")
        return []

def get_search_word():
    """
    Prompts the user to enter the word they are looking for.
    Returns:
        search_word (str): The search word entered by the user.
    """
    search_word = input("What name are we looking for? ")
    return search_word

def binary_search(names_list, search_word):
    """
    Performs the binary search on the names list to find the search word.
    Args:
        names_list (list): The list of names to search in.
        search_word (str): The word the algorithm is searching for.
    Returns:
        found (boolean): True if the search word is found, False otherwise.
    """
    # Initializing variables for binary search
    i_min = 0
    i_max = len(names_list) - 1
    found = False
    global counter

    # Performing binary search on the names list
    while i_min <= i_max and not found:
        counter += 1
        i_middle = math.floor((i_min + i_max) / 2)

        if names_list[i_middle] < search_word:
            i_min = i_middle + 1
        elif names_list[i_middle] > search_word:
            i_max = i_middle - 1
        else:
            found = True

    return found

def run_test_cases(filename, search_word):
    """
    Runs the test cases for binary search.
    Args:
        filename (str): The name of the file to read.
        search_word (str): The word to search for.
    Returns:
        found (boolean): True if the search word is found, False otherwise.
    """
    file_data = read_file(filename)
    names_list = load_data(file_data)
    found = binary_search(names_list, search_word)
    get_efficiency(names_list)
    return found

def test_cases():
    """
    Runs multiple test cases for the binary search algorithm.
    """
    test_cases = [
        ["Empty list", "Lab06.empty.json", "Empty", False],
        ["Single item found", "Lab06.trivial.json", "trivial", True],
        ["Single item not found", "Lab06.trivial.json", "missing", False],
        ["Small list found", "Lab06.languages.json", "C++", True],
        ["Small list not found", "Lab06.languages.json", "Lisp", False],
        ["Big list found", "Lab06.countries.json", "United States of America", True],
        ["Big list not found", "Lab06.countries.json", "United States", False]
    ]
    
    test_num = 0
    for case in test_cases:
        test_num += 1
        case_title = case[0]
        filename = case[1]
        search_word = case[2]
        expected_result = case[3]

        print("-----------------------------------")
        print(f"Test Case Number: {test_num}\n")
        found = run_test_cases(filename, search_word)
        
        # Checking if the search word was found and printing the appropriate message
        if expected_result == found:
            result = f"The expected result was: '{expected_result}'\n" \
                     f"The test result was: '{found}'\n" \
                     f"The test result matched expected result.\n" \
                     "The test Passed."
        else:
            result = f"The expected result was: '{expected_result}'\n" \
                     f"The test result was: '{found}'\n" \
                     f"The test result does not match expected result.\n" \
                     "The test Failed."

        print(f"Case Title: {case_title}")
        print(f"Filename: {filename}")
        print(f"Search Word: {search_word}")
        print(f"{result}")
        
        if found:
            print(f"The search word: '{search_word}' was found in '{filename}'.")
        else:
            print(f"The search word: '{search_word}' was not found in '{filename}'.")
        print("-----------------------------------")

def get_efficiency(names_list):
    """
    Calculates and prints the efficiency plot point numbers of the binary search.
    Args:
        names_list (list): The list of names used for searching.
    """
    n = len(names_list)
    c = counter

    lengths.append(n)
    iterations.append(c)

    print("Data points")
    print(f"The length of the list: {n}")
    print(f"How many iterations it took: {c}\n")

def display_table():
    """
    Prints the input and the counter to a table to the terminal.
    """
    print("n | c")
    print("--+--")
    for n, c in zip(lengths, iterations):
        print(f"{n} | {c}")

def display_graph():
    """
    Creates, displaysand plots the points on the graph.
    It shows the data from the lengths and the iterations lists.
    """
    plt.plot(lengths, iterations, 'ro-')
    plt.xlabel("Input(n)")
    plt.ylabel("Iterations(c)")
    plt.title("Algorithm Efficiency Graph")
    plt.show()

def create_test_lists():
    """
    Creates test lists based on user input.
    
    Returns:
        lists (list): A list of lists containing the generated test lists.
    """
    num_lists = int(input("How many lists do you want? "))

    lists = []
    for i in range(num_lists):
        length = int(input(f"Enter the length of list {i+1}: "))
        new_list = list(range(1, length + 1))
        lists.append(new_list)

    return lists

def default_test_lists():
    """
    Generates default test lists with set predefined lengths for the lists.
    
    Returns:
        lists (list): A list of lists containing the generated default test lists.
    """
    test_lengths = [4, 8, 16, 32, 64, 124, 248, 496, 992, 1984]

    lists = []
    for length in test_lengths:
        new_list = list(range(1, length + 1))
        lists.append(new_list)

    return lists

def test_efficiency():
    """
    Performs efficiency testing on the binary search algorithm.

    The function prompts the user to choose whether to create their own lists or use default test lists.
    Then it clears any existing data in lengths and iterations lists.

    For each test list, it performs a binary search for the last element of the list,
    calculates the efficiency, and stores the results.

    Lastly, It calls the display functions for the table and the graph.
    """
    choice = input("Do you want to create your own lists?(y/n): ").lower()
    if choice == "y":
        lists = create_test_lists()
    else:
        lists = default_test_lists()
    lengths.clear()
    iterations.clear()

    for test_list in lists:
        search_word = test_list[-1]
        
        binary_search(test_list, search_word)
        get_efficiency(test_list)

    display_table()
    display_graph()

def main():
    """
    Runs the program and executes the tests for the binary search.

    This function promps if they want to run the tests.
    If they do it runs the test_cases function and the test_efficiency function

    If the user chooses not to run the tests this function runs
    it prompts for a filename, reads the file data, performs a binary search on the loaded data,
    calculates the efficiency, and displays the search results.

    """
    test = input("Do you want to run the tests? (y/n): ")
    if test.lower() == 'y':
        test_cases()
        test_efficiency()
    else:
        filename = get_file()
        file_data = read_file(filename)
        names_list = load_data(file_data)
        search_word = get_search_word()
        found = binary_search(names_list, search_word)
        get_efficiency(names_list)

        # Checking if the name was found and printing the appropriate message
        if found:
            print(f"We found {search_word} in {filename}.")
        else:
            print(f"{search_word} was not found in {filename}.")

if __name__ == "__main__":
    main()



