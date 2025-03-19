status = ["Tetap", "Honorer"]
group = ["A", "B", "C"]
salary = [1000000, 750000]
permanent_bonus = [200000, 400000, 550000]
honorary_bonus = [150000, 275000, 480000]

for s in status:
    print("Status:", s)
    for i in range(len(group)):
        if s == "Tetap":
            sal = salary[0]
            bonus = permanent_bonus[i]
        else:
            sal = salary[1]
            bonus = honorary_bonus[i]
        total = sal + bonus
        print("Golongan: ", group[i])
        print("Gaji pokok: ", sal)
        print("Bonus: ", bonus)
        print("Total: ", total)