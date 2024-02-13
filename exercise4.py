math=int(input("math:"))
if math >100 or math<0:
    print("invalid")
english=int(input("english:"))
if english > 100 or english<0:
    print("invalid")
biology=int(input("biology:"))
if biology > 100 or biology<0:
    print("invalid")
chemistry=int(input("chemistry:"))
if chemistry > 100 or chemistry<0:
    print("invalid")
french=int(input("french:"))
if french>100 or french<0:
    print("invalid")

total=math+english+biology+chemistry+french
print(total)
average=total/5
print(average)

if average<=39:
    print("E")
elif average>=40 and average<=59 :
    print("D")
elif average>=60 and average<=69:
    print("C")
elif average>=70 and average<=79:
    print("B")
elif average>=80 and average<=100:
    print("A")
else:
    print("invalid")

