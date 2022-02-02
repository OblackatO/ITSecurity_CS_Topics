# Given a string X, get the longest substring that hasn't repeating characters in a raw.
# JUIKOP : valid
# JISS: Invalid because of 'SS', the good substring would be JIS

# input_string = "asdnkasdknaaaaduauwdamssdaomsodiasdhassdjiunbmösdppfsuhfssdhfaovmxxxvnalaspd"
input_string  = "aaaaaaaaaaaaaaaa"

"""
[>] Basic Idea
- Iterate over each char.
- Check if char == char-1
- If yes, a repittion was found, new substring starts

[>] Data structures
- final_longest_string
- temporary_string
- previous_char
- current_char

[>] Logic Remarks
- final_longest_string gets update if
    - A repetition is found when building temporary string
    && when temporary_string > final_longest_string
- previous_char = '' if
    - A repetition is found.
"""

def sliding_windows2(input_string: str) -> str:
    if type(input_string) is not str:
        print("Input must be a string")
        return ""
    final_longest_string = ""
    temporary_string = ""
    previous_char = ""
    for index in range(0, len(input_string)):
        current_char = input_string[index]
        if current_char == previous_char or index == len(input_string)-1: # There is a repetition or the last char was reached.
            previous_char = ""
            if final_longest_string == "" or len(temporary_string) > len(final_longest_string):
                final_longest_string = temporary_string
                temporary_string = current_char
            else:
                temporary_string = "" # Repetitive char found, start new temp string.
        else:
            temporary_string += current_char
        previous_char = current_char
    print(f"Longest non repetitive string found: {final_longest_string} - len: {len(final_longest_string)}")
    return final_longest_string

sliding_windows2(input_string)




















def sliding_window(input_string: str) -> str:
    longest_string_temp = ""
    longest_string_final = ""
    previous_char = ''
    for index in range(0,len(input_string)):
        if previous_char != input_string[index]:
            previous_char = input_string[index]
            longest_string_temp += input_string[index]
        else:
            if longest_string_final == "":
                longest_string_final = longest_string_temp
                continue
            if len(longest_string_temp) > len(longest_string_final): # A bigger non repetitive string was found.
                longest_string_final = longest_string_temp
                longest_string_temp = ""
            previous_char = ''
    if longest_string_final == "": # There are non repetitive characters in the whole input_string
        longest_string_final = input_string
    print(f"Longest non repetitive string found: {longest_string_final} - len: {len(longest_string_final)}")
    return longest_string_final


#sliding_window(input_string)


