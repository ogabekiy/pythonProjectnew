class Book():
    def __init__(self,name,author,year):
        self.year = year
        self.author = author
        self.name = name

class Book_store(Book):
    def __init__(self,name,author,year,price):
        super().__init__(name,author,year)
        self.price = price
    def reduce(self):
        if 2024 - int(self.year) >= 5:
            self.price = (int(self.price) / 10) * 8
            print(f" narx 20% ga kamaydi {self.price}")
        else:
            print(f" narx ozgarmadi {self.price}")
print("har bir kitobni har bir qatorda name author year va priceni probel bn kiriting")


for i in range(5):
    b = input().split()
    book = Book_store(b[0], b[1], b[2], b[3])
    book.reduce()


# molxona jorj 2023 48000
# atomodatlar james 2020 72000
# harry opoter 2007 56000
# alhimik asd 2010 40000
# godfather mar 2000 96000






