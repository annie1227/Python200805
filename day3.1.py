n=[]
s=[]
total=0
avg=0
amount=int(input("請輸入班上總人數: "))
for _ in range(amount):
    name=input("請輸入名字: ")
    score=int(input("請輸入分數: "))
    n.append(name)
    s.append(score)
print (s)

for m in range(amount):
    total=total+s[m]
avg=total/amount
print("平均是",avg)

highest=0
highest_name=''
lowest=99999999
lowest_name=''
for k in range (amount):
    if s[k]>highest:
        highest= s[k]
        highest_name= n[k]
print("最高分為",highest_name,"-", highest,"分")

for j in range (amount):
    if s[j]<lowest:
        lowest=s[j]
        lowest_name=n[j]
print("最低分為",lowest_name,"-",lowest,"分")