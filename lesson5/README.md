# Artificial Intelligence - 5-Topshiriq (Nazariy qism)
# Introduction to Machine Learning

## 1. Mashinali o'qitish nima?

**Machine Learning (ML)** — kompyuterga aniq qoidalar yozmasdan, ma'lumotlardan o'zi o'rganib, qaror qabul qilishni o'rgatuvchi AI tarmog'i.

**Qayerlarda ishlatiladi:**

| Soha | Misol |
|------|-------|
| **Email** | Spam xabarlarni filtrlash |
| **Tibbiyot** | Kasallikni bashorat qilish |
| **YouTube/Netflix** | Video tavsiya qilish |
| **Bank** | Firibgarlikni aniqlash |
| **Savdo** | Narxni bashorat qilish |
| **Transport** | Avtopilot mashinalar |

---

## 2. Mashinali o'qitish turlari

| Turi | Tavsif | Misol |
|------|--------|-------|
| **Supervised Learning** | Belgilangan (labeled) ma'lumotlar bilan o'rganadi | Rasm tanish, spam filtri |
| **Unsupervised Learning** | Belgilanmagan ma'lumotlardan o'zi pattern topadi | Mijozlarni guruhlash |
| **Reinforcement Learning** | Mukofot/jazo orqali o'rganadi | O'yin AI, robot |

---

## 3. Rasmda ko'rsatilgan o'rganish usuli

**Supervised Learning (Nazorat ostida o'qitish)**

Rasmda ko'rinib turibdi:
- **Labeled Data** — har bir rasm belgisi bilan berilgan (Elephant, Cow, Camel)
- **Supervisor** — to'g'ri javobni tekshiruvchi nazoratchi
- **Training Data Set** + **Desired Output** — o'qitish uchun ma'lumot va kutilgan natija
- **Algoritm** belgilangan ma'lumotdan o'rganib, yangi rasmlarni to'g'ri aniqlaydi

---

## 4. Rasmda ko'rsatilgan o'rganish usuli

**Unsupervised Learning (Nazoratsiz o'qitish)**

Rasmda ko'rinib turibdi:
- **Unknown Output** — kutilgan natija berilmagan
- **No Training Data Set** — o'qitish ma'lumotlari yo'q
- **Interpretation** — algoritm o'zi ma'lumotni tahlil qiladi
- Ma'lumotlar orasidagi **o'xshashlikni** o'zi topib, guruhlarga ajratadi (clustering)

---

## 5. Regressiya masalalari

**Regressiya** — uzluksiz (continuous) qiymatni bashorat qilish usuli.

**Maqsad:** Berilgan ma'lumotlar asosida kelajakdagi qiymatni taxmin qilish.

**Misol:** Uy narxini bashorat qilish — uy maydoni (m²) asosida narxini aniqlash.

> Amaliy qism `main.py` da — oddiy Linear Regression dasturi.
