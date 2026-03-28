#!/usr/bin/python
class TestImpl:
    def transform_employee_data(self, employees):
        emp_dict = {}

        for rec in employees:
            curr_rec = {'name': rec['name'], 'salary': rec['salary']}
            curr_dept = rec['department']
            emp_dict[curr_dept] = emp_dict.get(curr_dept, []).append(curr_rec)
            print(emp_dict)
            emp_dict[curr_dept] = sorted(emp_dict[curr_dept], key=lambda x: x['salary'])
        print(emp_dict)
        # if emp_dict:
        #     for key, val in emp_dict:
        #         emp_dict[key] = sorted(val, key=lambda x:x['salary'])

        return emp_dict


arr = [3, 4, 1, 3, 2]
k = 5

[3, 7, 8, 11, 13]
[13, 10, 6, 5, 2]



