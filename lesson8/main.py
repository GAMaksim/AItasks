# 8-Topshiriq (Amaliy qism)
# K-Means Clustering algoritmini qo'lda yozish

import math
import random

def masofa(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def kmeans(data, k, max_iter=100):
    # 1. Tasodifiy markazlar tanlash
    centroids = random.sample(data, k)

    for iteration in range(max_iter):
        # 2. Har bir nuqtani eng yaqin markazga biriktirish
        clusters = [[] for _ in range(k)]
        for point in data:
            distances = [masofa(point, c) for c in centroids]
            closest = distances.index(min(distances))
            clusters[closest].append(point)

        # 3. Yangi markazlarni hisoblash
        new_centroids = []
        for cluster in clusters:
            if cluster:
                avg_x = sum(p[0] for p in cluster) / len(cluster)
                avg_y = sum(p[1] for p in cluster) / len(cluster)
                new_centroids.append((avg_x, avg_y))
            else:
                new_centroids.append(random.choice(data))

        # 4. Markazlar o'zgarmasa to'xtatish
        if new_centroids == centroids:
            break
        centroids = new_centroids

    return clusters, centroids, iteration + 1


# 4. Dataset bilan klasterlash (k=3)
print("=" * 55)
print("4. K-MEANS KLASTERLASH (k=3)")
print("=" * 55)

data = [
    (2, 10), (2.5, 5), (8, 4), (5, 8), (7, 5),
    (10, 8), (8, 8), (3, 5), (5, 4), (6, 10)
]

print(f"\nMa'lumotlar: {data}")
print(f"K = 3 (3 ta klaster)")

random.seed(42)
clusters, centroids, iterations = kmeans(data, k=3)

print(f"\nNatija ({iterations} iteratsiya):\n")
for i, cluster in enumerate(clusters):
    cx, cy = round(centroids[i][0], 2), round(centroids[i][1], 2)
    print(f"  Klaster {i+1} (markaz: [{cx}, {cy}]):")
    for point in cluster:
        print(f"    • ({point[0]}, {point[1]})")


# 5. Kaggle Dataset simulyatsiyasi
print("\n" + "=" * 55)
print("5. KAGGLE DATASET — K-MEANS KLASTERLASH")
print("=" * 55)

# Kaggle datasetidan namuna (5 klaster)
random.seed(10)
kaggle_data = []

# 5 ta klaster generatsiya
centers = [(-6, 3), (0, 9), (6, -4), (-3, -3), (5, 5)]
for cx, cy in centers:
    for _ in range(20):
        x = cx + random.uniform(-2, 2)
        y = cy + random.uniform(-2, 2)
        kaggle_data.append((round(x, 1), round(y, 1)))

print(f"\nJami nuqtalar: {len(kaggle_data)}")
print("K = 5 (5 ta klaster)\n")

clusters, centroids, iterations = kmeans(kaggle_data, k=5)

print(f"Natija ({iterations} iteratsiya):\n")
for i, cluster in enumerate(clusters):
    cx, cy = round(centroids[i][0], 2), round(centroids[i][1], 2)
    print(f"  Klaster {i+1}: {len(cluster)} ta nuqta | Markaz: [{cx}, {cy}]")

# Batafsil ko'rsatish
print("\nKlasterlar tafsiloti:")
for i, cluster in enumerate(clusters):
    nuqtalar = [f"({p[0]},{p[1]})" for p in cluster[:5]]
    qolgan = f"... +{len(cluster)-5} ta" if len(cluster) > 5 else ""
    print(f"  Klaster {i+1}: {', '.join(nuqtalar)} {qolgan}")
