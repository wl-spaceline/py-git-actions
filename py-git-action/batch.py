from typing import Any, Iterable, List
# def batches(iterable: Iterable[Any], batch_size: int) -> Iterable[List[Any]]:
#     batch = []
#     for item in iterable:
#         batch.append(item)
#         if len(batch) == batch_size:
#             yield batch
#             batch = []
#     if batch:
#         yield batch
#    return results

from itertools import islice
def batches(iterable: Iterable[Any], batch_size: int) -> Iterable[List[Any]]:
    iterator = iter(iterable)
    while True:
        batch = list(islice(iterator, batch_size))
        if not batch:
            return
        yield batch
