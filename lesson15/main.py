# 15-Topshiriq
# AI Shaxsiylashtirilgan O'qitish Tizimi

import json
import math
import random

# 1. Sintetik ma'lumotlar
random.seed(42)

mavzular = ["Matematika", "Fizika", "Kimyo", "Biologiya", "Informatika"]
uslublar = ["vizual", "eshituvchan", "amaliy"]

talabalar = []
for i in range(15):
    talaba = {
        "id": i + 1,
        "ism": f"Talaba_{i+1}",
        "uslub": random.choice(uslublar),
        "natijalar": {m: random.randint(30, 100) for m in mavzular},
    }
    talabalar.append(talaba)

# 2. Materiallar bazasi
materiallar = {
    "Matematika": {
        "vizual":     ["Video: Algebrani ko'rgazmali o'rganish", "Infografika: Formulalar jadvali"],
        "eshituvchan": ["Podcast: Matematika asoslari", "Audio dars: Tenglamalar yechish"],
        "amaliy":     ["Mashqlar: 50 ta algebra masalasi", "Interaktiv: GeoGebra bilan ishlash"],
    },
    "Fizika": {
        "vizual":     ["Video: Nyuton qonunlari animatsiya", "Simulyatsiya: PhET laboratoriya"],
        "eshituvchan": ["Podcast: Fizika kundalik hayotda", "Audio: Mexanika asoslari"],
        "amaliy":     ["Tajriba: Erkin tushish tajribasi", "Loyiha: Oddiy elektr zanjir"],
    },
    "Kimyo": {
        "vizual":     ["Video: Kimyoviy reaksiyalar", "3D: Molekula tuzilishi"],
        "eshituvchan": ["Podcast: Davriy jadval", "Audio: Kislotalar va asoslar"],
        "amaliy":     ["Lab: Virtual kimyo laboratoriyasi", "Mashq: Tenglamalarni tenglashtirish"],
    },
    "Biologiya": {
        "vizual":     ["Video: Hujayra tuzilishi", "Animatsiya: DNK replikatsiyasi"],
        "eshituvchan": ["Podcast: Evolyutsiya nazariyasi", "Audio: Ekologiya asoslari"],
        "amaliy":     ["Loyiha: O'simlik kuzatuvi", "Tadqiqot: Mikroskop bilan ishlash"],
    },
    "Informatika": {
        "vizual":     ["Video: Python asoslari", "Infografika: Algoritmlar"],
        "eshituvchan": ["Podcast: AI tarixi", "Audio: Dasturlash tamoyillari"],
        "amaliy":     ["Mashq: 30 ta Python masala", "Loyiha: Kalkulator dasturi"],
    },
}

# 3. Tavsiya tizimi
def tavsiya_qil(talaba):
    natijalar = talaba["natijalar"]
    uslub = talaba["uslub"]

    # eng past natijali mavzularni topamiz
    sorted_mavzular = sorted(natijalar.items(), key=lambda x: x[1])
    zaif_mavzular = [m for m, n in sorted_mavzular if n < 70]

    tavsiyalar = []
    for mavzu in zaif_mavzular:
        if mavzu in materiallar and uslub in materiallar[mavzu]:
            for material in materiallar[mavzu][uslub]:
                tavsiyalar.append({
                    "mavzu": mavzu,
                    "material": material,
                    "sabab": f"{mavzu} dan {natijalar[mavzu]} ball — yaxshilash kerak"
                })

    return tavsiyalar

# 4. Baholash (Precision, Recall, F1)
def baholash():
    TP = 0  # to'g'ri ijobiy
    FP = 0  # noto'g'ri ijobiy
    FN = 0  # o'tkazib yuborilgan

    for talaba in talabalar:
        tavsiyalar = tavsiya_qil(talaba)
        zaif = [m for m, n in talaba["natijalar"].items() if n < 70]

        tavsiya_mavzulari = set(t["mavzu"] for t in tavsiyalar)

        for m in zaif:
            if m in tavsiya_mavzulari:
                TP += 1
            else:
                FN += 1

        for m in tavsiya_mavzulari:
            if m not in zaif:
                FP += 1

    precision = TP / (TP + FP) if (TP + FP) > 0 else 0
    recall = TP / (TP + FN) if (TP + FN) > 0 else 0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0

    return precision, recall, f1

# 5. Natijalar
print("=" * 60)
print("AI SHAXSIYLASHTIRILGAN O'QITISH TIZIMI")
print("=" * 60)

# talabalar jadvali
print(f"\nTALABALAR NATIJALARI:")
print(f"  {'Ism':<12} | {'Uslub':<10} | ", end="")
for m in mavzular:
    print(f"{m[:4]:^6}", end=" | ")
print()
print(f"  {'-'*12}-+-{'-'*10}-+", end="")
for _ in mavzular:
    print(f"-{'-'*6}-+", end="")
print()

for t in talabalar:
    print(f"  {t['ism']:<12} | {t['uslub']:<10} | ", end="")
    for m in mavzular:
        n = t['natijalar'][m]
        mark = " *" if n < 70 else "  "
        print(f"{n:>3}{mark} | ", end="")
    print()

# har bir talabaga tavsiya
print(f"\nSHAXSIY TAVSIYALAR:")
for t in talabalar[:5]:
    tavsiyalar = tavsiya_qil(t)
    if tavsiyalar:
        print(f"\n  {t['ism']} (uslub: {t['uslub']}):")
        for tv in tavsiyalar:
            print(f"    [{tv['mavzu']}] {tv['material']}")
            print(f"       Sabab: {tv['sabab']}")

# baholash
precision, recall, f1 = baholash()
print(f"\nMODEL BAHOLASH:")
print(f"  Precision: {precision:.2f}")
print(f"  Recall:    {recall:.2f}")
print(f"  F1 Score:  {f1:.2f}")

# json ga saqlash
output = {
    "talabalar": talabalar,
    "baholash": {"precision": round(precision, 2), "recall": round(recall, 2), "f1": round(f1, 2)}
}
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)
print(f"\nMa'lumotlar data.json ga saqlandi")
