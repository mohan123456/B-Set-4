a=input("enter:")
b="~!@#$%^&*()<>?:,./;"
count=0
for i  in a:
  if i in b :
    count=count+1
print(count)
