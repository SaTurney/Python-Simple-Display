#TotalPurchase.py
#August 29, 2018
#Sabrina Turney
#Chapter 2 Exercise 4: Total Purchase

#This program utilizes input from user to get total price of 5 items + sales tax

def main():
    #Declare main function, initialize variables for items (user will be providing prices)
    #CamelCase naming convention for variables
    ItemOne = 0.0
    ItemTwo = 0.0
    ItemThree = 0.0
    ItemFour = 0.0
    ItemFive = 0.0

    ItemTotal = 0.0   #Making a variable for ItemOne-Five variables, so I don't need to type it all and clutter the math later
    SalesTax = 0.0    #Making a variable for the sales tax we will be calculating later
    TotalPurchase = 0.0 #Variable for total purchase price (items + sales tax)

    #Introduction - I added a newline here so I can read all the code easily in a smaller sized window
    print('''Welcome to the total price calculator! We will be calculating the\n total price of five items for you today.''')

    ItemOne = eval(input("Please enter the value of your first item: "))         #Keeping all input statements in one block for readability.
    ItemTwo = eval(input("Please enter the value of your second item: "))        #Prompt user, assign variable for the item. Using eval for float value.
    ItemThree = eval(input("Please enter the value of your third item: "))
    ItemFour = eval(input("Please enter the value of your fourth item: "))
    ItemFive = eval(input("Please enter the value of your fifth item: "))


    #I take all input values and assign them to a new variable (less typing, easier to read later)
    ItemTotal = (ItemOne + ItemTwo + ItemThree + ItemFour + ItemFive)

    print (f'\nThe total value of your items is: ${ItemTotal}\n')  #First establishing total cost of Items One-Five as ItemTotal
    print("Now, we will add the sales tax, which is 6%.")       #Calculate sales tax on Items One-Five as SalesTax using 6%
    SalesTax = (ItemTotal)*(0.06)

    print(f'Your sales tax on these five items will be ${SalesTax}.\n')#Requirement to show sales tax.

    TotalPurchase = (ItemTotal) + (SalesTax)                    #Calculate total purchase price of items and tax.
    print(f'The total purchase price of all your items with tax is ${TotalPurchase}.')#Requirement to show total purchase price.

   #You must use the main() funct call to begin this program. 
