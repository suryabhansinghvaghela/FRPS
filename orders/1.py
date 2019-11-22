import csv
a=''' '''
with open('order-confirmation_108.csv','rt')as f:
  data = csv.reader(f)
  for row in data:
        a=a+str(row)
print(type(a))

