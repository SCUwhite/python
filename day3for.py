for i in range(1,6):
    print("这是第",i,"次循环")  
a=1
while a<=100:
    print(a)
    a+=1

total=0
for i in range(1,101):
    total+=i
print("1到100的和是:",total)
while True:
    pwd=input("请输入密码:")
    if pwd=="888888":
        print("密码正确，欢迎使用本系统")
        break
    else:
        print("密码错误，请重新输入")