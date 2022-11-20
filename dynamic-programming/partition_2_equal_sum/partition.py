import unittest
from functools import lru_cache
import random

def can_partition(numbers: list[int]) -> bool:
    """ 
    Search for a subset of numbers[:index] that sums to target_sum 
    O(n*S), S=sum(numbers)/2, n=len(numbers) 

    @type index: int
    @param index: the index to start the subrange within the numbers list

    @type target_sum: int
    @param target_sum: the current target sum, if 0 it means we reached the target

    @rtype: bool
    @return: Return True if the target sum can be reached or if target_sum is 0, False otherwise
    """  
    @lru_cache(maxsize=None)
    def find_partitions(index: int, target_sum: int) -> bool:
        if target_sum == 0:
            return True
        
        if target_sum < 0 or index >= len(numbers):
            return False
        
        number = numbers[index]

        return find_partitions(index + 1, target_sum - number) or find_partitions(index + 1, target_sum)
        
    total = sum(numbers)

    if total % 2:
        return False

    return find_partitions(0, total//2)

class TestPartitions(unittest.TestCase):
    def test_basic(self):
        self.assertTrue(can_partition([2, 6, 5, 3]))
        self.assertFalse(can_partition([2, 6, 5, 3, 1]))
        self.assertFalse(can_partition([2, 6, 5, 4]))
        self.assertTrue(can_partition([1] * 50))
        half = [random.randint(0, 100) for x in range(25)]
        entire = half + half
        random.shuffle(entire)
        self.assertTrue(can_partition(entire))

unittest.main()