from batch import batches
from itertools import chain

def test_batch_on_list():
    assert list(batches([1, 2, 3, 4, 5, 6], 1)) == [
        [1], [2], [3], [4], [5], [6]
    ]
    assert list(batches([1, 2, 3, 4, 5, 6], 2)) == [
        [1, 2], [3, 4], [5, 6]
    ]
    assert list(batches([1, 2, 3, 4, 5, 6], 3)) == [
        [1, 2, 3], [4, 5, 6]
    ]
    assert list(batches([1, 2, 3, 4, 5, 6], 4)) == [
        [1, 2, 3, 4], [5, 6],
    ]

def test_batch_order():
    """
    Ensures that the order of elements in batches is the same as in the source iterable
    """
    iterable = range(100)
    batch_size = 2
    output = batches(iterable, batch_size)
    assert list(chain.from_iterable(output)) == list(iterable)

def test_batch_sizes():
    """
     ensures that all batches have the same size
    """
    iterable = range(100)
    batch_size = 2
    output = list(batches(iterable, batch_size))
    for batch in output[:-1]:
        assert len(batch) == batch_size
    assert len(output[-1]) <= batch_size
