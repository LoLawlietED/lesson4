grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(students)
gradesAVE = [sum(grades[0][0:])/len(grades[0]),sum(grades[1][0:])/len(grades[1]),sum(grades[2][0:])/len(grades[2]),sum(grades[3][0:])/len(grades[3]),sum(grades[4][0:])/len(grades[4])]
dict = dict(zip(students, gradesAVE))
print(dict)
