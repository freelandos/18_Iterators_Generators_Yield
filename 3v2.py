from collections import deque


class FlatIterator:

    def __init__(self, list_of_lists):
        self.list_of_lists = deque(list_of_lists)

    def __iter__(self):
        return self

    def __next__(self):
        if not self.list_of_lists:
            raise StopIteration
        if isinstance(self.list_of_lists[0], list):
            self.list_of_lists = deque(self.list_of_lists.popleft()) + self.list_of_lists
            return self.__next__()
        return self.list_of_lists.popleft()


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
