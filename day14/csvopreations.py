import csv
'''with open("/Users/codegnan/day14/exampl.csv",'r') as f:
    content = csv.reader(f)
    for i in content:
        print(i)'''
with open("/Users/codegnan/day14/exampl.csv",'w',newline="") as f:
    writer=csv.writer(f)
    writer.writerow(['ssandeep',23,298373469])