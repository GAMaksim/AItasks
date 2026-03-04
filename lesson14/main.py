# 14-Topshiriq (Amaliy qism)
# NLP - Sentiment, NER, POS, QA

# 2. Sentiment Analysis - Tvitlarni tahlil
print("=" * 55)
print("2. SENTIMENT ANALYSIS — Tvitlar tahlili")
print("=" * 55)

positive_words = [
    "good", "great", "love", "awesome", "happy", "best", "excellent",
    "beautiful", "amazing", "wonderful", "perfect", "like", "enjoy",
    "fantastic", "brilliant", "nice", "super", "yaxshi", "zo'r", "ajoyib"
]
negative_words = [
    "bad", "hate", "terrible", "awful", "worst", "ugly", "horrible",
    "stupid", "boring", "angry", "sad", "poor", "fail", "wrong",
    "yomon", "dahshat", "qo'rqinchli", "xunuk"
]

def sentiment_analyze(text):
    words = text.lower().split()
    pos = sum(1 for w in words if w in positive_words)
    neg = sum(1 for w in words if w in negative_words)
    if pos > neg:
        return "IJOBIY ✅", pos, neg
    elif neg > pos:
        return "SALBIY ❌", pos, neg
    return "NEYTRAL ➖", pos, neg

tweets = [
    "I love this new phone, it is amazing and beautiful!",
    "This movie was terrible and boring, worst ever",
    "The weather is nice today",
    "I hate waiting in traffic, it makes me angry",
    "What a great day, everything is perfect and wonderful",
    "Bu restoran juda yaxshi va ajoyib",
    "Yomon xizmat ko'rsatish, dahshat",
]

print(f"\n  {'Tvit':^45} | {'Natija':^12} | {'(+)':^3} | {'(-)':^3}")
print(f"  {'-'*45}-+-{'-'*12}-+-{'-'*3}-+-{'-'*3}")
for tweet in tweets:
    result, pos, neg = sentiment_analyze(tweet)
    short = tweet[:43] + ".." if len(tweet) > 43 else tweet
    print(f"  {short:<45} | {result:^12} | {pos:^3} | {neg:^3}")


# 3. Named Entity Recognition (NER)
print(f"\n{'=' * 55}")
print("3. NAMED ENTITY RECOGNITION (NER)")
print("=" * 55)

persons = ["Ali", "Elon", "Musk", "Putin", "Trump", "Biden", "Steve", "Jobs",
           "Zilola", "Sardor", "Bahrom", "Mirobidjon", "Karimov", "Mirziyoyev"]
locations = ["Toshkent", "Samarqand", "Buxoro", "London", "New York", "Tokyo",
             "Moscow", "Berlin", "Paris", "Uzbekistan", "America", "Japan", "O'zbekiston"]
organizations = ["Google", "Apple", "Tesla", "Microsoft", "Samsung", "OpenAI",
                 "Facebook", "Meta", "Amazon", "NASA", "UN", "FIFA"]

def ner_analyze(text):
    words = text.split()
    entities = []
    for word in words:
        clean = word.strip(".,!?;:'\"()[]")
        if clean in persons:
            entities.append((clean, "SHAXS"))
        elif clean in locations:
            entities.append((clean, "JOY"))
        elif clean in organizations:
            entities.append((clean, "TASHKILOT"))
    return entities

ner_sentences = [
    "Elon Musk founded Tesla and works with NASA in America",
    "Ali Toshkentda Google kompaniyasida ishlaydi",
    "Biden met Putin in Moscow to discuss UN policies",
    "Mirziyoyev Samarqandda Samsung zavodi ochdi",
    "Steve Jobs created Apple in America",
]

for sentence in ner_sentences:
    entities = ner_analyze(sentence)
    print(f"\n  \"{sentence}\"")
    for name, etype in entities:
        icons = {"SHAXS": "👤", "JOY": "📍", "TASHKILOT": "🏢"}
        print(f"    {icons[etype]} {name} → {etype}")


# 4. POS Tagging
print(f"\n{'=' * 55}")
print("4. PART-OF-SPEECH (POS) TAGGING")
print("=" * 55)

