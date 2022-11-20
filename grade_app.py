# percentage=float(input("Enter your percentage: "))

# if percentage <= 90 :
#     print("You have got an grade A")
# elif percentage <=80:
#     print("You have got grade B")
# elif percentage <=70:
#     print("You have got grade C")
# elif percentage <=60:
#     print("You have got grade D ")
# else:
#     print("You have got E")

# Grade Calculator

mark_math=int(input("Enter your mark in the mathematics : "))
mark_physics=int(input("Enter your mark in the Physics : "))
mark_chemistry=int(input("Enter your mark in the Chemistry : "))
mark_computer=int(input("Enter your mark in the Computer : "))
mark_biology=int(input("Enter your mark in the Biology : "))
mark_english=int(input("Enter your mark in the English : "))
mark_nepali=int(input("Enter your mark in the Nepali  : "))
total_mark=700
acheive_mark=float(mark_math+mark_physics
+mark_chemistry+mark_computer+mark_biology+mark_english+mark_nepali)
print(acheive_mark)
percentage=float(acheive_mark/total_mark*100)
print(f"Your percentage is {percentage}")

    # Grade Logic
if percentage <=90:
    print("You have got A grade")
elif percentage <=80:
    print("You have got B grade")
elif percentage <=70:
    print("You have got a C")
elif percentage <=60:
    print("You have got a C")
elif percentage <=50:
    print("You have got a C")
else:
    print("You have got a grade")