credit_score = int(input("Enter your credit score here: "))
income = float(input("Enter your income here: "))

if credit_score >= 650:
    if income >= 7000:
        print("You are qualified for a full student loan.")
    else:
        print("You are qualified for 60 percent of the student loan.")
elif 550 < credit_score < 650:
    print("Please find a way to improve your credit score.")
elif 350 <= credit_score <= 550:
    print("You are not qualified for a student loan.")
else:
    print("You are responsible for paying your own school fees.")
