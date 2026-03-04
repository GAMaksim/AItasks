# 7-Topshiriq (Amaliy qism)
# Supervised Learning: Regressiya va Klassifikatsiya

import math

# 3. Linear Regression - Uy narxini bashorat
print("=" * 55)
print("3. LINEAR REGRESSION — Uy narxini bashorat qilish")
print("=" * 55)

data = [
    {"area": 120, "price": 300_000_000},
    {"area": 150, "price": 450_000_000},
    {"area": 100, "price": 200_000_000},
    {"area": 200, "price": 500_000_000},
    {"area": 80,  "price": 180_000_000},
]

print("\nO'qitish ma'lumotlari:")
for d in data:
    print(f"  Maydon: {d['area']} m²  →  Narx: {d['price']:,} so'm")

areas = [d["area"] for d in data]
prices = [d["price"] for d in data]
n = len(areas)

sum_x = sum(areas)
sum_y = sum(prices)
sum_xy = sum(areas[i] * prices[i] for i in range(n))
sum_x2 = sum(x ** 2 for x in areas)

m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
b = (sum_y - m * sum_x) / n

print(f"\n  Formula: narx = {round(m):,} × maydon + {round(b):,}")

test_area = 160
prediction = m * test_area + b
print(f"\n  BASHORAT: {test_area} m2 uy narxi = {round(prediction):,} so'm")


# 4. Logistik regressiya - Spam aniqlash
print("\n" + "=" * 55)
print("4. LOGISTIK REGRESSIYA — Spam aniqlash")
print("=" * 55)

spam_data = [
    ([5,  0], 0),   # "Salom qalaysiz" — spam emas
    ([3,  0], 0),   # "Darsga keling" — spam emas
    ([50, 5], 1),   # "BUYURTMA BERING!!!" — spam
    ([40, 3], 1),   # "BEPUL PATTI!!!" — spam
    ([8,  0], 0),   # "Bugun uchrashamiz" — spam emas
    ([60, 7], 1),   # "MILLION YUTIB OLING" — spam
    ([4,  1], 0),   # "Havolani ko'ring" — spam emas
    ([45, 4], 1),   # "CHEGIRMA 90%!!!" — spam
]

def sigmoid(z):
    return 1 / (1 + math.exp(-z))

w1 = 0.05
w2 = 0.3
bias = -2.0

print(f"\n  {'So\\'zlar':^8} | {'Linklar':^8} | {'Haqiqiy':^8} | {'Ehtimol':^8} | {'Natija':^8}")
print(f"  {'-'*8}-+-{'-'*8}-+-{'-'*8}-+-{'-'*8}-+-{'-'*8}")

togri = 0
for features, label in spam_data:
    z = w1 * features[0] + w2 * features[1] + bias
    prob = sigmoid(z)
    pred = 1 if prob >= 0.5 else 0
    togri += (pred == label)
    status = "✅" if pred == label else "❌"
    print(f"  {features[0]:^8} | {features[1]:^8} | {label:^8} | {prob:^8.3f} | {status:^8}")

print(f"\n  Aniqlik: {togri/len(spam_data)*100:.0f}%")

print("\n  YANGI XABAR:")
for sozlar, linklar, matn in [(6, 0, "Bugun kutubxonaga boramiz"), (55, 6, "BEPUL TELEFON!!!")]:
    z = w1 * sozlar + w2 * linklar + bias
    natija = "SPAM" if sigmoid(z) >= 0.5 else "SPAM EMAS"
    print(f"  \"{matn}\" -> {natija}")


# 5. Fiat 500 Dataset - Regressiya
print("\n" + "=" * 55)
print("5. FIAT 500 DATASET — Narxni bashorat qilish")
print("=" * 55)

fiat = [
    {"yili": 2016, "km": 45000,  "narx": 8500},
    {"yili": 2018, "km": 25000,  "narx": 11000},
    {"yili": 2015, "km": 78000,  "narx": 6500},
    {"yili": 2019, "km": 15000,  "narx": 12500},
    {"yili": 2014, "km": 95000,  "narx": 5500},
    {"yili": 2017, "km": 55000,  "narx": 7800},
    {"yili": 2020, "km": 10000,  "narx": 14000},
    {"yili": 2013, "km": 110000, "narx": 4500},
    {"yili": 2016, "km": 62000,  "narx": 7000},
    {"yili": 2021, "km": 5000,   "narx": 15500},
]

print(f"\n  {'Yili':^5} | {'KM':^8} | {'Narx (€)':^10}")
print(f"  {'-'*5}-+-{'-'*8}-+-{'-'*10}")
for f in fiat:
    print(f"  {f['yili']:^5} | {f['km']:>8,} | {f['narx']:>10,}")

kms = [f["km"] for f in fiat]
prices = [f["narx"] for f in fiat]
n = len(kms)

sx = sum(kms)
sy = sum(prices)
sxy = sum(kms[i] * prices[i] for i in range(n))
sx2 = sum(x**2 for x in kms)

m = (n * sxy - sx * sy) / (n * sx2 - sx ** 2)
b = (sy - m * sx) / n

print(f"\n  Formula: narx = {round(m, 4)} × km + {round(b, 1)}")

print(f"\n  BASHORATLAR:")
for km in [20000, 50000, 80000, 120000]:
    print(f"  {km:>7,} km -> {round(m * km + b):,} evro")
