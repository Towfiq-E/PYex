large=None
small=None

while True:
    num=input("enter a int number ")
    if num=="done":
        break
    try:
            num1=int(num)

    except:
            print("invalid input")
            continue
    if large is None:
        large=num1
    elif num1>large:
        large=num1
        continue

    if small is None:
        small=num1
    elif num1<small:
        small=num1
        continue




print('maxi', large)
print('mini', small)


