import csv
f=open("student.csv","a",newline="")
a=csv.writer(f)
a.writerow(["studentid","rollno","name","phno"])
studentid=int(input("studentid: "))
rollno = int(input("rollno: "))
name = input("name: ")
phno= int(input("phno: "))
a.writerow([studentid,rollno,name,phno])
print("student record has save")
with open('student.csv','r',newline='') as file:
    read = csv.DictReader(file)
    for i in read:
        print(i['rollno'],i['name'])
