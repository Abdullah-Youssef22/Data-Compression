from dataclasses import dataclass
from unittest import result

@dataclass
class Tag:
    index: int
    next_char: str

class LZ78:
    def __init__(self, string):
        self.__string = string
        self.__compressed = []
        self.__decompressed = ""

    def compress(self):
        deictionary = {}
        cursor = 0
        res = []

        while cursor < len(self.__string):
            substring = ""
            index = 0
            while cursor < len(self.__string) and substring + self.__string[cursor] in deictionary:
                substring += self.__string[cursor]
                index = deictionary[substring]
                cursor += 1

            if cursor < len(self.__string):
                substring += self.__string[cursor]
                deictionary[substring] = len(deictionary) + 1
                res.append(Tag(index=index, next_char=self.__string[cursor]))
                cursor += 1
            else:
                res.append(Tag(index=index, next_char="\0"))

        self.__compressed = res
        return res
    
    def deCompress(self):
        dictionary = {}
        result = ""
        next_index = 1
    
        for tag in self.__compressed:
            substring = ""
    
            if tag.index > 0:
                substring = dictionary[tag.index]
    
            if tag.next_char != "\0":
                substring += tag.next_char
    
            result += substring
    
            if tag.next_char != "\0":
                dictionary[next_index] = substring
                next_index += 1
    
        self.__decompressed = result
        return result


def main():
    text = input("Enter the string to compress: ")
    lz = LZ78(text)

    while True:
        print("\n===== LZ78 Menu =====")
        print("1. Compress")
        print("2. Decompress")
        print("3. Exit")

        choice = input("Choose an operation: ")

        if choice == "1":
            compressed = lz.compress()
            print("\nCompressed Data:")
            for tag in compressed:
                print(tag)

        elif choice == "2":
            decompressed = lz.deCompress()
            print("\nDecompressed Data:")
            print(decompressed)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

