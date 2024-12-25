from dataclasses import dataclass, field

# 1. Mahsulot ma'lumotlari
@dataclass
class Product:
    name: str
    price: float = field(default=0.0)
    availability: bool = True

    def set_price(self, new_price: float):
        if new_price > 0:
            self.price = new_price
        else:
            raise ValueError("Narx faqat ijobiy qiymat bo'lishi mumkin.")

@dataclass
class ElectronicProduct(Product):
    warranty: int = 0


product = Product(name="Telefon", price=1000, availability=True)

product.set_price(1200)
print(product)

laptop = ElectronicProduct(name="Laptop", price=3000, availability=True, warranty=24)
print(laptop)

# 2. Transport vositalari
@dataclass
class Vehicle:
    brand: str
    speed: float = 0.0

    def increase_speed(self, increment: float):
        if self.speed + increment <= 300:
            self.speed += increment
        else:
            raise ValueError("Tezlik 300 km/soatdan oshmasligi kerak.")

@dataclass
class Car(Vehicle):
    fuel_type: str = "Benzin"

@dataclass
class Bicycle(Vehicle):
    brake_type: str = "Disk tormoz"

car = Car(brand="Toyota", speed=200, fuel_type="Benzin")

car.increase_speed(50)
print(car)

bike = Bicycle(brand="Giant", speed=20, brake_type="Disk tormoz")
bike.increase_speed(10)
print(bike)

# 3. Kitoblar kutubxonasi
@dataclass
class Book:
    title: str
    author: str
    price: float

    def set_price(self, new_price: float, is_admin: bool):
        if is_admin:
            self.price = new_price
        else:
            raise PermissionError("Faqat admin narxni o'zgartirishi mumkin.")

@dataclass
class EBook(Book):
    file_size: float = 0.0

@dataclass
class PrintedBook(Book):
    paper_type: str = "Matli"

book = Book(title="Python dasturlash", author="Avazbek", price=50)
book.set_price(60, is_admin=True)
print(book)

ebook = EBook(title="Python E-Book", author="Avazbek", price=30, file_size=15.5)
printed_book = PrintedBook(title="Python Guide", author="Avazbek", price=40, paper_type="Matli")
print(ebook)
print(printed_book)

# 4. Ishchilar ro'yxati
@dataclass
class Employee:
    name: str
    position: str
    salary: float

    def increase_salary(self, increment: float, is_director: bool):
        if is_director:
            self.salary += increment
        else:
            raise PermissionError("Faqat direktor maoshni oshirishi mumkin.")

@dataclass
class Manager(Employee):
    team_size: int = 0

    def manage_team(self):
        return f"{self.name} {self.team_size} kishilik jamoani boshqaradi."

@dataclass
class Developer(Employee):
    programming_language: str = "Python"

    def write_code(self):
        return f"{self.name} {self.programming_language}da kod yozmoqda."

employee = Employee(name="Rustam", position="Developer", salary=5000)
employee.increase_salary(1000, is_director=True)
print(employee)

manager = Manager(name="Aziz", position="Manager", salary=7000, team_size=10)
developer = Developer(name="Jasur", position="Developer", salary=6000, programming_language="Python")

print(manager.manage_team())
print(developer.write_code())

# 5. Sportchilar
@dataclass
class Athlete:
    name: str
    sport: str
    records: dict

    def update_record(self, record_name: str, new_value, check_record: bool):
        if check_record:
            self.records[record_name] = new_value
        else:
            raise PermissionError("Faqat yangi natijalar bilan almashtirish mumkin.")

@dataclass
class Runner(Athlete):
    max_distance: float = 0.0

    def run(self, distance: float):
        return f"{self.name} {distance} km yugurdi."

@dataclass
class Swimmer(Athlete):
    pool_length: float = 0.0

    def swim(self, laps: int):
        return f"{self.name} {laps} marta {self.pool_length} metrlik havzada suzdi."

athlete = Athlete(name="Bobur", sport="Yugurish", records={"100m": "10s"})

athlete.update_record("100m", "9.8s", check_record=True)
print(athlete)

runner = Runner(name="Islom", sport="Yugurish", records={"Marafon": "2 soat"}, max_distance=42)
swimmer = Swimmer(name="Aziza", sport="Suzish", records={"50m": "25s"}, pool_length=25)

print(runner.run(10))
print(swimmer.swim(20))
