def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    
    count = 0
    while number != 1:
        if number % 2 == 0:
            number //= 2  # Use integer division for even numbers
        else:
            number = 3 * number + 1  # Calculate 3n + 1 for odd numbers
        count += 1
    
    return count