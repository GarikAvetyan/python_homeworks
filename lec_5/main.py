def sum_of_elements(numbers, exclude_negative=False):
    total = 0
    for num in numbers:
        if not exclude_negative or num >= 0:
            total += num
    return total

user_input = input("Enter a list of numbers separated by spaces: ")
numbers = [int(num) for num in user_input.split()]
exclude_negative_input = input("Do you want to exclude negative numbers? (yes or no): ")
exclude_negative = exclude_negative_input.lower() == "yes"
result = sum_of_elements(numbers, exclude_negative)

print(f"Sum of elements {'excluding' if exclude_negative else 'including'} negative numbers: {result}")