from abc import ABC, abstractmethod


class Food(ABC):
    @abstractmethod
    def get_nutrition(self):
        pass


class Sausage(Food):
    def get_nutrition(self):
        return "Calories, protein, fat"

    def get_color(self):
        return "Red"

    def get_expiration(self):
        return "2 weeks from Production"


class Cat:
    def __init__(self) -> None:
        self.energy = 0

    def eat(self, food: Food):
        print(f"Eating food with nutrition: {food.get_nutrition()}")
        self.energy += 100

my_cat = Cat()
my_sausage = Sausage()
my_cat.eat(my_sausage)