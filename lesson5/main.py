# 5-Topshiriq (Amaliy qism)
# Oddiy Linear Regression - Uy narxini bashorat qilish

# 5. Regressiya masalasi
# ma'lumot: uy maydoni va narxi
# maqsad: yangi uy maydoniga qarab narxini bashorat qilish

print("=" * 55)
print("5. ODDIY LINEAR REGRESSION")
print("   Uy narxini bashorat qilish (maydon bo'yicha)")
print("=" * 55)

# O'qitish ma'lumotlari
maydonlar = [30, 45, 60, 75, 90, 105, 120]     # m²
narxlar =   [150, 200, 280, 350, 420, 500, 580]  # mln so'm

n = len(maydonlar)

print("\nO'qitish ma'lumotlari:")
print(f"  {'Maydon (m²)':^15} | {'Narx (mln)':^15}")
print(f"  {'-'*15}-+-{'-'*15}")
for i in range(n):
    print(f"  {maydonlar[i]:^15} | {narxlar[i]:^15}")

# formulalar
# y = mx + b (chiziqli formula)
# m = (n*Σxy - Σx*Σy) / (n*Σx² - (Σx)²)
# b = (Σy - m*Σx) / n

sum_x = sum(maydonlar)
sum_y = sum(narxlar)
sum_xy = sum(maydonlar[i] * narxlar[i] for i in range(n))
sum_x2 = sum(x ** 2 for x in maydonlar)

m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
b = (sum_y - m * sum_x) / n

print(f"\nHisoblash:")
print(f"  Σx  = {sum_x}")
print(f"  Σy  = {sum_y}")
print(f"  Σxy = {sum_xy}")
print(f"  Σx² = {sum_x2}")
print(f"  m (og'irlik) = {round(m, 2)}")
print(f"  b (siljish)  = {round(b, 2)}")
print(f"\n  Formula: narx = {round(m, 2)} * maydon + {round(b, 2)}")

# bashorat
print(f"\n{'=' * 55}")
print("BASHORAT:")
print(f"{'=' * 55}")

test_maydonlar = [40, 80, 100, 150]
for maydon in test_maydonlar:
    narx = m * maydon + b
    print(f"  {maydon} m² uy narxi: {round(narx)} mln so'm")

# aniqlik tekshirish
print(f"\n{'=' * 55}")
print("ANIQLIK TEKSHIRISH:")
print(f"{'=' * 55}")

print(f"  {'Maydon':^10} | {'Haqiqiy':^10} | {'Bashorat':^10} | {'Farq':^10}")
print(f"  {'-'*10}-+-{'-'*10}-+-{'-'*10}-+-{'-'*10}")

jami_xato = 0
for i in range(n):
    bashorat = round(m * maydonlar[i] + b)
    farq = abs(narxlar[i] - bashorat)
    jami_xato += farq
    print(f"  {maydonlar[i]:^10} | {narxlar[i]:^10} | {bashorat:^10} | {farq:^10}")

ortacha_xato = round(jami_xato / n, 1)
print(f"\n  O'rtacha xatolik: {ortacha_xato} mln so'm")
