def calculate_sum_of_bonus(data):
    total_bonus = 0

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

#本薪*表現 + 本薪*職等 = 獎金
        total_bonus += old_salary * performance_rules[element["performance"]] + \
                       old_salary * role_rules[element["role"]]


#設定獎金上限,超過則按照比例調降
    max_bonus = 10000
    

    if total_bonus > max_bonus:
        ratio = max_bonus / total_bonus  # 比例
        total_bonus *= ratio

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