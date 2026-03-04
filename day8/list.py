length = int(input("enter no of students:"))


names = []
cgpas = []
max_name = ''
max_value = 0
min_name = ''

for i in range(length):
    name = input("enter names of students:")
    cgpa = float(input("enter cgpa ofstudents: "))
    if cgpa>max_value:
        max_name = name
        max_value = cgpa
    elif cgpa<min_value:
        min_name = name
        min_value = cgpa

    names.append(name)
    cgpas.append(cgpa)
print("max is:",max_name,max_value)
print("min is:",min_name,min_value)
for i in range(length):
    print(str(i).ljust(2) ,names[i].ljust(20) , cgpas[i])