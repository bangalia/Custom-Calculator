#Hello and welcome to the Fluffy Hat Emporium!
#This is a calculator that uses the circumference of your head and the length of your forehead to calculate
# the fluff fusion equation for your custom hat.
name=input("Enter your name:")
print("Hello "+ name+"!")
circumference=input("Please enter the circumference of your head")#in inches
#Measure the circumference with a measuring tape, don't forget to slip one finger in the side for extra space!
circumference=int(circumference)
print(circumference)
hat_length=input("Please enter the length of your forehead minus 2")#in inches
#The subtracting 2 is so your hat will rest perfectly on your forehead to showcase your face :)
hat_length=int(hat_length)
print(hat_length)
in_fabric=(circumference * hat_length) #in in the variable name stands for inches
in_fabric=int(in_fabric)
fave_color=input("What is your favorite color?")
fluff_preference=input("Would you like a small or large puffball?")
fluffy="Your fluff fusion equation is %s of %s warm fabric with a %s puffball!" % (in_fabric,fave_color,fluff_preference)
print(fluffy)
 