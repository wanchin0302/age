driving = input ("請問有開車嗎? ")
age = input ("請輸入年齡: ")
age = int (age)
if driving == "有":
    if age >= 18:
       print("可以開車")
    else:
       print("你怎麼可以開車，是違法的")
elif driving == "沒有":
    if age >= 18:
       print("可以考駕照")
    else:
       print("18歲後，就可以考駕照了")
else:
    print("只能輸入有/沒有")

