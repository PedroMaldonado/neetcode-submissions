from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    count_chars = {}
    
    for letter in word:
        if letter not in count_chars:
                count_chars[letter] = 1
        else:
            count_chars[letter] += 1

    return count_chars


# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
