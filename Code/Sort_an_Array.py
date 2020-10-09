class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(A):
            LA = len(A)
            if LA == 1: return A
            LH, RH = mergeSort(A[: LA//2]), mergeSort(A[LA//2:])
            return merge(LH, RH)
        
        def merge(LH, RH):
            LLH, LRH = len(LH), len(RH)
            S, i, j = [], 0, 0
            while i < LLH and j < LRH:
                if LH[i] <= RH[j]:
                    S.append(LH[i])
                    i += 1
                else:
                    S.append(RH[j])
                    j += 1
            
            return S + (RH[j:] if i == LLH else LH[i:])
        
        return mergeSort(nums)