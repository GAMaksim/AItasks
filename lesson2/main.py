# 2-Topshiriq (Amaliy qism)

# 1. Hanoi minorasi - AI rekursiv yechimi
def hanoi(n, source, destination, auxiliary):
    if n == 1:
        print(f"  Disk 1: {source} -> {destination}")
        return
    hanoi(n - 1, source, auxiliary, destination)
    print(f"  Disk {n}: {source} -> {destination}")
    hanoi(n - 1, auxiliary, destination, source)

print("=" * 50)
print("1. HANOI MINORASI (3 ta disk)")
print("=" * 50)
hanoi(3, "Source", "Destination", "Auxiliary")


# 3. BFS algoritmi
from collections import deque

def bfs(graf, boshlangich, maqsad):
    navbat = deque([boshlangich])
    tashrif = set([boshlangich])
    yol = {boshlangich: None}

    while navbat:
        tugun = navbat.popleft()
        print(f"  Tekshirilmoqda: {tugun}")

        if tugun == maqsad:
            natija = []
            while tugun is not None:
                natija.append(tugun)
                tugun = yol[tugun]
            return natija[::-1]

        for qoshni in graf[tugun]:
            if qoshni not in tashrif:
                tashrif.add(qoshni)
                navbat.append(qoshni)
                yol[qoshni] = tugun

    return None

print("\n" + "=" * 50)
print("3. BFS ALGORITMI")
print("=" * 50)

graf = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": [],
    "F": []
}

print("Graf: A->[B,C], B->[D,E], C->[F]")
print("Maqsad: A dan F gacha yo'l topish\n")
yol = bfs(graf, "A", "F")
print(f"\n  Topilgan yo'l: {' -> '.join(yol)}")


# 4. ID raqamlarini tartiblash (har qadam izohlangan)
print("\n" + "=" * 50)
print("4. ID RAQAMLARINI TARTIBLASH (Bubble Sort)")
print("=" * 50)

talabalar = [
    {"id": 1045, "ism": "Ali"},
    {"id": 1012, "ism": "Zilola"},
    {"id": 1078, "ism": "Sardor"},
    {"id": 1003, "ism": "Madina"},
    {"id": 1056, "ism": "Diyorbek"}
]

print("\nBoshlang'ich ro'yxat:")
for t in talabalar:
    print(f"  ID: {t['id']} - {t['ism']}")

print("\nTartiblash bosqichlari:")
n = len(talabalar)
qadam = 1
for i in range(n - 1):
    print(f"\n  --- {i + 1}-o'tish ---")
    for j in range(n - 1 - i):
        a = talabalar[j]["id"]
        b = talabalar[j + 1]["id"]
        if a > b:
            print(f"  Qadam {qadam}: {a} > {b} -> Almashtiramiz")
            talabalar[j], talabalar[j + 1] = talabalar[j + 1], talabalar[j]
        else:
            print(f"  Qadam {qadam}: {a} < {b} -> O'zgarishsiz")
        qadam += 1

print("\nTartiblangan ro'yxat:")
for t in talabalar:
    print(f"  ID: {t['id']} - {t['ism']}")
