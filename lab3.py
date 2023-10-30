def operations_with_lists(a, b):
    return [set(a) & set(b), set(a) | set(b), set(a) - set(b), set(b) - set(a)]

def character_occurrences(text):
    char_dict = {}
    for char in text:
        char_dict[char] = char_dict.get(char, 0) + 1
    return char_dict

def compare_dictionaries(dict1, dict2):
    if dict1.keys() != dict2.keys():
        return False
    for key in dict1.keys():
        if type(dict1[key]) != type(dict2[key]):
            return False
        if isinstance(dict1[key], dict):
            if not compare_dictionaries(dict1[key], dict2[key]):
                return False
        elif dict1[key] != dict2[key]:
            return False
    return True

def build_xml_element(tag, content, **kwargs):
    attributes = " ".join([f'{key}="{value}"' for key, value in kwargs.items()])
    return f"<{tag} {attributes}>{content}</{tag}>"

def validate_dict(rules, dictionary):
    for key, prefix, middle, suffix in rules:
        if key not in dictionary:
            return False
        value = dictionary[key]
        if not value.startswith(prefix) or not value.endswith(suffix) or middle not in value[len(prefix):-len(suffix)]:
            return False
    return True

def count_unique_duplicates(lst):
    unique_elements = len(set(lst))
    duplicate_elements = len(lst) - unique_elements
    return unique_elements, duplicate_elements

def set_operations(*sets):
    operations_dict = {}
    for i in range(len(sets)):
        for j in range(i + 1, len(sets)):
            a = sets[i]
            b = sets[j]
            operations_dict[f"{a} | {b}"] = a.union(b)
            operations_dict[f"{a} & {b}"] = a.intersection(b)
            operations_dict[f"{a} - {b}"] = a.difference(b)
            operations_dict[f"{b} - {a}"] = b.difference(a)
    return operations_dict

def loop(mapping):
    result = []
    visited = set()
    current_key = mapping['start']
    while current_key not in visited:
        result.append(current_key)
        visited.add(current_key)
        current_key = mapping[current_key]
    return result

def my_function(*args, **kwargs):
    return sum(1 for arg in args if arg in kwargs.values())
