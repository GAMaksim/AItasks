# Artificial Intelligence - 4-Topshiriq (Nazariy qism)
# Bilimni ifodalash — Knowledge Representation

## 1. Mulohazalar (Mantiqiy xulosa)

### a)
- **Shart:** Agar Bahrom darsda 5 baho olsa → otasi velosiped olib beradi
- **Fakt:** Bahrom velosiped **olmadi**
- **Xulosa:** Demak, **Bahrom darsda 5 baho olmagan**

> Mantiqiy usul: **Modus Tollens** — `A → B, ¬B ⊢ ¬A`

### b)
- **Shart:** Agar TV kabelidan signal kelsa → serial tomosha qilish mumkin
- **Fakt:** Serial tomosha qilinyapti
- **Xulosa:** Demak, **TV kabelidan signal kelayotgan bo'lishi kerak**

> Mantiqiy usul: **Modus Ponens (teskari)** — `A → B, B ⊢ A`

---

## 2. Mulohazalar (Disjunktiv sillogizm)

- **Shart 1:** OS kamchiliklari bo'lsa → driverlar kerak
- **Shart 2:** Xotirada joy yetishmasligi **yoki** OS kamchiliklari bor
- **Fakt:** Xotirada joy **yetishmaydi** (xotira muammosi bor)
- **Xulosa:** Demak, muammo **xotira yetishmasligida**, OS kamchiligi yo'q → **driverlar kerak emas**

> Mantiqiy usul: **Disjunktiv sillogizm** — `A ∨ B, A ⊢ ¬B` (eksklyuziv yoki)

---

## 3-4. Mantiqiy jadval va ifoda hisoblash

> Amaliy qism `main.py` da — jadval va hisoblash dasturda amalga oshirilgan.

---

## 5. First-Order Logic — 3 ta misol

**First-Order Logic** — predikatlar, kvantorlar (∀, ∃) va o'zgaruvchilar yordamida bilimni ifodalash.

### Misol 1: Barcha talabalar imtihon topshiradi
```
∀x (Talaba(x) → ImtihonTopshiradi(x))
```
"Har qanday x uchun: agar x talaba bo'lsa, u imtihon topshiradi"

### Misol 2: Ba'zi dasturchilar Python biladi
```
∃x (Dasturchi(x) ∧ Biladi(x, Python))
```
"Shunday x mavjudki: x dasturchi va x Python biladi"

### Misol 3: Ali Zilolaning do'sti
```
Do'st(Ali, Zilola)
∀x∀y (Do'st(x, y) → Do'st(y, x))
```
"Ali Zilolaning do'sti. Agar x y ning do'sti bo'lsa, y ham x ning do'sti"
