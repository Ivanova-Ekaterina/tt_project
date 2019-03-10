def compare_json_data(source_data_a, source_data_b):
    def compare(data_a, data_b):
        if type(data_a) is list:
            if (
                    (type(data_b) != list) or
                    (len(data_a) != len(data_b))
            ):
                return False
            used_index = []
            for list_index, list_item in enumerate(data_a):
                tmp = 0
                for i in range(len(data_a)):
                    if compare(list_item, data_b[i]) and (not i in used_index):
                        tmp = tmp + 1
                        used_index.append(i)
                        break
                if tmp == 0:
                    return False
            return True
        if type(data_a) is dict:
            if type(data_b) != dict:
                return False
            for dict_key, dict_value in data_a.items():
                if (
                        (dict_key not in data_b) or
                        (not compare(dict_value, data_b[dict_key]))
                ):
                    return False
            return True
        return (
                (data_a == data_b) and
                (type(data_a) is type(data_b))
        )

    return (
            compare(source_data_a, source_data_b) and
            compare(source_data_b, source_data_a)
    )
