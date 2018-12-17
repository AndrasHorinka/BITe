def convert_dict_in_lists_to_list(expandabe_list):
    array = list()
    for dictionary in expandabe_list:
        for key, value in dictionary.items():
            array.append(value)
    return array