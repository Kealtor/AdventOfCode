with open('input_day1.txt') as f:
    input = f.readlines()
    input = [int(i.strip()) for i in input]

list_of_increase_p1 = []
list_of_increase_p2 = []
for i in range(len(input)-3):
    if input[i]<input[i+1]:
        list_of_increase_p1.append('i')
        
for i in range(len(input)-3):
    if input[i]+input[i+1]+input[i+2]<input[i+1]+input[i+2]+input[i+3]:
        list_of_increase_p2.append('i')


print(len(list_of_increase_p1))
print(len(list_of_increase_p2))