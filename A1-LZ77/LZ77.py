class Token:
    def __init__(self, goBack, length, nextChar):
        self.goBack = goBack
        self.length = length
        self.nextChar = nextChar

    def __repr__(self):
        return f"({self.goBack}, {self.length}, {self.nextChar!r})"

class LZ77:

    def __init__(self, text):
        self.__decompressed = None
        self.__compressed = None
        self.__string = text

    def putText(self, text):
        self.__string = text

    def compress(self, windowSize=10):
        res: list[Token] = []
        cursor = 0

        while cursor < len(self.__string):
            bestLength = 0
            bestGoBack = 0

            start = max(0, cursor - windowSize)

            for cand in range(start, cursor):
                length = 0

                while (
                        cursor + length < len(self.__string)
                        and self.__string[cand + length] == self.__string[cursor + length]
                ):
                    length += 1

                if length > bestLength:
                    bestLength = length
                    bestGoBack = cursor - cand

            nextChar = "\0"

            if cursor + bestLength < len(self.__string):
                nextChar = self.__string[cursor + bestLength]

            res.append(
                Token(
                    goBack=bestGoBack,
                    length=bestLength,
                    nextChar=nextChar
                )
            )

            cursor += bestLength + 1

        self.__compressed = res
        return res


    def deCompress(self):
        result = ""
        for token in self.__compressed:
            start = len(result) - token.goBack
            leng = token.length
            for i in range(start, start + leng):
                result += result[i]
            if token.nextChar != "\0":
                result += token.nextChar

        self.__decompressed = result
        return result


    def __getCompressedSize(self):
        if not self.__compressed:
            return 0

        maxP = max(token.goBack for token in self.__compressed)
        maxL = max(token.length for token in self.__compressed)

        positionBits = max(1, maxP.bit_length())
        lengthBits = max(1, maxL.bit_length())
        symbolBits = 8

        tagSize = positionBits + lengthBits + symbolBits

        numberOfTags = len(self.__compressed)
        compressedSize = numberOfTags * tagSize

        return compressedSize


    def __getSizeBeforeCompressed(self):
        return 8 * len(self.__string)


    def printResult(self):
        print("The result : \n")
        print("Compressed text:")
        for token in self.__compressed:
            print(token)

        print("Size before compressing : " + str(self.__getSizeBeforeCompressed()))
        print("Compressed size: " + str(self.__getCompressedSize()))
        print("Decompressed text : " + self.__decompressed + "\n")
        if self.__decompressed == self.__string:
            print("Status : True")
        else:
            print("Status : False")


