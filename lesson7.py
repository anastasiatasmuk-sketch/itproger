# # Списки з даними
# nums = [5,4,3,2,1]
# nums[2] = 34.8
# # print(nums[3])
#
# nums2 = [5, 7, 8, 9, [10, 11, 12, 13]]
# # print(nums2[-1][1])
#
# nums.append(45)
# nums.insert(1, False) #False=0 True=1
# # nums.extend(nums2)
# nums.sort()
# nums.reverse()
# # nums.pop()
# nums.remove(4)
#
# print(nums.count(45))
# print(nums)
# print(len(nums))

#Списки та цикли
# nums = [1,2,3,4,5,6,7,8,9]
#
#
# for el in nums:
#     res = el ** 2
#     print(res)

#Практичне використання
user_count_hobby = int(input("Enter the number of hobby: "))

i = 0
hobby = []
while i < user_count_hobby:
    text = "Enter hobby " + str(i +1) + ": "
    hobby.append(input(text))

    i += 1

print(hobby)


