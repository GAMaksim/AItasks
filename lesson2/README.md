# Artificial Intelligence - 2-Topshiriq (Nazariy qism)

## 1. Hanoi minorasi — AI qanday yechadi?

**Masala:** N ta diskni Source ustundan Destination ga ko'chirish. Qoida: katta disk kichik disk ustiga qo'yilmaydi.

**AI yechimi — Rekursiv algoritm (Divide and Conquer):**
1. N-1 ta diskni `Source → Auxiliary` ga ko'chirish (rekursiv)
2. Eng katta diskni `Source → Destination` ga ko'chirish
3. N-1 ta diskni `Auxiliary → Destination` ga ko'chirish (rekursiv)

AI bu masalani **State Space** orqali yechadi — barcha holatlarni graf sifatida ko'rib, eng qisqa yo'lni topadi. Minimum qadamlar: **2^N - 1**

---

## 2. State Space nima?

**State Space** — masalaning barcha mumkin bo'lgan holatlarini va ular orasidagi o'tishlarni ifodalovchi model.

| Tarkibiy qism | Tavsif |
|---------------|--------|
| **Initial State** | Boshlang'ich holat (masala boshi) |
| **Goal State** | Maqsad holat (masala yechimi) |
| **Actions** | Holatni o'zgartiruvchi amallar |
| **Transitions** | Bir holatdan boshqasiga o'tish |

State Space = **graf**, tugunlar = holatlar, qirralar = amallar.

---

## 3. BFS (Breadth-First Search) nima va qanday ishlaydi?

**BFS** — grafda eng yaqin tugunlardan boshlab, **qatlam-qatlam** qidiradigan algoritm.

**Ishlash tartibi:**
1. Boshlang'ich tugunni navbatga (queue) qo'yish
2. Navbatdan birinchi tugunni olish
3. Uning barcha qo'shnilarini navbatga qo'shish
4. Maqsad topilguncha takrorlash

| Afzalliklari | Kamchiliklari |
|-------------|---------------|
| Eng qisqa yo'lni topadi | Ko'p xotira talab qiladi |
| To'liq — yechim albatta topiladi | Katta graflarda sekin |

---

## 4. ID raqamlarini tartiblash

> Amaliy qism `main.py` da — Bubble Sort algoritmida har bir qadam izohlab ko'rsatilgan.

---

## 5. Qidiruv strategiyalarining turlari

### Uninformed Search (Ko'r qidiruv)
Maqsad haqida ma'lumot yo'q, barcha yo'llarni tekshiradi:

| Strategiya | Tavsif |
|-----------|--------|
| **BFS** | Kenglik bo'yicha qidirish |
| **DFS** | Chuqurlik bo'yicha qidirish |
| **UCS** | Eng arzon yo'l bo'yicha |
| **DLS** | Cheklangan chuqurlikda |
| **IDDFS** | Bosqichma-bosqich chuqurlik |

### Informed Search (Aqlli qidiruv)
Maqsadga yaqinlik haqida ma'lumot (heuristika) bor:

| Strategiya | Tavsif |
|-----------|--------|
| **Greedy** | Eng yaqin tugunga boradi |
| **A\*** | Eng optimal yo'lni topadi |
| **Hill Climbing** | Faqat yuqoriga harakat |

**Farqi:** Ko'r qidiruv barcha yo'lni sinaydi (sekin), aqlli qidiruv maqsadga qarab yo'naladi (tez).
