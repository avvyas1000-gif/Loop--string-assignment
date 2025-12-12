#check how many number divisible by 7
count=0
for i in range(1,101):
    if i%7==0:
        count = count+1
print(count)