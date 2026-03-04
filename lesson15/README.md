# Artificial Intelligence - 15-Topshiriq (Nazariy qism)
# Takrorlash — Barcha tushunchalar

## 1. Computer Vision

### a) Image Processing
**Image Processing** — raqamli rasmlarni qayta ishlash texnologiyasi. Rasm sifatini yaxshilash, filtrlash, ranglarni o'zgartirish kabi amallar bajariladi. Piksellar ustida matematik amallar orqali ishlaydi.

### b) Image Segmentation
**Image Segmentation** — rasmni ma'noli segmentlarga (qismlarga) bo'lish. Har bir pikselga sinf belgilanadi (odam, fon, mashina). Model: DeepLab. Misol: avtopilotda yo'l, odam, mashina ajratiladi.

---

## 2. Neural Networks

### a) Neural Network
**Neyron tarmoq** — inson miyasidagi neyronlarga o'xshab ishlaydi. Kiruvchi ma'lumotlarni qayta ishlab, og'irliklar orqali o'rganadi va natija chiqaradi.

### b) Layers (Qatlamlar)
| Qatlam | Vazifasi |
|--------|---------|
| **Input Layer** | Ma'lumotni qabul qiladi |
| **Hidden Layers** | Ma'lumotni qayta ishlaydi, patternlarni o'rganadi |
| **Output Layer** | Yakuniy natijani chiqaradi |

### c) Activation Functions
| Funksiya | Formula | Diapazoni |
|----------|---------|-----------|
| **Sigmoid** | 1/(1+e⁻ˣ) | (0, 1) |
| **Tanh** | (eˣ-e⁻ˣ)/(eˣ+e⁻ˣ) | (-1, 1) |
| **ReLU** | max(0, x) | [0, ∞) |

---

## 3. Machine Learning

### a) Regression
**Regressiya** — uzluksiz qiymatni bashorat qilish. Misol: uy narxini bashorat (y = mx + b).

### b) Classification
**Klassifikatsiya** — ma'lumotni toifalarga ajratish. Misol: email spam/spam emas (0 yoki 1).

### c) Clustering
**Klasterlash** — ma'lumotlarni labelsiz guruhlarga ajratish. Misol: K-Means bilan mijozlarni segmentlash.

---

## 4. Natural Language Processing

### a) Tokenization
Matnni tokenlarga (so'zlarga) bo'lish: `"Salom dunyo"` → `["Salom", "dunyo"]`

### b) Lemmatization
So'zni lug'at shakliga (lemma) keltirish: `"running"` → `"run"`, `"better"` → `"good"`

### c) Stemming
So'z o'zagini kesib olish (qo'pol usul): `"running"` → `"run"`, `"studies"` → `"studi"`

**Farqi:** Lemmatization — to'g'ri so'z beradi, Stemming — faqat o'zakni kesadi.

### d) Bag of Words
Matnni so'zlar chastotasi vektori sifatida ifodalash:
```
"mushuk yaxshi" → [1, 0, 1]
"it yaxshi"     → [0, 1, 1]
 Lug'at: [mushuk, it, yaxshi]
```

---

## 5. Yakuniy Loyiha

> `index.html` — AI Shaxsiylashtirilgan O'qitish Tizimi (Demo)
> `main.py` — Python ML modeli (tavsiya tizimi)
