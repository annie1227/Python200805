d={}

while True:
    print("1.建立詞彙")
    print("2.列出所有單字")
    print("3.英翻中")
    print("4.中翻英")
    print("5.測驗學習成果")
    print("6.離開系統")
    x=int(input("請輸入數字: "))
    if x==6:
        break
    
    if x==1:
        while True:
            eng=str(input("請輸入新單字(按0跳出): "))
            if eng=='0':
                break
            chi=str(input("請輸入中文單字: "))
            d[eng]=chi
        
    elif x==2:
        print(d)
        
    elif x==3:
        while True:
            eng=str(input("請輸入英文單字(按0跳出): "))
            if eng=='0':
                break
            print(eng,'的中文是',d[eng])
            
    elif x ==4:
        while True:
            chi=str(input("請輸入中文單字(按0跳出): "))
            if chi=='0':
                break
            for k,v in d.items():
                if v==chi:
                    print(chi,'的英文是',k)
                    
    elif x ==5:
         
         for k in d.keys():
             print(k)
             w=input("請輸入中文意思(按0跳出): ")
             if w=='0':
                 break
             elif w==d[k]:
                 print("答對了!")
             else:
                 print("再試一次!")
                 
    else:
        break
    
          
          
          
          
          
          