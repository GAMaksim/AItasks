# 6-Topshiriq (Amaliy qism)
# Data and Features in Machine Learning

# 2. Yo'qolgan qiymatlarni aniqlash
print("=" * 55)
print("2. YO'QOLGAN QIYMATLARNI ANIQLASH")
print("=" * 55)

data = [
    {"ism": "Ali",     "yosh": 20,   "shahar": "Toshkent"},
    {"ism": "Zilola",  "yosh": None,  "shahar": "Samarqand"},
    {"ism": "Sardor",  "yosh": 25,   "shahar": None},
    {"ism": None,      "yosh": 30,   "shahar": "Buxoro"},
    {"ism": "Madina",  "yosh": None,  "shahar": "Toshkent"},
]

print("\nMa'lumotlar:")
for i, row in enumerate(data):
    print(f"  {i+1}. {row}")

print("\nYo'qolgan qiymatlar:")
total_missing = 0
for i, row in enumerate(data):
    for key, val in row.items():
        if val is None:
            print(f"  Qator {i+1}, \"{key}\" ustunida qiymat yo'q")
            total_missing += 1

print(f"\nJami yo'qolgan qiymatlar: {total_missing}")


# 3. Array statistikasi
print("\n" + "=" * 55)
print("3. ARRAY STATISTIKASI")
print("=" * 55)

arr = [20, 49, 31, 12, 80, -17, 51, 42]
print(f"\nArray: {arr}")

# O'rta arifmetik
mean = sum(arr) / len(arr)
print(f"\nO'rta arifmetik (mean): {mean}")

# Min
print(f"Minimum: {min(arr)}")

# Max
print(f"Maximum: {max(arr)}")

# Median
sorted_arr = sorted(arr)
print(f"Tartiblangan: {sorted_arr}")
n = len(sorted_arr)
if n % 2 == 0:
    median = (sorted_arr[n // 2 - 1] + sorted_arr[n // 2]) / 2
else:
    median = sorted_arr[n // 2]
print(f"Median: {median}")


# 5. Uy narxlari dataseti
uylar = [
    {"maydon": 120, "yoshi": 5,  "xonalar": 3, "hudud": "Shaharda",   "narx": 300_000_000},
    {"maydon": 150, "yoshi": 10, "xonalar": 4, "hudud": "Qishloqda",  "narx": 450_000_000},
    {"maydon": 100, "yoshi": 2,  "xonalar": 2, "hudud": "Shaharda",   "narx": 200_000_000},
    {"maydon": 200, "yoshi": 15, "xonalar": 5, "hudud": "Shaharda",   "narx": 500_000_000},
    {"maydon": 80,  "yoshi": 3,  "xonalar": 2, "hudud": "Qishloqda",  "narx": 180_000_000},
]

# a) Statistika
print("\n" + "=" * 55)
print("5a. STATISTIKA XULOSALARI")
print("=" * 55)

def statistika(qiymatlar, nom):
    s = sorted(qiymatlar)
    n = len(s)
    med = (s[n//2-1] + s[n//2]) / 2 if n % 2 == 0 else s[n//2]
    print(f"\n  {nom}:")
    print(f"     Min:    {min(s):>15,}")
    print(f"     Max:    {max(s):>15,}")
    print(f"     Mean:   {sum(s)/n:>15,.1f}")
    print(f"     Median: {med:>15,.1f}")

statistika([u["maydon"] for u in uylar], "Maydon (m²)")
statistika([u["yoshi"] for u in uylar], "Yoshi (yil)")
statistika([u["xonalar"] for u in uylar], "Xonalar soni")
statistika([u["narx"] for u in uylar], "Narx (so'm)")

# b) Kategoriyali -> Raqamli
print("\n" + "=" * 55)
print("5b. KATEGORIYALI -> RAQAMLI (Label Encoding)")
print("=" * 55)

hudud_encoding = {"Shaharda": 0, "Qishloqda": 1}
print(f"\n  Encoding: {hudud_encoding}\n")
for u in uylar:
    raqam = hudud_encoding[u["hudud"]]
    print(f"  {u['maydon']} m2 | {u['hudud']:^10} -> {raqam} | {u['narx']:>15,} so'm")

# c) Xonalari bo'yicha saralash
print("\n" + "=" * 55)
print("5c. XONALARI SONI BO'YICHA SARALASH")
print("=" * 55)

saralangan = sorted(uylar, key=lambda u: u["xonalar"])
print()
for u in saralangan:
    print(f"  {u['xonalar']} xona | {u['maydon']} m² | {u['hudud']:^10} | {u['narx']:>15,} so'm")
