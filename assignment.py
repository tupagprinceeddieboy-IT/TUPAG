300

def find_closest(a, b, c):
    diff_a = abs(300 - a)
    diff_b = abs(300 - b)
    diff_c = abs(300 - c)

    smallest = min(diff_a, diff_b, diff_c)

    if diff_a == diff_b == diff_c:
        print("All numbers are equally closest to", 300)
    elif diff_a == smallest:
        print(a, "is the closest number to", 300)
    elif diff_b == smallest:
        print(b, "is the closest number to", 300)
    else:
        print(c, "is the closest number to", 300)


print("Find the closest number to", 300)

a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))
c = int(input("Enter your third number: "))

find_closest(a, b, c)