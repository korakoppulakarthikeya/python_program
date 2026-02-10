length = int(input("enter no of students:"))


names = []
cgpas = []
for i in range(length):
    name = input("enter names of students:")
    cgpa = float(input("enter cgpa ofstudents: "))
        
    names.append(name)
    cgpas.append(cgpa)
for i in range(length):
    print(str(i).ljust(2) ,names[i].ljust(20) , cgpas[i])