qualification = input("Enter your qualification: ")
criminal_record = input("have you committed a crime before: ")
if qualification == "Bachelor degree" or qualification== "Masters":
    if criminal_record == "no":
        print("You are selected for the interview")
    else:
        print("we will call you back")
else: 
    print("You are not qualified for this job position")
    

