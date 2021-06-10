# 1)Student
# Создайте класс Student, конструктор которого имеет параметры name, lastname,
# department, year_of_entrance. Добавьте метод get_student_info, который
# возвращает имя, фамилию, год поступления и факультет в
# отформатированном виде: “Вася Иванов поступил в 2017 г. на факультет:
# Программирование.”

class Student:
    def __init__(self, name, lastname, departmant, year_of_entrance):
        self.__name = name
        self.__lastname = lastname
        self.__department = departmant
        self.__year_of_entrance = year_of_entrance

    def get_student_info(self):
        print(self.__name,self.__lastname)