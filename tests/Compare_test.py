import CompareJSON

first = {'a': 1, 'b': 2, 'c': [1, 2, "a", [9, 7], "b", "b"]}
second = {'b': 2, 'a': 1, 'c': [2, 1, "b", "b", "a", [7, 9]]}

print (CompareJSON.compare_json_data(first, second))
