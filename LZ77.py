from dataclasses import dataclass

@dataclass 
class Tag:
    offset: int
    length: int
    next_char: str

def lz77_compress(word):
    i=0
    tags = []
    while i < len(word):
        offset = 0
        length = 0
        next_char = ''
        search_start = max(0, i - 255)

        while i < len(word):
            j = i -1
            longest_len = 0 
            farest_pos = 0

            while j >= search_start:
                k = 0
                while (i + k < len(word)) and (word[j + k] == word[i + k]):
                    k += 1
                if k > longest_len:
                    longest_len = k
                    farest_pos = j
                j -= 1

            if longest_len > 0:
                offset = i - farest_pos
                length = longest_len
                next_char = word[i + longest_len] if (i + longest_len) < len(word) else ''
                tags.append(Tag(offset, length, next_char))
                i += longest_len + 1
            else:
                next_char = word[i]
                tags.append(Tag(0, 0, next_char))
                i += 1
    return tags


