class Room():
    def __init__(self, lenght, height, widgth):
        self.widgth = widgth
        self.height = height
        self.lenght = lenght
        self.cnt = 0
    def win(self):
        while True:
            if (self.height >= 2 or self.widgth) and (self.lenght >= 15):
                if self.height >= 2:
                    self.height -= 2
                    self.cnt += 1
                if self.widgth >= 2:
                    self.widgth -= 2
                    self.cnt += 1
            else:
                break

        return (f"{2 * self.cnt}")
print("har bir xona malumotlarini bir qatorda balandlik bo'y enini kiriting")
for i in range(5):
    xona = input().split()
    a = Room(xona[0], xona[1], xona[3])
    print("oynalar soni: -> ", a.win())