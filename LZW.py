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

def LZW_decompress(compressed_data):
    dictinory = {i: chr(i) for i in range(256)}
    current_code = compressed_data[0]
    current_string = dictinory[current_code]
    decompressed_data = [current_string]
    next_code = 256
    for code in compressed_data[1:]:
        if code in dictinory:
            entry = dictinory[code]
        elif code == next_code:
            entry = current_string + current_string[0]
        else:
            raise ValueError("Invalid compressed code: {}".format(code))

        decompressed_data.append(entry)

        dictinory[next_code] = current_string + entry[0]
        next_code += 1

        current_string = entry
    return ''.join(decompressed_data)

def main():
    while True:
        print("\n===== LZW Compression System =====")
        print("1. Compress")
        print("2. Decompress")
        print("3. Exit")

        choice = input("Choose an operation: ")

        if choice == "1":
            text = input("Enter the string to compress: ")
            compressed = LZW_compress(text)
            print("Compressed data:", compressed)

        elif choice == "2":
            try:
                codes = list(map(int, input(
                    "Enter compressed codes separated by spaces: "
                ).split()))

                decompressed = LZW_decompress(codes)
                print("Decompressed data:", decompressed)

            except (ValueError, IndexError) as error:
                print("Error:", error)

        elif choice == "3":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
