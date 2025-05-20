grade = int(input("Enter yoiur grades: "))
attendance = int(input("Enter your attendance: "))

if grade >= 80:
    if attendance >= 85:
        print("Student passes with honors!")
    else:
        print("Student passes, but without honors!")
else:
    print("Student fails. ")
    
