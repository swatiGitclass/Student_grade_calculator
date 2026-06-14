def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"

    else:
        return "Fail"
try:
    name = input("Enter Student Name:")

    subject1 = float(input("enter marks for Subject 1 :"))
    subject2 = float(input("enter marks for Subject 2 :"))
    subject3 = float(input("enter marks for Subject 3 :"))
    subject4 = float(input("enter marks for Subject 4 :"))
    subject5 = float(input("enter marks for Subject 5 :"))

    total = (
        subject1+
        subject2+
        subject3+
        subject4+
        subject5

)
        
    percentage = total/5

    grade = calculate_grade(percentage)

    print("\n =======RESULT =========")
    print("Student Name :", name)
    print("Total Marks u got is:", total)
    print("Percentage u got is :", round(percentage,2))
    print("Grade u got is :",grade)

except ValueError:
    print("please enter valid numeric marks.")

    