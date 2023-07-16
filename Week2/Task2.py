def calculate_sum_of_bonus(data):
    total_bonus = 0
    old_total_bonus = 0
    individual_bonuses = {}

#定義bonus基準級距   
    performance_rules = {
        "above average": 0.1,
        "average": 0.05,
        "below average": 0.02
    }

    role_rules = {
        "Engineer": 0.03,
        "CEO" : 0.05,
        "Sales" : 0.01
    }

#比對所有input的個別物件
#注意所有括號用途
    for element in data["employees"]:
        old_salary = 0

#處理salary欄位
        salary = str(element["salary"])
        salary = salary.replace(",", "")

#處理外幣單位
        if "USD" in salary:
            salary = salary.replace("USD", "")  # 移除單位
            old_salary = float(salary) * 30  # 乘以幣值
        else:
            old_salary = float(salary)

#個人獎金 : 本薪*表現 + 本薪*職等
        bonus = old_salary * performance_rules[element["performance"]] + \
        old_salary * role_rules[element["role"]]

#儲存個人獎金
        individual_bonuses[element["name"]] = bonus

#計算總獎金
        old_total_bonus += individual_bonuses[element["name"]]

#總獎金若超過某數, 按比例調整獎金
    max_bonus = 10000
    if old_total_bonus > max_bonus:
        ratio = max_bonus / old_total_bonus
        old_total_bonus *= ratio
    
#同時調整員工獎金金額並印出
    for name in individual_bonuses:
        individual_bonuses[name] = int(individual_bonuses[name] * ratio)
        print(name , individual_bonuses[name])
        total_bonus += individual_bonuses[name]

    print(int(total_bonus))


calculate_sum_of_bonus({
    "employees":[
        {
        "name":"John",
        "salary":"1000USD",
        "performance":"above average",
        "role":"Engineer"
        },
        {
        "name":"Bob",
        "salary":60000,
        "performance":"average",
        "role":"CEO"
        },
        {
        "name":"Jenny",
        "salary":"50,000",
        "performance":"below average",
        "role":"Sales"
        }
    ]
}) # call calculate_sum_of_bonus function