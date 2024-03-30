# 1. Name:
#      Grant Call
# 2. Assignment Name:
#      Lab 13: Prime Numbers
# 3. Assignment Description:
#      This program will display all the prime numbers at or below
#       a certain value. It will first prompt the user for an integer.
#       If the integer is less than 2, then the program will prompt
#       the user for another number. The program will then compute all
#       the prime numbers below (and including) the given number.
#       When finished, the program will display the list of prime numbers.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part for me was adding the asserts.
#      I struggle understanding them and where to put them.
#      Other than that everything was very stright forward
#      because of the design I made last week.
# 5. How long did it take for you to complete the assignment?
#      8 hours


import math

def get_range():
    """
    Prompts the user to enter a range number.
    If the value is below 2 it prints an error message for the user.
    It then reprompts the user enter a range number.

    Returns:
    - n_range (int): A range number that is equal to or greater than 2.
    """
    n_range = 0
    while n_range < 2:
        n_range = int(input("Enter the range number: "))
        if n_range >= 2:
            return n_range
        else:
            print(f"Input number {n_range} is less than 2. Input a number that is equal to or greater than 2")

def get_bool_array(n_range):
    """
    Creates a boolean array to represent prime numbers up to a given range.

    Args:
    - n_range (int): The range number.

    Returns:
    - is_prime_array (list): a boolean array representing prime numbers.
    """
    is_prime_array = [True] * (n_range + 1)
    is_prime_array[0] = False
    is_prime_array[1] = False
    return is_prime_array

def compute_sqrt(n_range):
    """
    Computes the square root of the given range number.

    Args:
    - n_range (int): The range number.

    Returns:
    - square_n (int): The square root of the range number.
    """
    square_n = int(math.sqrt(n_range))
    return square_n

def compute_prime_numbers(n_range, square_n, is_prime_array):
    """
    Computes the prime numbers up to the given range number.

    Args:
    - n_range (int): The range number.
    - square_n (int): The square root of the range number.
    - is_prime_array (list): a boolean array representing prime numbers.

    Returns:
    - is_prime_array (list): Updates boolean array after computing prime numbers.
    """
    for current_index in range(2, square_n + 1):
        assert 2 <= current_index <= len(is_prime_array) - 1 # current_index is out of range
        if is_prime_array[current_index]:
            for i_multiple in range(current_index * 2, n_range + 1, current_index):
                assert current_index <= i_multiple <= len(is_prime_array) - 1 # i_multiple is out of range
                is_prime_array[i_multiple] = False
    return is_prime_array

def get_prime_numbers_array(n_range, is_prime_array):
    """
    Gets the list of prime numbers up to the given range number.

    Args:
    - n_range (int): The range number.
    - is_prime_array (list): Boolean array representing prime numbers.

    Returns:
    - prime_nums (list): List of prime numbers.
    """
    prime_nums = []
    for num_index in range(n_range + 1):
        assert 0 <= num_index <= len(is_prime_array) - 1 # num_index is out of range
        if is_prime_array[num_index]:
            prime_nums.append(num_index)
    return prime_nums

def auto_test():
    """
    Runs automated tests from a list of test values.
    """
    test_values = [-1, 0, 1, 2, 10, 53, 100, 200]
    assert type(test_values) == list

    count = 0
    for value in test_values:
        count += 1
        print("=========================================================================================")
        print(f"Test case: #{count} - Testing input value {value}\n")
        if value >= 2:
            n_range = value
            original_is_prime_array = get_bool_array(n_range)
            square_n = compute_sqrt(n_range)
            new_is_prime_array = compute_prime_numbers(n_range, square_n, original_is_prime_array)
            prime_nums = get_prime_numbers_array(n_range, new_is_prime_array)
            print(f"This program will find all the prime numbers at or below N. Select that N: {n_range}")
            print(f"The prime numbers at or below {value} are {prime_nums}")
            print("=========================================================================================\n")
        else:
            print(f"Value: {value} is less than 2 and therfore not a prime number")
        
def main():
    """
    Executes the program.
    """
    auto_test()
    n_range = get_range()
    assert type(n_range) == int # n_range is not an integer
    original_is_prime_array = get_bool_array(n_range)
    assert type(original_is_prime_array) == list # original_is_prime_array is not a list
    square_n = compute_sqrt(n_range)
    assert type(square_n) == int # square_n is not an integer
    new_is_prime_array = compute_prime_numbers(n_range, square_n, original_is_prime_array)
    assert type(new_is_prime_array) == list # new_is_prime_array is not a list
    prime_nums = get_prime_numbers_array(n_range, new_is_prime_array)
    assert type(prime_nums) == list # prime_nums is not a list

    print(prime_nums)

if __name__ == "__main__":
    main()
