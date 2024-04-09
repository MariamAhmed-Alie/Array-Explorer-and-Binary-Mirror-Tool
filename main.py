# Array manipulation functions

# Find elements in an array using XOR
def find_elements_using_xor(arr):
    xor_result = 0
    for element in arr:
        xor_result ^= element
    print(f"Elements found in your array using XOR: {xor_result}")
    return xor_result

# Finding repeating elements in an array of size n
def find_repeating_elements(arr):
    unique_elements = set()
    repeating_elements = set()
    for element in arr:
        if element in unique_elements:
            repeating_elements.add(element)
        else:
            unique_elements.add(element)
    print(f"Repeating elements found in your array: {repeating_elements}")
    return list(repeating_elements)

# Find odd occurring elements in an array
def find_odd_occurring_elements(arr):
    element_count = {}
    for element in arr:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1
    odd_elements = [element for element, count in element_count.items() if count % 2 != 0]
    print(f"Odd occurring elements found in your array: {odd_elements}")
    return odd_elements

# Swap variables without using a third variable
def swap_variables(a, b):
    a, b = b, a
    print(f"Your variables have been swapped: {a, b}")
    return a, b

# Binary palindrome check
def is_binary_palindrome(num):
    binary = bin(num)[2:]
    if binary == binary[::-1]:
        print(f"{binary} is a palindrome.")
        return True
    else:
        print(f"{binary} is not a palindrome.")
        return False

# User input function
def main():
    try:
        while True:
            print("\nMenu:")
            print("1. Find elements in an array using XOR")
            print("2. Find repeating elements in an array")
            print("3. Find all odd occurring elements in an array")
            print("4. Swap variables without using a third variable")
            print("5. Check if binary representation of a number is palindrome")
            print("6. Exit")
            choice = input("Enter your choice (1-6): ")
            if choice == "1":
                user_array = list(map(int, input("Please provide an array (space-separated integers): ").split()))
                find_elements_using_xor(user_array)
            elif choice == "2":
                user_array = list(map(int, input("Please provide an array (space-separated integers): ").split()))
                find_repeating_elements(user_array)
            elif choice == "3":
                user_array = list(map(int, input("Please provide an array (space-separated integers): ").split()))
                find_odd_occurring_elements(user_array)
            elif choice == "4":
                user_vars = list(map(int, input("Please provide two variables (space-separated integers): ").split()))
                if len(user_vars) != 2:
                    print("Please provide exactly two variables.")
                else:
                    swap_variables(user_vars[0], user_vars[1])
            elif choice == "5":
                user_num = int(input("Please provide a number: "))
                is_binary_palindrome(user_num)
            elif choice == "6":
                print("Exiting the program...")
                break
            else:
                print("Invalid choice. Please try again.")
    except ValueError as e:
        print("You have entered the value incorrectly. Please enter integer values.")

if __name__ == "__main__":
    main()