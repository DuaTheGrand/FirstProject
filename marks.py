def mark_calculator (marks:int):
    print("!!!")
    if marks > 0 and marks < 50:
        return 2
    elif marks >= 50 and marks <65:
        return 3
    elif marks >= 65 and marks < 80:
        return 4
    elif marks >= 80 and marks <=100:
        return 5
    else:
        return("Marks are between 0 and 100")

print(mark_calculator(65))
print(mark_calculator(81))
print(mark_calculator(43))
print(mark_calculator(120))
print(mark_calculator(-1))
