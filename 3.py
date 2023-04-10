class FlatIterator:

    def __init__(self, list_of_lists):
        self.list_of_lists = list(reversed(list_of_lists))

    def __iter__(self):
        return self

    def __next__(self):
        if not self.list_of_lists:
            raise StopIteration
        if isinstance(self.list_of_lists[-1], list):
            last_element = list(reversed(self.list_of_lists.pop()))
            self.list_of_lists += last_element
            return self.__next__()
        return self.list_of_lists.pop()


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()
