import random 
flowers = ["Антуриум", "Гербер", "Тюльпан"]
colors = ["белый", "красный", "синий", "розовый", "желтый"]
random_color = [random.randint (0, len(colors) - 1) for a in flowers]
flower_colors = dict(zip(flowers,[colors[i] for i in random_color]))
print(flower_colors)