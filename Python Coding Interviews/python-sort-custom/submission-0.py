from typing import List

def get_word_length(word: str) -> int:
    return len(word)

def sort_words(words: List[str]) -> List[str]:
    sorted_words = []

    while words:
        max_val = words[0]

        for i in range(len(words)):
            if get_word_length(words[i]) > get_word_length(max_val):
                max_val = words[i]

        sorted_words.append(max_val)
        words.remove(max_val)

    return sorted_words


def sort_numbers(numbers: List[int]) -> List[int]:
    sorted_numbers = []
    
    while numbers:
        min_val = numbers[0]
    
        for i in range(len(numbers)):
            if abs(numbers[i]) < abs(min_val):
                min_val = numbers[i]
    
        sorted_numbers.append(min_val)
        numbers.remove(min_val)

    return sorted_numbers


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))