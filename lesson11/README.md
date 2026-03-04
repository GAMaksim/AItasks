# Artificial Intelligence - 11-Topshiriq (Nazariy qism)
# Introduction to Natural Language Processing (NLP)

## 1. NLP nima va qanday ishlaydi?

**NLP (Natural Language Processing)** — kompyuterga inson tilini tushunish, tahlil qilish va generatsiya qilish qobiliyatini beruvchi AI tarmog'i.

**Qanday ishlaydi:**
1. **Matn olish** — foydalanuvchi yozadi yoki gapiradi
2. **Tokenizatsiya** — matnni so'zlarga bo'lish
3. **Tahlil qilish** — grammatika, ma'no, kontekst
4. **Natija chiqarish** — tarjima, javob, klassifikatsiya

---

## 2. NLP qayerlarda ishlatiladi?

| Soha | Misol |
|------|-------|
| **Chatbotlar** | ChatGPT, Siri, Alexa — savolga javob beradi |
| **Tarjima** | Google Translate — tillararo tarjima |
| **Spam filtri** | Email ichidagi spamni aniqlash |
| **Sentiment tahlili** | Sharhlardan ijobiy/salbiy fikr aniqlash |
| **Matn yaratish** | Yangiliklar, she'r, kod yozish |
| **Ovozni matnga** | Speech-to-Text texnologiyasi |

---

## 3. Text Processing va Text Analysis bosqichlari

| Bosqich | Tavsif |
|---------|--------|
| **1. Tokenizatsiya** | Matnni so'zlarga bo'lish: "Salom dunyo" → ["Salom", "dunyo"] |
| **2. Lowercasing** | Katta harflarni kichikga o'girish: "SALOM" → "salom" |
| **3. Stop words olib tashlash** | Keraksiz so'zlarni o'chirish: "va", "bu", "uchun" |
| **4. Stemming/Lemmatization** | So'zni asliga keltirish: "yozayotgan" → "yoz" |
| **5. Vectorization** | So'zlarni raqamlarga aylantirish (Bag of Words, TF-IDF) |
| **6. Tahlil** | Klassifikatsiya, sentiment, NER va boshqalar |

---

## 4. Tokenization va Bag of Words

### Tokenization
Matnni kichik qismlarga (tokenlarga) bo'lish:
```
"Python dasturlash tili" → ["Python", "dasturlash", "tili"]
```

### Bag of Words (BoW)
Matnni so'zlar chastotasi asosida vektorga aylantirish:

```
Matn 1: "mushuk yaxshi"
Matn 2: "it yaxshi"

Lug'at:  [mushuk, it, yaxshi]
Matn 1:  [1,     0,  1     ]
Matn 2:  [0,     1,  1     ]
```

---

## 5. Matn klassifikatsiyasi

> Amaliy qism `main.py` da — spam/spam emas klassifikatori.
