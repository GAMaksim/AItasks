# Artificial Intelligence - 8-Topshiriq (Nazariy qism)
# Unsupervised Learning: Clustering

## 1. Klasterlash nima?

**Klasterlash** — ma'lumotlarni o'xshashlik asosida guruhlarga (klasterlarga) ajratish. Label (belgi) berilmaydi — algoritm o'zi topadi.

**Usullari:**

| Usul | Tavsif |
|------|--------|
| **K-Means** | K ta markazga eng yaqin nuqtalarni guruhlaydi |
| **Hierarchical** | Daraxsimon tuzilma bilan guruhlaydi |
| **DBSCAN** | Zich hududlarni klaster deb belgilaydi |

---

## 2. K-Means (K-yaqin qo'shnilar) qanday ishlaydi?

**Qadamlar:**
1. **K ta tasodifiy markaz** tanlanadi (centroids)
2. Har bir nuqta **eng yaqin markazga** biriktiriladi
3. Har bir klaster uchun **yangi markaz** hisoblanadi (o'rtacha)
4. **2-3 qadamlar** markazlar o'zgarmagunicha takrorlanadi

---

## 3. Rasmlar tahlili

**1-rasm:** Ma'lumotlar nuqtalari 3 ta aniq guruhga bo'lingan:
- **Chap pastda** (~x:-6, y:3) — birinchi klaster
- **Yuqori o'rtada** (~x:0, y:9) — ikkinchi klaster
- **O'ng pastda** (~x:6, y:-4) — uchinchi klaster

K-Means algoritmi shu 3 ta guruhni avtomatik topgan.

**2-rasm:** Xuddi shu ma'lumotlar, lekin **2 ta qizil yulduzcha** (★) qo'shilgan — bular **centroids** (klaster markazlari) yoki **yangi nuqtalar**. Algoritm ularni eng yaqin klasterga biriktiradi.

---

## 4-5. Amaliy topshiriqlar

> `main.py` — K-Means klasterlash algoritmining to'liq kodi.
