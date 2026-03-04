def studentdetails(info):
    print("student name :",info[0])
    print("student batch :",info[1])
    print("student g_year :",info[2])
data = [
    ['karthikeya','pfs48','2026'],
    ['achuth','jfs45','2025'], 
    ['sathvik','pfs45','2026']
]
for i in data:
    studentdetails(i)