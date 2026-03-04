# 11-Topshiriq (Amaliy qism)
# Oddiy Matn Klassifikatsiyasi - Spam Aniqlash (NLP)

# 1. Tokenizatsiya
def tokenize(matn):
    matn = matn.lower()
    belgilar = ".,!?;:()[]{}\"'-"
    for b in belgilar:
        matn = matn.replace(b, "")
    return matn.split()

# 2. Bag of Words
def bag_of_words(tokens, lugat):
    vektor = [0] * len(lugat)
    for token in tokens:
        if token in lugat:
            vektor[lugat.index(token)] += 1
    return vektor

# 3. O'qitish ma'lumotlari
train_data = [
    ("Bepul telefon yutib oling hoziroq", "spam"),
    ("Chegirma 90 foiz faqat bugun", "spam"),
    ("Siz million yutdingiz tabriklaymiz", "spam"),
    ("Bepul sovga olish uchun bosing", "spam"),
    ("Aktsiya narxi tushdi sotib oling", "spam"),
    ("Bugun darsga kech qolaman", "ham"),
    ("Ertaga uchrashuvga kelasizmi", "ham"),
    ("Uy vazifani qachon topshiramiz", "ham"),
    ("Kutubxonada yangi kitob bor", "ham"),
    ("Bugun ob havo yaxshi ekan", "ham"),
]

# 4. Lug'at yaratish
print("=" * 55)
print("MATN KLASSIFIKATSIYASI — Spam Aniqlash")
print("=" * 55)

# Stop words
stop_words = ["va", "bu", "uchun", "ham", "bilan", "bir", "da"]

all_tokens = []
for matn, _ in train_data:
    tokens = tokenize(matn)
    tokens = [t for t in tokens if t not in stop_words]
    all_tokens.extend(tokens)

lugat = list(set(all_tokens))
print(f"\nLug'at hajmi: {len(lugat)} ta so'z")

# 5. O'qitish
# Har bir sinf uchun o'rtacha vektorni hisoblash
spam_vektors = []
ham_vektors = []

for matn, label in train_data:
    tokens = tokenize(matn)
    tokens = [t for t in tokens if t not in stop_words]
    vektor = bag_of_words(tokens, lugat)
    if label == "spam":
        spam_vektors.append(vektor)
    else:
        ham_vektors.append(vektor)

# O'rtacha vektor
def ortacha_vektor(vektors):
    n = len(vektors)
    result = [0] * len(vektors[0])
    for v in vektors:
        for i in range(len(v)):
            result[i] += v[i]
    return [x / n for x in result]

spam_avg = ortacha_vektor(spam_vektors)
ham_avg = ortacha_vektor(ham_vektors)

# 6. Klassifikatsiya (Cosine Similarity)
import math

def cosine_similarity(v1, v2):
    dot = sum(a * b for a, b in zip(v1, v2))
    mag1 = math.sqrt(sum(a ** 2 for a in v1))
    mag2 = math.sqrt(sum(a ** 2 for a in v2))
    if mag1 == 0 or mag2 == 0:
        return 0
    return dot / (mag1 * mag2)

def classify(matn):
    tokens = tokenize(matn)
    tokens = [t for t in tokens if t not in stop_words]
    vektor = bag_of_words(tokens, lugat)

    spam_score = cosine_similarity(vektor, spam_avg)
    ham_score = cosine_similarity(vektor, ham_avg)

    return "spam" if spam_score > ham_score else "ham", spam_score, ham_score

# 7. O'qitish ma'lumotlari tekshiruv
print("\nO'qitish ma'lumotlari tekshiruvi:")
print(f"  {'Matn':^40} | {'Haqiqiy':^7} | {'Bashorat':^8} |")
print(f"  {'-'*40}-+-{'-'*7}-+-{'-'*8}-+")

togri = 0
for matn, label in train_data:
    pred, _, _ = classify(matn)
    status = "✅" if pred == label else "❌"
    togri += (pred == label)
    qisqa = matn[:38] + ".." if len(matn) > 38 else matn
    print(f"  {qisqa:<40} | {label:^7} | {pred:^8} | {status}")

print(f"\n  Aniqlik: {togri}/{len(train_data)} ({togri/len(train_data)*100:.0f}%)")

# 8. Yangi matnlarni tekshirish
print(f"\n{'=' * 55}")
print("YANGI MATNLARNI TEKSHIRISH")
print(f"{'=' * 55}\n")

test_messages = [
    "Bepul mashina yutib oling",
    "Ertaga darsga boramiz",
    "Chegirma faqat bugun sovga",
    "Kutubxonaga borib kitob olamiz",
    "Million dollar yutdingiz bosing",
]

for matn in test_messages:
    natija, spam_s, ham_s = classify(matn)
    icon = "🚫 SPAM" if natija == "spam" else "✅ HAM"
    print(f"  \"{matn}\"")
    print(f"    → {icon}  (spam: {spam_s:.3f}, ham: {ham_s:.3f})\n")
