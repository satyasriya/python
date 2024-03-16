import csv

# Writing to the file
with open("student.csv", "a", newline="") as f:
    a = csv.writer(f)
    studentid = int(input("studentid: "))
    rollno = int(input("rollno: "))
    name = input("name: ")
    phno = int(input("phno: "))
    a.writerow([studentid, rollno, name, phno])
    print("Student record has been saved.")

# Reading from the file
with open('student.csv', 'r', newline='') as f:
    read = csv.DictReader(f)
    for row in read:
        print(row['studentid'], row['name'])
