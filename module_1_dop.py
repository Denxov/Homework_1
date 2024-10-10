# Вычисление среднего балла на лету
def __avg__(l:list):
  return sum(l)/len(l)
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_=list(students)
grades_=list(grades)
students_.sort()
print(students_)
students_=dict(zip(students_,grades))
stud=input('Студент? ')
while(students_.get(stud)!=None):
    print('Средний балл: ',sum(students_[stud])/students_[stud].__len__())
    stud = input('Студент? ')
# Словарь имя: средний балл
grades_avg=list(map(__avg__,grades_))
students_avg=dict(zip(students_,grades_avg))
print(students_avg)