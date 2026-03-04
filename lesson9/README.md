# Artificial Intelligence - 9-Topshiriq (Nazariy qism)
# Introduction to Neural Networks

## 1. Neyron tarmoqlar nima?

**Neyron tarmoq** — inson miyasidagi neyronlar tizimiga o'xshab ishlaydi. Kiruvchi ma'lumotlarni qayta ishlab, natija chiqaruvchi matematik model.

Har bir **neyron**: kirishni oladi → og'irlik bilan ko'paytiradi → aktivatsiya funksiyasidan o'tkazadi → natija chiqaradi.

---

## 2. Neyron tarmoq qismlari

| Qism | Xususiyati |
|------|-----------|
| **Input Layer** | Kiruvchi ma'lumotlarni qabul qiladi. Neyronlar soni = feature'lar soni |
| **Hidden Layer** | Ma'lumotni qayta ishlaydi. Bir yoki bir nechta qatlam. Murakkab patternlarni o'rganadi |
| **Output Layer** | Yakuniy natijani chiqaradi. Klassifikatsiya: 0/1, Regressiya: son |
| **Weights (og'irliklar)** | Har bir aloqa uchun og'irlik. O'qitish jarayonida o'zgaradi |
| **Bias (siljish)** | Har bir neyronning qo'shimcha parametri. Natijani sozlashga yordam beradi |
| **Activation Function** | Chiziqli bo'lmagan (nonlinear) o'zgarish kiritadi |

```
  Input Layer    Hidden Layer    Output Layer
  ┌───┐          ┌───┐
  │ x₁├────┐ ┌──►│ h₁├───┐
  └───┘    │ │   └───┘   │     ┌───┐
           ▼ ▲           ▼     │   │
  ┌───┐  ┌─────┐  ┌───┐  ┌──►│ y │
  │ x₂├─►│     ├─►│ h₂├──┘   └───┘
  └───┘  └─────┘  └───┘
```

---

## 3. Aktivatsiya funksiyalari

Aktivatsiya funksiyasi — neyronning chiqishini **chiziqli bo'lmagan** shaklga keltiradi. Ularsiz tarmoq faqat chiziqli masalalarni yecha oladi.

| Funksiya | Formula | Diapazoni | Qachon ishlatiladi |
|----------|---------|-----------|-------------------|
| **Sigmoid** | 1 / (1 + e⁻ˣ) | (0, 1) | Ikkilik klassifikatsiya |
| **Tanh** | (eˣ - e⁻ˣ) / (eˣ + e⁻ˣ) | (-1, 1) | Yashirin qatlamlar |
| **ReLU** | max(0, x) | [0, ∞) | Eng ko'p ishlatiladigan |
| **Softmax** | eˣᵢ / Σeˣ | (0, 1) | Ko'p klassli masalalar |

---

## 4. TensorFlow Playground tahlili

### Asl sozlamalar:
- **Activation:** Tanh
- **Dataset:** Circle (doiraviy)
- **Network:** 4 → 2 (2 ta yashirin qatlam)
- **Problem:** Classification

### O'zgartirilgan sozlamalar:
- **Activation:** ReLU ga o'zgartirdim — tezroq o'rganadi
- **Network:** 4 → 4 → 2 ga o'zgartirdim — qatlam qo'shdim
- **Learning Rate:** 0.03 → 0.01 — aniqroq o'rganadi
- **Noise:** 0 → 10 — real hayotga yaqinroq

### Tahlil:
- Qatlam qo'shilsa → **murakkab patternlar** o'rganadi
- ReLU → Tanh dan **tezroq** ishlaydi
- Learning Rate kamaytirsa → **aniqroq** lekin sekinroq
- Noise qo'shilsa → model **umumlashtirishni** o'rganadi
