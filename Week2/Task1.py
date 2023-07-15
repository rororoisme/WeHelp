def find_and_print(messages):

    for name, message in messages.items():

#如果對話字串出現關鍵字就印出人名
#Python換行可以利用反斜線
        if "18 years old" in message \
        or "college student" in message \
        or "legal age" in message \
        or "vote" in message:
            
# 排除否定詞句
            if "not" not in message \
            and "under" not in message:
                print(name)









find_and_print({
"Bob":"My name is Bob. I'm 18 years old.",
"Mary":"Hello, glad to meet you.",
"Copper":"I'm a college student. Nice to meet you.",
"Leslie":"I am of legal age in Taiwan.",
"Vivian":"I will vote for Donald Trump next week",
"Jenny":"Good morning."
})
