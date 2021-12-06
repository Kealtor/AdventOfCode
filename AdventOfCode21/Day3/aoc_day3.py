import pandas as pd 
with open('input_day3.txt') as f:
    inputs = f.readlines()
    inputs = [i.strip() for i in inputs]

input = [[i for i in j] for j in inputs]

names = [f'd{i}' for i in range(12)]

df = pd.DataFrame(input , columns = names)
liste= []
for col in df.columns:
    liste.append(df[col].mode()[0])

liste2 = ['1' if i =='0' else '0' for i in liste]
print(int("".join(liste),2)*int("".join(liste2),2))

inputd = inputs.copy()
i=0
sublist = []
while len(inputd) != 1:
    sublist = []
    for j in inputd:
        if j[i] == liste[i]:
            sublist.append(j)
    inputd.clear()
    inputd = sublist.copy()
    i+=1
a = inputd
print(inputd)

inpute = inputs.copy()
i=0
sublist =[]
while len(inpute) != 1:
    sublist = []
    for j in inpute:
        if j[i] != liste[i]:
            sublist.append(j)
    inpute.clear()
    inpute = sublist.copy()
    i+=1
print(inpute)

print(int("".join(inputd),2)*int("".join(inpute),2))