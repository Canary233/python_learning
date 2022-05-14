bmi = float(input())
if bmi <= 18.5:
    out = "thin"
if bmi <= 25:
    out = "medium"
else:
    out = "fat"
print(out)