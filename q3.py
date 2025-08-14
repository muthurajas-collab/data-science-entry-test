def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    if not isinstance(dct, dict):
        raise TypeError("dct must be a dictionary")
    
    if key in dct:
        print(f"Original value for '{key}': {dct[key]}")
    
    dct[key] = value
    return dct


# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
# - {"age": 25}, "age", 26

# Scenario 1
result1 = update_dictionary({}, "name", "Alice")
print(result1)  # Expected: {'name': 'Alice'}

# Scenario 2
result2 = update_dictionary({"age": 25}, "age", 26)
# Expected print: Original value for 'age': 25
print(result2)  # Expected: {'age': 26}
