def function_with_uncommon_error(a, b):
    try:
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            result = a / b
        else:
            print("Type error: Inputs must be numbers")
            return None
    except ZeroDivisionError:
        print("Division by zero!")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
    return result

# This will now correctly handle the type error
result = function_with_uncommon_error("hello", 5)
print(result)

result = function_with_uncommon_error(10, 2) #this will work fine
print(result)