
def count_group(string: str) -> list:
    if not string:
        return []
    counter = 0
    group = []
    temp = string[0]
    for index, s in enumerate(string):
        if temp == s:
            counter += 1
        else:
            group.append((temp, counter))
            counter = 1
        temp = s
    else:
        group.append((temp, counter))

    return group

def test_short_string():
    assert count_group('') == []
    assert count_group('a') == [('a', 1)]
    assert count_group('aaaabbbcca') == [('a', 4), ('b', 3), ('c', 2), ('a', 1)]
