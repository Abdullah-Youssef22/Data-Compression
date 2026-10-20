from LZ77 import LZ77


class Program:
    def __init__(self):
        self.__status = True
        self.__lz77 = LZ77("")

    def run(self):
        print("LZ77 COMPRESSION ALGORITHM.... \n")
        while self.__status:
            text = input("Enter the text you want to compress : ")
            self.__lz77.putText(text)
            self.__lz77.compress()
            self.__lz77.deCompress()
            self.__lz77.printResult()


            question = input("Another compressed text ? [Y/N]")
            if question == "Y" or question == "y":
                continue
            else:
                self.__status = False




