nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
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
    outer_index = 0
    inner_index = 0
    while outer_index < len(nested_list):
        if inner_index < len(nested_list[outer_index]):
            yield nested_list[outer_index][inner_index]
            inner_index += 1
        elif inner_index == len(nested_list[outer_index]):
            outer_index += 1
            inner_index = 0

if __name__ == '__main__':

    for i in FlatIterator(nested_list):
        print(i)
    print('===================================')

    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)
    print('===================================')

    for i in flat_generator(nested_list):
        print(i)


