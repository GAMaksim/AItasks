# Artificial Intelligence - 3-Topshiriq (Nazariy qism)
# Searching Algorithms

## 1. "Agent" tushunchasi

**Agent** — atrofdagi muhitni (environment) sezib, qaror qabul qilib, harakat qiladigan tizim.

**Agent tarkibi:**
| Tarkibiy qism | Tavsif |
|---------------|--------|
| **Sensor** | Muhitni sezish (kamera, mikrofon, ma'lumot) |
| **Actuator** | Muhitga ta'sir qilish (harakat, javob berish) |
| **Agent Function** | Sensor ma'lumotidan actuator harakatiga o'tkazish |

**Misol:** Avtopilot mashina — kamera (sensor) yo'lni ko'radi, algoritm (agent function) qaror qiladi, rul (actuator) buriladi.

---

## 2. State Space, Initial State va Goal State

**Misol: Labirintdan chiqish**

```
  ┌───┬───┬───┬───┐
  │ S │   │ ▓ │   │     S = Start (Initial State)
  ├───┼───┼───┼───┤     G = Goal  (Goal State)
  │ ▓ │   │   │ ▓ │     ▓ = Devor (o'tib bo'lmaydi)
  ├───┼───┼───┼───┤       = Bo'sh yo'l
  │   │ ▓ │   │   │
  ├───┼───┼───┼───┤
  │   │   │ ▓ │ G │
  └───┴───┴───┴───┘
```

| Tushuncha | Tavsif |
|-----------|--------|
| **State Space** | Labirintdagi barcha mumkin bo'lgan pozitsiyalar to'plami |
| **Initial State** | Boshlang'ich nuqta — S (yuqori chap burchak) |
| **Goal State** | Maqsad nuqta — G (pastki o'ng burchak) |
| **Actions** | Yuqori, pastga, chapga, o'ngga yurish |
| **Path** | S dan G gacha bo'lgan yo'l ketma-ketligi |

---

## 3. Graf vizual ko'rinishi

```
            A
            │
            B
           / \
          C    D
          │    │
          E    F
          │   /|\
          G  H I
         / \   /|\
        J   K M N O
            │
            L
```

> Amaliy qism `main.py` da — BFS va DFS algoritmlari bilan yo'l topish.

---

## 4. BFS — A dan K gacha yo'l

> Amaliy qism `main.py` da — BFS algoritmining har bir qadami ko'rsatilgan.

---

## 5. BFS va DFS — A dan J gacha

Rasmdan olingan graf:
```
          A
        / | \
       B  C  D
      /\  |   \
     E  F G    H
        |  |
        I  J    ← Maqsad
```

> Amaliy qism `main.py` da — BFS va DFS algoritmlari taqqoslangan.
