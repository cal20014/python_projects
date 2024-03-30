# 1. Name:
#      Grant Call
# 2. Assignment Name:
#      Lab 10: Numeric Sequence
# 3. Assignment Description:
#      The program prompts the user for a positive integer
#      then it displays the nth or requested François number.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part for me was actually understanding the pseudocode
#      for the example. I struggled to understand this line:
#      array[index % 2] = array[0] + array[1]. It was confusing to me
#      and after I rewrote it several times that it finally clicked.
#      The other part for me was trying to understand how to write the
#      asserts that I wanted and make them work the way I intended them to.
#      I also strugged to figure out how to write the ttest cases and
#      how I would get them all to run without failing so I could display
#      each test case.
# 5. How long did it take for you to complete the assignment?
#      8 hours

def get_françois_num():
    """
    Prompts the user to enter a positive number and returns the entered number.
    
    Returns: (int) The positive number entered by the user.
    """
    while not done:
        françois_number = int(input("Enter a number: "))
        if françois_number > 0:
            done = True
        else:
            print("Invalid input. Please input a number greater than 0.")
    return françois_number

def calculate_françois_num(françois_number):
    """
    Calculates the François number for a given input number.
    
    Args:
    françois_number (int): The input number for which to calculate the François number.
    
    Returns:
    int: The François number corresponding to the input number.
    """
    assert type(françois_number) == int
    array = [1, 2]
    assert type(array) == list
    if françois_number > 2:
        for index in range(3, françois_number + 1):
            assert len(array) == 2 # Index out of range error: Array length is not equal to 2
            assert 0 <= index % 2 < len(array) # Index out of range.
            array[index % 2] = array[0] + array[1]

    value = array[françois_number % 2]
    return value

def run_test_cases():
    """
    Runs a set of test cases to display the calculated François number for each test case.
    """
    test_cases = [-1, 0, 1, 2, 9, 100, 200]
    assert type(test_cases) == list
    count = 0
    for françois_number in test_cases:
        assert type(françois_number) == int
        count += 1
        if françois_number > 0:
            print(f"Case # {count} - test case: {françois_number}: {calculate_françois_num(françois_number)}")
        else:
            print(f"Case # {count} - test case: {françois_number}: The input was less than zero. Therefore the value was invalid")
        
def main():
    """
    Prompts the user to choose whether to run test cases or to run the program normally
    If test cases are chosen, it calls the run_test_cases function.
    If an interactive number entry is chosen, it calls the get_françois_num and calculate_françois_num functions,
    and displays the calculated François number.
    """
    choice = input("Do you want to run the test cases? (y/n): ")
    if choice == "y":
        run_test_cases()
    else:
        françois_number = get_françois_num()
        value = calculate_françois_num(françois_number)
        print(f"Result: {value}")

if __name__ == '__main__':
    main()
