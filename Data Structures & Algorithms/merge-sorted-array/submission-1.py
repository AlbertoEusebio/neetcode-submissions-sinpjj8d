class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j=m-1

        if n==0:
            return

        
        while j >= 0:
            nums1[j+n] = nums1[j]
            nums1[j] =0
            j-=1

        print(nums1)

        j=n
        i=0
        k=0

        while i<n and j<m+n:
            if nums2[i] < nums1[j]:
                nums1[k] = nums2[i]
                i+=1
            else:
                nums1[k] = nums1[j]
                j+=1
            k+=1
        while i<n:
            nums1[k] = nums2[i]
            k+=1
            i+=1

        while j<m+n:
            nums1[k] = nums1[j]
            k+=1
            j+=1
        
