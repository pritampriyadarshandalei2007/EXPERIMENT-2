# wap to enter % and display the graduation system.
percentage = float(input("Enter percentage: "))

if percentage >= 90:
    print("Graduation: A+")
elif percentage >= 80:
    print("Graduation: A")
elif percentage >= 70:
    print("Graduation: B")
elif percentage >= 60:
    print("Graduation: C")
elif percentage >= 50:
    print("Graduation: D")
else:
    print("Graduation: Fail")