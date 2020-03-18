"""Gabriela Marie S. Mendez
   DATALGO Lab 02
   Feb. 5, 2020
   I have neither received nor provided any help
   on this (lab) activity, nor have I concealed
   any violation of the Honor Code.
"""
amount = float(input("Enter monetary amount charged: ")) #reads and constructs a numerical value
amtgiven = float(input("Enter monetary amount given: "))
change = amtgiven - amount

amt1 = change//1000  # // is used for integer division
change = change%1000  # modulo operator returns the remainder after performing the integer division
amt2 = change//500
change = change%500
amt3 = change//200
change = change%200
amt4 = change//100
change = change%100
amt5 = change//50
change = change%50
amt6 = change//20
change = change%20
amt7 = change//10
change = change%10
amt8 = change//5
change = change%5
amt9 = change//1
change = change%1
amt10 = change//.25
change = change%.25

print ("Number of 1000 peso bill: ", (amt1)) # prints the output
print ("Number of 500 peso bill: ", (amt2))
print ("Number of 200 peso bill: ", (amt3))
print ("Number of 100 peso bill: ", (amt4))
print ("Number of 50 peso bill: ", (amt5))
print ("Number of 20 peso bill: ", (amt6))
print ("Number of 10 peso coin: ", (amt7))
print ("Number of 5 peso coin: ", (amt8))
print ("Number of 1 peso coin: ", (amt9))
print ("Number of .25 peso coin: ", (amt10))
