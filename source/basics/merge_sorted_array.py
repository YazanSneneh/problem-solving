from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    length = m+n
    nums1 = nums1[0:m]
    nums2 = nums2[0:n]

    if m == 0:
        return nums2[0:n]

    if n== 0:
        return nums1[0:m]

    for i in range(length-2):
        if i<m:
            nums1.insert(i, nums2[i-1])
        elif i>= m:
            nums1.append(nums2[m:])
    return sorted(nums1)


nums1=[1, 2, 3, 0, 0, 0]
nums2 = [2, 3]
rsult = merge(nums1, 3, nums2, 2)

print(rsult)