class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) == 0:
            return 0
        return self.selection(nums, 0, len(nums)-1, len(nums)-k)
    
    def selection(self, nums, l, r, k):
        if l == r:
            return nums[l]

        # select a random pivot_index
        pivot_index = random.randint(l, r)

        # find the pivot position in a sorted list
        pivot_index = self.partition(nums, l, r, pivot_index)
        
        # the pivot is in its final sorted position
        if k == pivot_index:
            return nums[k]
        elif k < pivot_index:
            return self.selection(nums, l, pivot_index-1, k)
        else:
            return self.selection(nums, pivot_index+1, r, k)
    
    def partition(self, nums, l, r, pivot_index):
        pivot = nums[pivot_index]
        # move pivot to end
        nums[pivot_index], nums[r] = nums[r], nums[pivot_index]  
        # move all smaller elements to the left
        store_index = l
        for i in range(l, r):
            if nums[i] < pivot:
                nums[store_index], nums[i] = nums[i], nums[store_index]
                store_index += 1
        # move pivot to its final place
        nums[r], nums[store_index] = nums[store_index], nums[r] 
        
        return store_index

class Solution2:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Sort the array and take the number in reverse order
        return sorted(nums)[-k]