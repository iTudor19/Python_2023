def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib[:n]

def prim(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_prim(numbers):
    return [num for num in numbers if prim(num)]

def list_operations(a, b):
    intersection = list(set(a) & set(b))
    union = list(set(a) | set(b))
    diff_a_b = list(set(a) - set(b))
    diff_b_a = list(set(b) - set(a))
    return intersection, union, diff_a_b, diff_b_a

def compose(musical_notes, moves, start_position):
    song = []
    current_position = start_position
    for move in moves:
        current_position = (current_position + move) % len(musical_notes)
        song.append(musical_notes[current_position])
    return song

def under_diagonal(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if j < i:
                matrix[i][j] = 0
    return matrix

def x_times(x, *lists):
    combined_list = sum(lists, [])
    result = [item for item in combined_list if combined_list.count(item) == x]
    return list(set(result))

def palindrom(n):
    return str(n) == str(n)[::-1]

def max_palindrom(numbers):
    palindromes = [num for num in numbers if palindrom(num)]
    return len(palindromes), max(palindromes)

def char_lists(x=1, strings=[], flag=True):
    if flag:
        return [[char for char in string if ord(char) % x == 0] for string in strings]
    else:
        return [[char for char in string if ord(char) % x != 0] for string in strings]

def blocked(matrix):
    blocked_ct = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if any(matrix[row][j] > matrix[i][j] for row in range(i + 1, len(matrix))):
                blocked_ct.append((i, j))
    return blocked_ct

def swaps(*lists):
    max_length = max(len(lst) for lst in lists)
    zipped_list = []
    for i in range(max_length):
        zipped_list.append(tuple(lst[i] if i < len(lst) else None for lst in lists))
    return zipped_list


def order_by_third_char(tuples):
    return sorted(tuples, key=lambda x: x[1][2] if len(x[1]) > 2 else 0)

def ordonare(words):
    groups = []
    while words:
        current_word = words[0]
        current_group = [current_word]
        words = words[1:]
        for word in words[:]:
            if word[-2:] == current_word[-2:]:
                current_group.append(word)
                words.remove(word)
        groups.append(current_group)
    return groups
