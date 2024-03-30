# 1. Name:
#      Grant Call
# 2. Assignment Name:
#      Lab 13 : Segregation Sort Program
# 3. Assignment Description:
#      This program is designed to implement a segregation sort algorithm.
#      This sorting algorithm is a recursive algorithm that sorts an array.
#      This program also includes a test function that validates the
#      segregation sort algorithm.
# 4. What was the hardest part? Be as specific as possible.
#      The most challenging part of this assignment was changing
#      the sorting algorithm from pseudocode to python code.
#      Honestly it was really simple and pretty easy.
#      I had some trouble with integrating the test function.
# 5. How long did it take for you to complete the assignment?
#      The assignment took approximately 3 hours to complete.

red = "\033[91m"
green = "\033[92m"
yellow = "\033[93m"
purple = "\033[35m"
cyan = "\033[96m"
reset = "\033[0m"

def get_array():
    """
    Generates and return a predefined array of integers.
    
    Returns:
        list: A list of integers.
    """
    array = [25, 9, 32, 8, 72, 7, 6, 32, 5, 95, 4, 3, 18, 2, 50, 1, 31, 89, 10, 77, 46, 55, 92]
    # print(array)
    return array

def display_array(array, name):
    """
    Displays an array with a given name in a formatted style with colored text.

    Args:
        array (list): The array to display.
        name (str): A descriptive name for the array.
    """
    print(f"{yellow}====================================================") # Start yellow color
    print(f"{name}:")
    print(f"\t> {array}")
    print(f"===================================================={reset}")  # End yellow color

def sort_rec(array, i_start, i_end):
    i_up = i_start
    i_down = i_end
    i_pivot = (i_start + i_end) // 2

    # End condition
    if i_up >= i_down or array == []:
        return array

    while i_up < i_down:
        while array[i_up] <= array[i_pivot] and i_up < i_pivot:
            i_up += 1
        while array[i_down] >= array[i_pivot] and i_down > i_pivot:
            i_down -= 1

        if i_pivot == i_up:
            i_pivot = i_down
        elif i_pivot == i_down:
            i_pivot = i_up

        # Swap elements
        array[i_up], array[i_down] = array[i_down], array[i_up]

    sort_rec(array, i_start, i_pivot - 1)
    sort_rec(array, i_pivot + 1, i_end)
    return array

def run_test_cases():
    """
    Runs test cases to validate the sort_rec function.
    Displays the result of each test case in colored text.
    """
    # Test cases: an array of arrays for input and expected output
    test_inputs = [
        [6, 12, 11],  # Trace example Unsorted
        ["witch", "pumpkin", "ghost", "vampire", "zombie"],  # Array of Strings Unsorted,
        [3, 2, 1, 5, 4],  # Normal Unsorted
        [1, 2, 3, 4, 5],  # Already Sorted
        [5, 4, 3, 2, 1],  # Reverse Sorted
        ["This will Cause an assertion error"],
        [1],  # Single Element
        [],  # Empty Array
        
    ]
    expected_outputs = [
        [6, 11, 12],
        ["ghost", "pumpkin", "vampire", "witch", "zombie"],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        ["Intentional Error"],
        [1],
        [],
    ]

    print(f"{cyan}\nRunning test cases...\n{reset}")
    count = 0
    success = 0
    fail = 0
    # Loop through each test case using its index
    for index in range(len(test_inputs)):
        count += 1
        # Sort the input array using the sort_rec function
        sorted_array = sort_rec(test_inputs[index], 0, len(test_inputs[index]) - 1)
        # Assert that the sorted_array matches the expected output

        if sorted_array == expected_outputs[index]:
            success += 1
        else:
            fail += 1

        try:
            assert sorted_array == expected_outputs[index]
            # If the assert does not fail, display a success message in green
            print(f"{green}====================================================")  # Start green color
            print(f"Case {count}: Test passed!\n \t> Input:           {test_inputs[index]}\n \t> Expected Output: {expected_outputs[index]}\n \t> Actual Output:   {sorted_array}")
            print(f"====================================================\n{reset}")  # End green color

        except AssertionError:
            # If the assert fails, display a failure message in red
            print(f"{red}====================================================")  # Start red color
            print(f"Case {count}:\n \t > Test failed for input: {test_inputs[index]}\n\t > Expected Output:       {expected_outputs[index]}\n\t > Actual Output:         {sorted_array}")
            print(f"====================================================\n{reset}")  # End red color

    print(f"{cyan}\nResults:{reset}")
    print(f"\t{purple}> Test cases ran: {count} {reset}")
    print(f"\t{green}> Test Cases Passed: {success}{reset}")
    print(f"\t{red}> Test Cases Failed: {fail}{reset}")
    

def main():
    # Get the predefined array
    array = get_array()

    # Display the unsorted array
    display_array(array, "Unsorted Array")

    # Sort the array
    sorted_array = sort_rec(array, 0, len(array) - 1)

    # Display the sorted array
    display_array(sorted_array, "Sorted Array")

    # Run the test cases
    run_test_cases()


if __name__ == "__main__":
        main()