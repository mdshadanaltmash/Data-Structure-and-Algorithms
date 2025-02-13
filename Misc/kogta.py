# a = [1, 2, -1, 3, 5, 7, -2, 7, -1]
#
# f_max = s_max = float('-inf')
#
# for num in a:
#     if num > f_max:
#         s_max = f_max
#         f_max = num
#     elif num > s_max and num < f_max:
#         s_max = num
#
# print(s_max)
#
# # max_e = max(a)
# #
# # print([num for num in a if num < max_e])
#
# # a.sort()
# l1 = set(a)
# l1 = list(l1)
# l1.sort()
# print(l1[-2])
#
#
#
# d = [{'name': 'Homer', 'age': 39}, {'name': 'Bart', 'age': 10}, {'name': 'Hummer', 'age': 14}]
#
#
# class Student:
#     def __init__(self):
#         self.data = []
#
#     def show_age_wise(self):
#         print(self.data)
#
#     def add_student(self, name, age):
#         details = {'name': name, 'age': age}
#         if self.data == []:
#             self.data.append(details)
#         else:
#             found = False
#             for i, student in enumerate(self.data):
#                 if student['age']>age:
#                     self.data.insert(i, details)
#                     found = True
#                     break
#             if not found:
#                 self.data.append(details)
#
#
# obj = Student()
# for items in d:
#     obj.add_student(items['name'], items['age'])
#
# obj.show_age_wise()
#

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"name: {self.name}, age: {self.age}"


d = [{'name': 'Homer', 'age': 39}, {'name': 'Bart', 'age': 10}, {'name': 'Hummer', 'age': 14}]

objects = [Person(person['name'], person['age']) for person in d]
objects = sorted(objects, key=lambda x: x.age)

print(objects)



# print(objects[0].age)
# print(objects[0].name)
# for i in range(len(objects)):
#     for j in range(i, len(objects)):
#         if objects[i].age > objects[j].age:
#             objects[i], objects[j] = objects[j], objects[i]
# objects.sort()



#
# create table emp(
#     name varchar2(50),
#     age number,
#     date_of_birth date,
#     salary number,
#     department VARCHAR2(100)
# );
#
# Select * from emp
# where
# salary > 50000 and department = 'HR';
#
# select * from emp where salary > (
# select avg(salary) from emp
# );
#
#
# NBFC
# loan
# big tech team (internal tech team and product)
# anuj kumar


















