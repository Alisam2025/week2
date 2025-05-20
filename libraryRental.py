membership_status = input(" Enter member's status: ")
overdue_books = int(input("Enter the number of overdue books: "))
if membership_status== "active":
    if overdue_books==0:
        print("allow to rent new books")
    else:
        print("clear overdue books before renting")
elif membership_status== "none":
    print("You are not a member")
elif membership_status== "expired":
    if overdue_books==0:
        print("Renew your membership")
    else:
        print("Renew your membership and clear overdue books")
else:
    print("Renew your membership or get a new membership")
    