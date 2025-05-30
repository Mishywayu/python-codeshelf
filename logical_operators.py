has_high_income = False
has_good_credit = False

if has_high_income and has_good_credit:  #all conditions shuld be true
    print("Eligible for loan")
else:
    print("Nope, not eligible")

if has_high_income or has_good_credit:  #atleast one condition should be true
    print("Eligible for loan")
else:
    print("Has none")


has_good_credits = False
has_criminal_record = False

if has_good_credits and not has_criminal_record:
    print("Yes, they are eligible for loans")
else:
    print("No, they are not eligible for loans")