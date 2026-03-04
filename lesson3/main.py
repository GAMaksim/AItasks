# 3-Topshiriq (Amaliy qism)
# Searching Algorithms - BFS va DFS

from collections import deque

# BFS algoritmi
def bfs(graf, boshlangich, maqsad):
    navbat = deque([boshlangich])
    tashrif = set([boshlangich])
    yol = {boshlangich: None}

    print(f"  BFS: {boshlangich} -> {maqsad}")

    while navbat:
        tugun = navbat.popleft()
        print(f"  Tekshirilmoqda: {tugun}  |  Navbat: {list(navbat)}")

        if tugun == maqsad:
            natija = []
            while tugun is not None:
                natija.append(tugun)
                tugun = yol[tugun]
            return natija[::-1]

        for qoshni in graf.get(tugun, []):
            if qoshni not in tashrif:
                tashrif.add(qoshni)
                navbat.append(qoshni)
                yol[qoshni] = tugun

    return None


# DFS algoritmi
def dfs(graf, boshlangich, maqsad):
    stack = [boshlangich]
    tashrif = set()
    yol = {boshlangich: None}

    print(f"  DFS: {boshlangich} -> {maqsad}")

    while stack:
        tugun = stack.pop()
        if tugun in tashrif:
            continue
        tashrif.add(tugun)
        print(f"  Tekshirilmoqda: {tugun}  |  Stack: {stack}")

        if tugun == maqsad:
            natija = []
            while tugun is not None:
                natija.append(tugun)
                tugun = yol[tugun]
            return natija[::-1]

        for qoshni in reversed(graf.get(tugun, [])):
            if qoshni not in tashrif:
                stack.append(qoshni)
                if qoshni not in yol:
                    yol[qoshni] = tugun

    return None


# 4. Graf #1 - A dan K gacha (BFS)
graf1 = {
    "A": ["B"],
    "B": ["C", "D"],
    "C": ["E"],
    "D": ["F"],
    "E": ["G"],
    "F": ["H", "I"],
    "G": ["J", "K"],
    "H": ["L"],
    "I": ["M", "N", "O"]
}

print("=" * 50)
print("4. GRAF #1: A -> K (BFS)")
print("=" * 50)
print("""
  Graf ko'rinishi:
            A
            |
            B
           / \\
          C    D
          |    |
          E    F
          |   /|\\
          G  H I
         / \\   /|\\
        J   K M N O
            |
            L
""")

yol = bfs(graf1, "A", "K")
print(f"\n  Topilgan yo'l: {' -> '.join(yol)}")


# 5. Graf #2 - A dan J gacha (BFS va DFS)
graf2 = {
    "A": ["B", "C", "D"],
    "B": ["E", "F"],
    "C": ["G"],
    "D": ["H"],
    "E": [],
    "F": ["I"],
    "G": ["J"],
    "H": [],
    "I": [],
    "J": []
}

print("\n" + "=" * 50)
print("5. GRAF #2: A -> J (BFS va DFS taqqoslash)")
print("=" * 50)
print("""
  Graf ko'rinishi:
          A
        / | \\
       B  C  D
      /\\  |   \\
     E  F G    H
        |  |
        I  J
""")

print("--- BFS (Kenglik bo'yicha) ---")
yol_bfs = bfs(graf2, "A", "J")
print(f"\n  BFS yo'li: {' -> '.join(yol_bfs)}")

print(f"\n--- DFS (Chuqurlik bo'yicha) ---")
yol_dfs = dfs(graf2, "A", "J")
print(f"\n  DFS yo'li: {' -> '.join(yol_dfs)}")

print(f"""
  TAQQOSLASH:
  BFS: {' -> '.join(yol_bfs)}  ({len(yol_bfs)} qadam)
  DFS: {' -> '.join(yol_dfs)}  ({len(yol_dfs)} qadam)
""")
