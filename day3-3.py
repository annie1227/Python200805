n=[]
s=[]
total=0
a=0
amount=int(input("請輸入班上總人數: "))
for _ in range(amount):
    name=input("請輸入名字: ")
    score=int(input("請輸入分數: "))
    n.append(name)
    s.append(score)
print (s)
for k in s:
    total=total+k

print("平均是: ",avg(total,amount))

def avg(totall,aamount):
    return totall/aamount


highest=0
highest_name=''
lowest=99999999
lowest_name=''

def high(aamount,sscore,nname):
    highest=0
    highest_name=''
    for k in range (aamount):
        if sscore[k]>highest:
            highest= sscore[k]
            highest_name= nname[k]
    
    return highest,highest_name
print("最高分是: " ,high(amount,s,n))

def low(aa,ss,nn):
    lowest=99999999
    lowest_name=''
    for j in range (aa):
        if ss[j]<lowest:
            lowest=ss[j]
            lowest_name=nn[j]
            
    return lowest,lowest_name
print("最低分是: " ,low(amount,s,n))





#amount=int(input("請輸入班上總人數: "))
#for _ in range(amount):
#    name=input("請輸入名字: ")
#    score=int(input("請輸入分數: "))
#    n.append(name)
#    s.append(score)
#print (s)



#for m in range(amount):
#    total=total+s[m]
    
#print("平均是: ",avg(total,amount))
    
    
#    avg(10,2)