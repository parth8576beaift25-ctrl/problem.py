
#Write a program that prints numbers from 1 to 10 but skips 5 using continue.
i=1
while i<=10:
    if i==5:
      i+=1

      continue
    print(i)
    i+=1