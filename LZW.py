def LZW_compress(string):
    dictinory = {chr(i): i for i in range(256)}
    current_string = ""
    compressed_data = []
    next_code = 256

    for char in string: 
        combined_string = current_string + char
        if combined_string in dictinory:
            current_string = combined_string
        else:
            compressed_data.append(dictinory[current_string])
            dictinory[combined_string] = next_code 
            next_code += 1
            current_string = char

    if current_string:
        compressed_data.append(dictinory[current_string])

    return compressed_data