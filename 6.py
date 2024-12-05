import random
n = int(input("n sonini kiriting: "))
son = random.randint(1, n)
for urinish in range(1, 4):
    taxmin = int(input(f"Sonni taxmin qiling "))
    if taxmin == son:
        print("Winner!")
        break
    else:
        print("Qaytadan urinish qiling.")

else:
    print("Looser! Siz sonni topa olmadingiz.")
