class Zoo:
    pass
zoo_object = Zoo()
zoo_object.animal_1 = 'Тигр'
zoo_object.animal_2 = 'Бегемот'
zoo_object.animal_3 = 'Жираф'
zoo_object.animal_1 = 'Лев'
zoo_object.animal_4 = [zoo_object.animal_2,zoo_object.animal_3]
zoo_object.animal_3 = 'Змея'
print(list(zoo_object.__dict__.values()))