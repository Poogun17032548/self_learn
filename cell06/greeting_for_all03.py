def greeting(name = "noble guest"):
    if not isinstance(name, str):
        return "Error: Name must be a string."
    else:
        return f"Hello, {name}!"

print(greeting())
print(greeting("Alice"))
print(greeting("Bob"))
print(greeting(123))  # This will trigger the type check and print an error message