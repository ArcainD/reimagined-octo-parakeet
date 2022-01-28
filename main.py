nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

nested_list2 = [
    ['a', 'b', 'c', [3, 4, 6, 78, ['FA', 'fs']]],
    ['d', 'e', 'f', 'h', False, [['dfhg', [23]], 'erg', ['rg']], 'aegf'],
    [1, 2, None],
]


class FlatIterator:

    def __init__(self, nested_list):
        self.nested_list = nested_list
        self.outer_list_index = 0
        self.inner_list_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.outer_list_index < len(nested_list):
            if self.inner_list_index < \
                    len(nested_list[self.outer_list_index]) - 1:
                res = nested_list[self.outer_list_index][self.inner_list_index]
                self.inner_list_index += 1

            else:
                res = nested_list[self.outer_list_index][self.inner_list_index]
                self.outer_list_index += 1
                self.inner_list_index = 0
            return res
        else:
            raise StopIteration


def flat_generator(nested_list):
    for item in nested_list:
        for i in item:
            yield i

    # gen = (i for item in nested_list for i in item)
    # return gen


def flat_generator2(nested_list):
    for item in nested_list:
        if type(item) == list:
            for x in flat_generator2(item):
                yield x
        else:
            yield item


if __name__ == '__main__':

    for i in FlatIterator(nested_list):
        print(i)
    print('')

    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)
    print('')

    for i in flat_generator(nested_list):
        print(i)
    print('')

    for i in flat_generator2(nested_list2):
        print(i)
