
def first_unique_char(s):
    freq_map = {}  # character: count
    # Step 1: Count frequency of each character
    for char in s:
        freq_map[char] = freq_map.get(char, 0) + 1
    # Step 2: Find the first character with count = 1
    for index, char in enumerate(s):
        if freq_map[char] == 1:
            return index
    return -1


