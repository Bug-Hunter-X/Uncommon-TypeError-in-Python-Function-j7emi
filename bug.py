def function_with_uncommon_error(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Division by zero!")
        return None
    except TypeError:
        print("Type error occurred!")
        return None
    return result

# This will result in an uncommon TypeError
result = function_with_uncommon_error("hello", 5)