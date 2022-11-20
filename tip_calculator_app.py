# print("tip calculator app")
# user_name = input('enter the user_name')
# num1 = 50
# num2 = 89
# print(num1+num2)
# last_name = "Paudel"
# frist_name = input('enter your name: ')
# age = int(input('enter your age'))
# print("Hello "+frist_name)
# pernamentaddress, currentaddress = "Ghorahi", "Kathmandu"
# country = (input('enter your country name: '))
# print(" You are living in the one of the most beautiful country in the world " +country + " " + currentaddress)

# Tip Calculator
print("-------------------------")
print("\n")
print("Bill Amount")
print("\n")
food_amount = float(input("Enter the food amount $ : "))
tip_percentage = float(input("Enter the tip amount % : "))/100
tip_amount = food_amount*tip_percentage
total_amount = food_amount+tip_amount
print("\n")
print(f"Food Amount $:{food_amount} ")
print(f"Tip Amount $:{tip_amount}")
print("\n")
print(f"The total amount $ :{total_amount}")
print("\n")

print("-------------------------")
