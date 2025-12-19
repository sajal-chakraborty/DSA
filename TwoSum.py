//define teh function   
def two_sum(nums, target):
    """
    Finds two numbers in the list that add up to the target sum.

    Args:
        nums (list of int): The input list of integers.
        target (int): The target sum.

    Returns:
        tuple: A tuple containing the indices of the two numbers that add up to the target sum.
               Returns None if no such pair exists.
    """
    num_map = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return (num_map[complement], i)
        num_map[num] = i
    
    return None
