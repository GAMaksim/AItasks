# Artificial Intelligence - 6-Topshiriq (Nazariy qism)
# Data and Features in Machine Learning

## 1. Feature va Label nima?

| Tushuncha | Tavsif | Misol |
|-----------|--------|-------|
| **Feature** | Model uchun kiritish ma'lumotlari (ustunlar) | Uy maydoni, yoshi, xonalar soni |
| **Label** | Bashorat qilinadigan maqsad qiymat | Uy narxi |

**Afzalliklari:**
- Feature'lar ma'lumotdagi **muhim xususiyatlarni** ajratib oladi
- Label orqali model **nimani o'rganishi** kerakligini biladi
- Yaxshi tanlangan feature'lar modelning **aniqligini oshiradi**
- Keraksiz feature'larni olib tashlash **tezlikni oshiradi**

---

## 2-3. JavaScript kodlari

> Amaliy qism `main.js` da — yo'qolgan qiymatlarni aniqlash va array statistikasi.

---

## 4. Kategoriyali va Sonli ma'lumotlar farqi

| Xususiyat | Kategoriyali | Sonli |
|-----------|-------------|-------|
| **Turi** | Matn yoki guruh | Raqam |
| **Misol** | "Shaharda", "Qishloqda" | 120, 300000 |
| **Hisoblash** | Matematik amal qilib bo'lmaydi | +, -, ×, ÷ mumkin |
| **Grafik** | Doiraviy, ustunli | Chiziqli, nuqtali |

**Kategoriyali → Raqamli o'tkazish mumkinmi? Ha! ✅**

| Usul | Misol |
|------|-------|
| **Label Encoding** | Shaharda=0, Qishloqda=1 |
| **One-Hot Encoding** | Shaharda=[1,0], Qishloqda=[0,1] |

---

## 5. Uy narxlari dataseti

> Amaliy qism `main.py` da — statistika, encoding va saralash.
