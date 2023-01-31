_dict = [
    {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": {
            "sub_a": "a",
            "sub_b": "b",
            "sub_c": "c"
        }
    },
    {
        "a": 4,
        "b": 5,
        "c": 6,
        "d": {
            "sub_a": "a",
            "sub_b": "b",
            "sub_c": "c"
        }
    },
    {
        "a": 7,
        "b": 8,
        "c": 9,
        "d": {
            "sub_a": "a",
            "sub_b": "b",
            "sub_c": "c"
        }
    }
]

for i in _dict:
    ad = {
        "a": i['a'],
        "b": i['b'],
        "c": i["c"],
        **{j: i['d'][j] for j in i['d']}
    }
    print(ad)
    # or new_list.append(ad)
