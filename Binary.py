# def coverted(ans):
#     # convert=bin(value)
#     # convert=convert.lstrip("0b")
#     print(ans)


# stats from hereeeeeeeeeeeeeeeeeeee
# ask=input("Enter a Character to convert it in binary digits:\n")
# def convertion(ask):
#     output_string=""
#     for i in range (0,127):
#         # make1=bin(chr(i))
#         # print(bin(i))
#         # to_bin=bin(i)
#         if(len(ask)>1):
#             for word in ask:
#                 if(chr(i)==word):
#                     ans=bin(i)
#                     ans=ans.lstrip("0b")
#                     output_string+=ans+" "
#                     print(f"Conversion of {word} in binary is:",ans)            
#         elif(chr(i)==ask):
#             ans=bin(i)
#             ans=ans.lstrip("0b")
#             # print(ans)
#             output_string+=ans+" "
#     print(output_string)
# convertion(ask)
# ends hereeeeeeeeeeeeeeeeeeeeeeeee


                    # for whatagain in range(0,len(ask)):
                    #     if(word==ask[whatagain]):
        # print(chr(i),i,to_bin.lstrip("0b"))
# butnow=chr(ask)
# butnow2=bin(butnow)
# butnowagin=bin(ask)
# print(butnowagin)
# print(butnow2)
# for i in range (33,127):
#     make1=list(chr(i))
#     make2=list(i)
#     print(make1)
#     print(make2)
    # to_bin=bin(i)
    # print(chr(i),i,to_bin.lstrip("0b"))


# into_number=chr(97)
# a=chr(65)
# print(a)
# print(into_number)
# match ask:
#     case 1:
#         get1=int(input("Enter a Number: "))
#         convertbinary(get1)
#     case 2:
#         get2=input("Enter a Character: ")
#         convertbinary(get2)
#     case 3:
#         get3=input("Enter a String: ")
#         convertbinary(get3)
#     case _:
        # print("Error!")





# CHATGPT Generated:

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
    # print(binary_dict)
if __name__ == "__main__":
    user_input = input("Enter a character to convert it to binary digits: ")
    convert_to_binary(user_input)