# 1. Name:
#      Grant
# 2. Assignment Name:
#      Lab 08: Sort
# 3. Assignment Description:
#      This program will read a list of names from a file and sort them.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part of this was figuring out how to translate the
#      psuedocode in python code. The hardest part about that was
#      figuring out the sort algorithm and implimenting it correctly.
#      The It was difficult figuring out what asserts to put into
#      my program and how to write them. The hardest asserts to understand
#      and to write was the the one that checked if the list was sorted.
#      The next was the index of out range asserts.
# 5. How long did it take for you to complete the assignment?
#      14 hours

import json

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
        print(f"Unable to open file '{filename}'.")
        print("The file was not found it is most likely not spelled correctly")
        print("Or the file does not exist.")

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
        data_list = data_json["array"]
        assert data_list is not None
        assert type(data_list) == list # datalist is not a list
        return data_list
    except:
        print("There is a problem with loading the json data")
    return []

def get_list_size(data_list):
    """
    Gets length of list
    Args:
        data_list (list): a list of elements (type is not specified)
    Returns:
        A variable with the value of the length of the list
    """

    list_size = len(data_list) 
    return list_size

def sort_lists(data_list, list_size):
    """
    Sorts a list
    Args:
        data_list (list): a list of elements (type is not specified)
        list_size (variable int): a varible containing the value of the length of a list
    Returns:
        A sorted list
    """
    for i_pivot in range(list_size - 1, 0, -1):
        assert 0 <= i_pivot < len(data_list) # Index out of range.
        i_largest = 0

        for i_check in range(1, i_pivot):
            assert 0 <= i_check < len(data_list) # Index out of range.
            assert 0 <= i_largest < len(data_list) # Index out of range.
            if data_list[i_check] > data_list[i_largest]:
                i_largest = i_check
        
        if data_list[i_largest] > data_list[i_pivot]:
            swap_value = data_list[i_largest]
            data_list[i_largest] = data_list[i_pivot]
            data_list[i_pivot] = swap_value

    if __debug__:
        for i in range(len(data_list)- 1):
            assert data_list[i] <= data_list[i + 1] # list is not sorted


    return data_list
    


def display_unsorted_list(unsorted_data_list, filename):
    print("\n-------------------------------------------------")
    print(f"This is the unsorted list for {filename}")
    print(unsorted_data_list) # this is here to compare with the end result to see if it was sorted correctly
    print("-------------------------------------------------")

def display_sorted_list(sorted_data_list, filename):
    print("-------------------------------------------------")
    print(f"This is the Sorted list for {filename}")
    print(sorted_data_list) # Assert that the datalist was actually sorted
    print("-------------------------------------------------")
    

def get_files_list():
    """
    It stores file names in a list
    Returns:
        A list of filenames
    """
    filenames = ["Lab08.empty.json", "Lab08.trivial.json", "Lab08.languages.json", "Lab08.states.json", "Lab08.cities.json"]
    return filenames

def run_sort(filename):
    """
    Runs all of the functions needed to perfrom the sort
    Args:
        
        filename (variable str): a varible containing a filename that is a string

    """
    assert filename is not None
    assert type(filename) == str
    assert len(filename) > 0 
    file_data = read_file(filename)
    unsorted_data_list = load_data(file_data)
    # display_unsorted_list(unsorted_data_list, filename) optional
    list_size = get_list_size(unsorted_data_list)
    sorted_data_list = sort_lists(unsorted_data_list, list_size)
    display_sorted_list(sorted_data_list, filename)


def test_driver():
    """
    Runs test cases on a list of file names
    """
    filenames = get_files_list()
    count = 0
    for filename in filenames:
        count += 1
        print(f"\nTest Case #{count}")
        print(filename)
        run_sort(filename)

def main():

    auto = input("Do you want to automatically run your test cases? (y/n): ").lower()
    if auto == "y":
        test_driver()
    else:
        filename = get_file()
        run_sort(filename)

if __name__ == "__main__":
    main()
