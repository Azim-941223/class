class Factory:
    def engine(self):
        return "Двигатель создан"

    
    def bridge(self):
        return "Ходовая часть создана"

class Toyota(Factory):
    def wheels(self):
        return "Колеса созданы"

    
    def windows(self):
        return "Стекла созданы"


car = Toyota()
method_list = [car.wheels(),car.windows(),car.engine(),car.bridge()]
print(method_list)