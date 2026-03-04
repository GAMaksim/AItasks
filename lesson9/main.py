# 9-Topshiriq (Amaliy qism)
# Oddiy Neyron Tarmoq - XOR masalasi

import math
import random

# aktivatsiya funksiyalari
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# oddiy neyron tarmoq
print("=" * 55)
print("ODDIY NEYRON TARMOQ — XOR masalasi")
print("=" * 55)

# XOR ma'lumotlari
# Kirish: [x1, x2], Chiqish: x1 XOR x2
inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
targets = [0, 1, 1, 0]

print("""
  XOR jadvali:
  ┌─────┬─────┬────────┐
  │  x1 │  x2 │ Natija │
  ├─────┼─────┼────────┤
  │  0  │  0  │   0    │
  │  0  │  1  │   1    │
  │  1  │  0  │   1    │
  │  1  │  1  │   0    │
  └─────┴─────┴────────┘
""")

# Tarmoq: 2 kirish → 2 yashirin → 1 chiqish
random.seed(42)

# Og'irliklar (random)
w_hidden = [[random.uniform(-1, 1) for _ in range(2)] for _ in range(2)]
b_hidden = [random.uniform(-1, 1) for _ in range(2)]
w_output = [random.uniform(-1, 1) for _ in range(2)]
b_output = random.uniform(-1, 1)

learning_rate = 0.5
epochs = 10000

print("O'qitish boshlandi...\n")

for epoch in range(epochs):
    total_error = 0

    for i in range(len(inputs)):
        x = inputs[i]
        target = targets[i]

        # Forward pass — Yashirin qatlam
        hidden = []
        for j in range(2):
            z = x[0] * w_hidden[j][0] + x[1] * w_hidden[j][1] + b_hidden[j]
            hidden.append(sigmoid(z))

        # Forward pass — Chiqish qatlam
        z_out = hidden[0] * w_output[0] + hidden[1] * w_output[1] + b_output
        output = sigmoid(z_out)

        # Xatolik
        error = target - output
        total_error += error ** 2

        # Backpropagation — Chiqish qatlamni yangilash
        d_output = error * sigmoid_derivative(output)

        for j in range(2):
            w_output[j] += learning_rate * d_output * hidden[j]
        b_output += learning_rate * d_output

        # Backpropagation — Yashirin qatlamni yangilash
        for j in range(2):
            d_hidden = d_output * w_output[j] * sigmoid_derivative(hidden[j])
            for k in range(2):
                w_hidden[j][k] += learning_rate * d_hidden * x[k]
            b_hidden[j] += learning_rate * d_hidden

    if epoch % 2000 == 0:
        print(f"  Epoch {epoch:>5}: Xatolik = {total_error:.6f}")

print(f"  Epoch {epochs:>5}: Xatolik = {total_error:.6f}")

# natijalar
print(f"\n{'=' * 55}")
print("NATIJALAR")
print(f"{'=' * 55}\n")

print(f"  {'Kirish':^10} | {'Kutilgan':^8} | {'Bashorat':^8} | {'Yaxlitlangan':^12}")
print(f"  {'-'*10}-+-{'-'*8}-+-{'-'*8}-+-{'-'*12}")

for i in range(len(inputs)):
    x = inputs[i]
    hidden = []
    for j in range(2):
        z = x[0] * w_hidden[j][0] + x[1] * w_hidden[j][1] + b_hidden[j]
        hidden.append(sigmoid(z))
    z_out = hidden[0] * w_output[0] + hidden[1] * w_output[1] + b_output
    output = sigmoid(z_out)
    rounded = 1 if output >= 0.5 else 0
    status = "✅" if rounded == targets[i] else "❌"
    print(f"  {str(x):^10} | {targets[i]:^8} | {output:^8.4f} | {rounded:^12} {status}")

print(f"""
  📊 Tarmoq tuzilishi:
     Input (2)  →  Hidden (2)  →  Output (1)
     Aktivatsiya: Sigmoid
     O'qitish tezligi: {learning_rate}
     Epochlar: {epochs}
""")
