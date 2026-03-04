# 4-Topshiriq (Amaliy qism)
# Bilimni ifodalash - Mantiqiy jadvallar

# 3. Mantiqiy jadval: C ∨ (¬A ∧ ¬B)
print("=" * 60)
print("3. MANTIQIY JADVAL: C ∨ (¬A ∧ ¬B)")
print("=" * 60)

print(f"\n{'A':^7}|{'B':^7}|{'C':^7}|{'¬A':^7}|{'¬B':^7}|{'¬A∧¬B':^7}|{'C∨(¬A∧¬B)':^11}")
print("-" * 60)

for A in [True, False]:
    for B in [True, False]:
        for C in [True, False]:
            not_A = not A
            not_B = not B
            and_result = not_A and not_B
            final = C or and_result

            a = "T" if A else "F"
            b = "T" if B else "F"
            c = "T" if C else "F"
            na = "T" if not_A else "F"
            nb = "T" if not_B else "F"
            ar = "T" if and_result else "F"
            fr = "T" if final else "F"

            print(f"{a:^7}|{b:^7}|{c:^7}|{na:^7}|{nb:^7}|{ar:^7}|{fr:^11}")

# 4. Ifoda qiymatini hisoblash
print("\n" + "=" * 60)
print("4. IFODA QIYMATINI HISOBLASH")
print("   (A ⇒ B) ∧ A ∧ ¬B ∨ C ∧ D")
print("   A=False, B=True, C=True, D=False")
print("=" * 60)

A = False
B = True
C = True
D = False

# Qadamma-qadam hisoblash
impl = (not A) or B      # A ⇒ B = ¬A ∨ B
not_B = not B             # ¬B

# Operator ustunligi: ¬ > ∧ > ∨ > ⇒
# ((A ⇒ B) ∧ A ∧ ¬B) ∨ (C ∧ D)
left = impl and A and not_B    # (A ⇒ B) ∧ A ∧ ¬B
right = C and D                 # C ∧ D
result = left or right          # Yakuniy

print(f"""
  Qadam 1: A ⇒ B  = ¬A ∨ B = ¬False ∨ True = True ∨ True = True
  Qadam 2: ¬B     = ¬True  = False
  Qadam 3: C ∧ D  = True ∧ False = False
  Qadam 4: (A ⇒ B) ∧ A ∧ ¬B = True ∧ False ∧ False = False
  Qadam 5: False ∨ False = False

  Natija: {result}  (False)
""")
