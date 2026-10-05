from dataclasses import dataclass

@dataclass 
class Tag:
    offset: int
    length: int
    next_char: str

def lz77_compress(word, search_size=255):
    tags = []
    i = 0
    
    while i < len(word):
        search_start = max(0, i - search_size)
        best_offset = 0
        best_length = 0
        
        # جرّب كل بوزيشن في الـ search buffer
        for j in range(search_start, i):
            k = 0
            # اسمح بالـ overlap (زي الـ PDF) — لو مش عايزه ضيف: j + k < i
            while (i + k < len(word)) and (word[j + k] == word[i + k]):
                k += 1
            
            if k > best_length:
                best_length = k
                best_offset = i - j
        
        # لو لقينا match
        if best_length > 0:
            next_char = word[i + best_length] if (i + best_length) < len(word) else ''
            tags.append(Tag(best_offset, best_length, next_char))
            i += best_length + (1 if next_char else 0)
        else:
            tags.append(Tag(0, 0, word[i]))
            i += 1
    
    return tags


def lz77_decompress(tags):
    decompressed = []
    for tag in tags:
        if tag.offset == 0 and tag.length == 0:
            decompressed.append(tag.next_char)
        else:
            start = len(decompressed) - tag.offset
            for k in range(tag.length):
                decompressed.append(decompressed[start + k])
            if tag.next_char:
                decompressed.append(tag.next_char)
    return ''.join(decompressed)


def print_tags(tags):
    for tag in tags:
        print(f"({tag.offset}, {tag.length}, '{tag.next_char}')")


def main():
    word = input("Enter a string to compress: ")
    tags = lz77_compress(word)
    print("Compressed tags:")
    print_tags(tags)

    decompressed = lz77_decompress(tags)
    print("Decompressed string:", decompressed)
    print("Compression successful:", decompressed == word)


if __name__ == "__main__":
    main()