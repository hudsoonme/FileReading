# Read from a file
with open("input.txt", "r") as file:
    data = file.read()
    print(data)

# Write to a file
with open("output.txt", "w") as file:
    file.write("Hello, World!")