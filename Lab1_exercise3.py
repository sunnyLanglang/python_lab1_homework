print("График функции y=x/2 в первом квадранте:")
print(" y\u2191")
print("  \u2502")
for y in range(9, -1, -1):
    x = y * 2
    if y > 0:
        line = f"{y:2d}│" + " " * (x) + "•"
        print(line)
    else:
        print(" 0\u2514" + "\u2500" * 18 + "\u2192 x")
        print("   0 2 4 6 8 1012141618")