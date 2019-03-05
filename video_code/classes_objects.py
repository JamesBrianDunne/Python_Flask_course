
lottery_player_dict = {
    'name': 'Rolf',
    'numbers': (5, 9, 12, 3, 1, 21)
}

class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_items(self, name, price):
        item = {"name": name, "price": price}
        self.items.append(item)

    def stock_price(self):
        return sum(item["price"] for item in self.items)


class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks)/len(self.marks)

    @classmethod
    def go_to_school(cls):
        print("I'm heading to School!")

    @staticmethod
    def go_home():
        print("I'm heading home!")


anna = Student("Anna", "MIT")
anna.marks.append(56)
anna.marks.append(71)

# print(anna.go_to_school())

print(anna.average())

Student.go_to_school()
Student.go_home()


class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_tems(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    @classmethod
    def franchise(cls, store):
        return Store(store.name + " - franchise")

    @staticmethod
    def store_details(store):
        return '{}, total stock price: {}'.format(store.name, int(store.stock_price()))