# Oddiy POS lug'ati
pos_dict = {
    # Otlar (Noun)
    "dog": "NOUN", "cat": "NOUN", "book": "NOUN", "car": "NOUN",
    "house": "NOUN", "city": "NOUN", "boy": "NOUN", "girl": "NOUN",
    "teacher": "NOUN", "student": "NOUN", "phone": "NOUN", "day": "NOUN",
    # Fe'llar (Verb)
    "is": "VERB", "are": "VERB", "was": "VERB", "run": "VERB",
    "eat": "VERB", "read": "VERB", "write": "VERB", "go": "VERB",
    "play": "VERB", "like": "VERB", "love": "VERB", "has": "VERB",
    "runs": "VERB", "reads": "VERB", "plays": "VERB", "likes": "VERB",
    # Sifatlar (Adjective)
    "big": "ADJ", "small": "ADJ", "fast": "ADJ", "slow": "ADJ",
    "good": "ADJ", "bad": "ADJ", "new": "ADJ", "old": "ADJ",
    "beautiful": "ADJ", "smart": "ADJ", "happy": "ADJ",
    # Ravishlar (Adverb)
    "very": "ADV", "quickly": "ADV", "slowly": "ADV", "always": "ADV",
    # Olmoshlar (Pronoun)
    "i": "PRON", "he": "PRON", "she": "PRON", "it": "PRON",
    "the": "DET", "a": "DET", "an": "DET", "this": "DET",
    # Bog'lovchilar
    "and": "CONJ", "but": "CONJ", "or": "CONJ",
    # Predloglar
    "in": "PREP", "on": "PREP", "at": "PREP", "to": "PREP", "with": "PREP",
}

pos_names = {
    "NOUN": "Ot", "VERB": "Fe'l", "ADJ": "Sifat", "ADV": "Ravish",
    "PRON": "Olmosh", "DET": "Artikl", "CONJ": "Bog'lovchi", "PREP": "Predlog"
}

def pos_tag(sentence):
    words = sentence.lower().strip(".,!?").split()
    result = []
    for word in words:
        clean = word.strip(".,!?")
        tag = pos_dict.get(clean, "UNKNOWN")
        result.append((word, tag))
    return result

pos_sentences = [
    "The big dog runs very fast",
    "She reads a new book in the house",
    "He is a smart and happy student",
]

for sentence in pos_sentences:
    tags = pos_tag(sentence)
    print(f"\n  \"{sentence}\"")
    for word, tag in tags:
        uz_name = pos_names.get(tag, "Noma'lum")
        print(f"    {word:<12} → {tag:<8} ({uz_name})")


# 5. Question Answering
print(f"\n{'=' * 55}")
print("5. SIMPLE QUESTION ANSWERING")
print("=" * 55)

knowledge_base = {
    "O'zbekiston": "O'zbekiston Markaziy Osiyodagi davlat. Poytaxti Toshkent. Aholisi 36 million.",
    "Python": "Python 1991-yilda Guido van Rossum tomonidan yaratilgan dasturlash tili.",
    "AI": "Sun'iy intellekt 1956-yilda John McCarthy tomonidan atamalashtirilgan.",
    "Google": "Google 1998-yilda Larry Page va Sergey Brin tomonidan asos solingan.",
    "Tesla": "Tesla 2003-yilda asoslangan elektromobil va energiya kompaniyasi. CEO: Elon Musk.",
    "TensorFlow": "TensorFlow Google tomonidan yaratilgan ochiq kodli mashinali o'qitish kutubxonasi.",
}

def answer_question(question):
    question_lower = question.lower()

    # Mavzuni topish
    best_topic = None
    best_score = 0
    for topic in knowledge_base:
        if topic.lower() in question_lower:
            if len(topic) > best_score:
                best_topic = topic
                best_score = len(topic)

    if not best_topic:
        return "Kechirasiz, bu savol uchun javob topilmadi."

    info = knowledge_base[best_topic]

    # Savolga mos javobni topish
    if any(w in question_lower for w in ["poytaxt", "capital"]):
        for sentence in info.split(". "):
            if "poytaxt" in sentence.lower() or "capital" in sentence.lower():
                return sentence
    elif any(w in question_lower for w in ["kim yaratgan", "kim tomonidan", "asoschisi", "founder", "created"]):
        for sentence in info.split(". "):
            if "tomonidan" in sentence.lower() or "asoslangan" in sentence.lower():
                return sentence
    elif any(w in question_lower for w in ["nima", "what"]):
        return info.split(". ")[0]
    elif any(w in question_lower for w in ["qachon", "when"]):
        for sentence in info.split(". "):
            if any(c.isdigit() for c in sentence):
                return sentence

    return info

questions = [
    "O'zbekistonning poytaxti qaysi?",
    "Python nima?",
    "AI ni kim yaratgan?",
    "Google qachon asoslangan?",
    "Tesla nima?",
    "TensorFlow nima?",
]

for q in questions:
    ans = answer_question(q)
    print(f"\n  ❓ {q}")
    print(f"  💡 {ans}")
