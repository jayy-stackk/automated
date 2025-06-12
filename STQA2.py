# Step 1: Function to validate user input
def validate_input(number):
    if 10 <= number <= 100:
        return "Valid Input"
    else:
        return "Invalid Input"

# Step 2: Apply Equivalence Partitioning
def equivalence_partitioning_tests():
    print("\n--- Equivalence Partitioning Tests ---")
    test_cases = [-5, 5, 50, 150]  # Divided into 3 partitions:
                                   # <10 (invalid), 10-100 (valid), >100 (invalid)
    for num in test_cases:
        result = validate_input(num)
        print(f"Test with input {num}: {result}")

# Step 3: Apply Boundary Value Analysis
def boundary_value_analysis_tests():
    print("\n--- Boundary Value Analysis Tests ---")
    boundary_values = [9, 10, 11, 99, 100, 101]  # Test just below, on, and just above boundaries
    for num in boundary_values:
        result = validate_input(num)
        print(f"Test with input {num}: {result}")

# Step 4: Main program execution
if __name__ == "__main__":
    # Allow user to enter input and validate
    try:
        user_input = int(input("Enter a number between 10 and 100: "))
        print(validate_input(user_input))
    except ValueError:
        print("Invalid input: Please enter an integer.")

    # Perform Black Box Testing
    equivalence_partitioning_tests()
    boundary_value_analysis_tests()

