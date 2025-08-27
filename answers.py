# File Read & Write Challenge

# Read the content of input.txt
with open("input.txt", "r") as infile:
    content = infile.read()

# Modify the content (example: make it uppercase)
modified_content = content.upper()

# Write modified content to output.txt
with open("output.txt", "w") as outfile:
    outfile.write(modified_content)

print("File modified and written to output.txt ✅")


# Error Handling Lab

filename = input("Enter the filename: ")

try:
    with open(filename, "r") as f:
        print("File content:\n")
        print(f.read())
except FileNotFoundError:
    print("❌ Error: File not found.")
except PermissionError:
    print("❌ Error: You don’t have permission to read this file.")
except Exception as e:
    print(f"❌ An unexpected error occurred: {e}")
