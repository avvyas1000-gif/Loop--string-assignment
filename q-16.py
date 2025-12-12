str1 = "Hello Python Programmer"
count =0
for ch in str1:
    if ch.lower()in 'aeiou':
       count+=1
print(count)