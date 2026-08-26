#мінімальний елемент
from ftplib import print_line


def minimal(l):
    min_num = l[0]
    for i in l[1:]:
        print_line(i)
        if i < min_num:
            min_num = i

    return min_num


nums1 = [5,  3, 9, 10, 12, 4, 7, 6]
res1 = minimal(nums1)

nums2 = [5, 3, 9, 10, 12, 4, 7, 6, -10]
res2 = minimal(nums2)

if res1 < res2:
    print(res1)
else:
    print(res2)
