age = int(input("Ваш возраст? "))
height = float(input("Ваш рост? "))
weight = float(input("Ваш вес? "))

if age < 10 or height <= 0 or height > 3 or weight <= 0 or weight > 500:
    print("Ошибочные входные данные")
else:
    bmi = weight / height ** 2
    bmi = round(bmi, 2)
    description = ""
    if age < 45:
        if bmi < 18.5:
            description = "недостаточной массой тела."
        elif 18.5 < bmi <= 24.99:
            description = "нормальной массой тела."
        elif 25 <= bmi <= 29.99:
            description = "избыточной массой тела."
        else:
            description = "ожирением."

    if age >= 45:
        if bmi < 22:
            description = "недостаточной массой тела."
        elif 22 < bmi <= 26.99:
            description = "нормальной массой тела."
        elif 27 <= bmi <= 31.99:
            description = "избыточной массой тела."
        else:
            description = "ожирением."

    print("bmi=", bmi, "Вы относитесь к группе людей с", description)
