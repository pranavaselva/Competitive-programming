class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        elements = {}
        stack = []
        for i in nums2:
            while stack and stack[-1] < i:
                small = stack.pop()
                elements[small] = i
            stack.append(i)

        while stack:
            elements[stack.pop()] = -1
        
        return [elements[i] for i in nums1]