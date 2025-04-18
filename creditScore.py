credit_score = int(input("Enter your credit score here: "))
income = float( input("Enter your income here: "))

if credit_score >=650 and income>=7000:
    print("You are quailified for a full studentloan")
if credit_score >=650 and income <7000:
    print("You are quailified for a 60 percent of the student loan")
if credit_score <650 and credit_score > 550:
    print("find a way to better your scores")
else:
    print("You are responsible for the paying your own school fees")


