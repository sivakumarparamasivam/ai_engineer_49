# role = input("Enter your role (admin/user/guest): ")
# match role:
#     case "admin":
#         print("You have full access.")
#     case "user":        
#         print("You have limited access.")
#     case "guest":
#         print("You have guest access.")
#     case default:
#         print("Invalid role.")   

# number =(10,20,30,40,50)
# print(number)
# # print(number[0])
# # print(number[3: : 2])
# # print(number[-2:])
# print(number[::-1])
# print(number[::-2])
# print(number[::-3])
# print(number[-1:-3: -2])

marks = [78,85,62,90,55,88]
for mark in marks:
    if mark >= 75:
        print(mark, "Distinction")
max_marks = max(marks)
print("Highest Marks", max_marks)
min_marks = min(marks)
print("Lowest Marks" ,min_marks)
average_marks = sum(marks)/len(marks)
print("Average Marks" ,average_marks)
marks.append(95)
print("After Appended '95' Mark", marks)
marks.remove(55)
print("After Removed '55' Mark", marks)
marks.sort()
print("Sorted" , marks)
marks.reverse()
print("Reverse Order" , marks)



















