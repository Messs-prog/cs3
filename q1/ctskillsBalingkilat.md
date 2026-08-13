## Section: 9-Balingkilat
## C#/name: #28 Ocampo, #29 Panahon, #30 Soriano
## Date: 08/13/2026

ANNEX B :
The Big Problem :
The new vending machine that was installed is inefficient and has a lot of defects. It sometimes give the wrong change, doesn't work properly when multiple students use it, gives the wrong item and can't track inventory properly.

The Sub Problems :
1.) The vending machine sometimes give the wrong change
2.) The vending machine doesn't notify the buyer or anyone when an item has run out.
3.) When a buyer press a wrong button, the vending machine gives the buyer the wrong item.
4.) The vending machine becomes slow when multiple buyers use it at once.

Possible CT Skills for each Sub Problems :
1.) Algorithm - This can help the vending machine give the correct change by calculating the total price, subtracting it from the amout paid and giving the change.
2.) Data Representation - This can notify people the number of items remaining by displaying it and notifying a staff when it hits a really low stock. You can use the quantity of each item by using it as data.
3.) Abstraction - It can clear the labels with the item name, price and image. 
4.) Decomposition - It can break the process of transaction down into smaller steps so it can process the student's order efficiently before proceeding to the next one.

4.) machine not notifying when an item is unavailable - pattern recognition - the machine can recognize the pattern of the item being unavailable once it has reached a quantity of 0. the machine can display an out of stock text to notify the user that the item is unavailable

START

Check the price of the item
Check the amount of money the buyer gave
Calculate the correct amount of change to be given to the buyer
IF Given change = Correct change THEN
  Change is correct
  END
ELSE 
  Change is incorrect
  Find Problem
IF Problem is the dispenser THEN
  change dispenser
IF Problem is coin sensor THEN
  change sensor
IF Problem is program THEN
  fix program

END
