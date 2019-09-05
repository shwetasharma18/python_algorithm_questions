obj = {
        'name':"Ram",
        'RollNo':12,
        'marks':{'Maths':50,'English':49,'seci':79},
        'teacher':{'Maths':"mr rama",'english':"ms komal"}
        }

print obj
for i in obj:
    print i , obj[i]

for i in obj:
    if i == "marks" or i == "teacher":
        for j in obj[i]:
            if j == "Maths":
                print obj["marks"][j] , obj["teacher"][j]
    break

new_list = []
for i in obj["marks"]:
    new_list.append(obj["marks"][i])
print max(new_list)
print min(new_list)

