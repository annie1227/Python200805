while True:
    print("------------------------------")
    print('1.加法')
    print('2.減法')
    print('3.乘法')
    print('4.除法')
    print('5.離開')
    x=int(input("請輸入數字: "))
    if x==5:
        break
    num1=int(input("請輸入第一個數: "))
    num2=int(input("請輸入第二個數: "))
    if x==1:
        print(num1,"+",num2,"=",num1+num2)
    elif x==2:
        print(num1,"-",num2,"=",num1-num2)
    elif x==3:
        print(num1,"x",num2,"=",num1*num2)
    elif x==4:
        print(num1,"/",num2,"=",num1/num2)
    else:
        break
    