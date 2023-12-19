def convert_to_binary(character):
    binary_dict = {}
    for i in range(128):    # e.g, if i=65 chr(i)=A
        binary_dict[chr(i)] = bin(i)[2:].zfill(7)   # this will modify the above dict to all keys and their binary values
    if len(character) == 1 and character in binary_dict:
        result = binary_dict[character]
        print(f"Conversion of {character} in binary is: {result}")
    elif len(character) > 1:
        result = ' '.join(binary_dict[char] for char in character if char in binary_dict)
        print(f"Conversion of {character} in binary is: {result}")
    else:
        print("Invalid input. Please enter a valid ASCII character.")
if __name__ == "__main__":
    user_input = input("Enter a character to convert it to binary digits: ")
    convert_to_binary(user_input)
