import random

# Generate a list of 20 random numbers between 1 and 100
unsorted_array = [random.randint(1, 100) for _ in range(20)]
sorted_array = unsorted_array.sort()

print(f"Unsorted Array: {unsorted_array}")
print(f"Sorted Array: {sorted_array}")

new_array = [12, 25, 34, 36, 37, 39, 46, 47, 51, 54, 57, 63, 65, 66, 68, 69, 69, 79, 83, 99]
[12, 25, 34, 36, 37, 39, 46, 47, 51, 54, 57, 63, 65, 66, 68, 69, 69, 79, 83, 99]

new_array.sort()
print(new_array)