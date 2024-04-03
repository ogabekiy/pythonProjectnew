class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

class Train(Time):
    def __init__(self, num_train, route, hour, minute, second):
        super().__init__(hour, minute, second)
        self.num_train = num_train
        self.route = route

# Poyezdlar ro'yxati
trains = []

# 5 ta poyezd malumotlarini kiritish
for i in range(5):
    print(f"Poyezd #{i + 1}")
    num_train = input("Poyezd raqamini kiriting: ")
    route = input("Poyezd yo'nalishini kiriting: ")
    hour = int(input("Jo'nash vaqti soatini kiriting: "))
    minute = int(input("Jo'nash vaqti daqiqasini kiriting: "))
    second = int(input("Jo'nash vaqti soniyasini kiriting: "))

    # Poyezd obyektini yaratish
    poyezd = Train(num_train, route, hour, minute, second)

    # Poyezd ro'yxatiga qo'shish
    trains.append(poyezd)

# Foydalanuvchi kiritgan poyezd raqami
poyezd_raqami = input("Qidirganiz poyezd raqamini kiriting: ")

# Foydalanuvchi kiritgan raqamga mos poyezdni topish
poyezd_topildi = False
for poyezd in trains:
    if poyezd.num_train == poyezd_raqami:
        poyezd_topildi = True
        current_time = Time(10, 0, 0)  # Hozirgi vaqtni o'rnating
        remaining_time = (poyezd.hour - current_time.hour) * 60 + (poyezd.minute - current_time.minute)
        print(f"{poyezd_raqami} raqamli poyezdga qolgan vaqt: {remaining_time} daqiqa")
        break

if not poyezd_topildi:
    print("Kechirasiz, kiritilgan raqamga mos poyezd topilmadi.")
