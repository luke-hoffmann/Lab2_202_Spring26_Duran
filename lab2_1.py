
def search(nums:list[int],idx:int = 0, target:int= -1)->int:
    #idx isn't used in this implentation but you will need it for recursive
    #convert to recursive
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

def recursive_search(nums: list[int], idx: int = 0, target:int=-1)->int:
    if (idx >= len(nums)): return -1
    if(nums[idx] == target): return idx
    return recursive_search(nums, idx+1, target)