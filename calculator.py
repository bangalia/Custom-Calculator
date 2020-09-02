#Hello and welcome to the fluffy hat emporium!
#This is a calculator that uses the circumference of your head and the length of your forehead to calculate
# the perfect amount of fabric needed for your custom hat.
name=input("Enter your name:")
print("Hello "+ name+"!")
circumference=input("please enter the circumference of your head")
#measure the circumference with a measuring tape, don't forget to slip one finger in the side for extra space!
circumference=int(circumference)
print(circumference)
hat_length=input("please enter the length of your forehead minus 2")
hat_length=int(hat_length)
print(hat_length)
in_fabric=(circumference * hat_length)
print(in_fabric)