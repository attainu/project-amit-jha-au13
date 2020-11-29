# PARKING LOT PROJECT

## DESCRIPTION

This is a parking lot project whose aim is to reduce human intervention and to make it an automatic process.

This project is made with the motive to provide solution for parking without any human intervention.

The parking spaces and car info are being stored in the **Dictionary** data type having a key and its value


_For eg:_

Parking Slot would be like = {'slot_no': Car_info OR Empty, 'slot_no': Car_info OR Empty, 'slot_no': Car_info OR Empty, ... So on}

Car Info would be like = {'regno': 'KA-01-HH-1234', 'color': 'White', 'current_time': '08:31:06', 'email': 'xyz@gmail.com'}

Empty/No Car would be like an empty dictionary = {}

---

## FEATURE

It has some basic listed features:

1. Create a Parking lot

2. Park new car

3. Leave a car

4. Check Status of Parking Lot

5. Search Car Registration No. by car Color

6. Search car Slot No. by car color

7. Search car Slot No. by car Registration No.

Extra Features:


1. Storing entry time of the car and email address of the car owner

2. Checking car parking duration while checking the status of Parking Lot

---

## EXPLAINING COMMANDS

| Feature                             | Command                                                              | Eg                                                |
| ----------------------------------- | -------------------------------------------------------------------- | ------------------------------------------------- |
| Create Parking                      | create_parking_lot(space)(no of slot per floor)(space)(no of floor)  | create_parking_lot 6 1                            |
| Check Parking Lot Status            | status                                                               | status                                            |
| Park a new car                      | park(space)(registration no)(space)(car color)(space)(email address) | park KA-01-HH-1234 White jhaamit3214@gmail.com |
| Leave a car                         | leave(space)(slot no)                                                | leave Floor1Slot4                                 |
| Search registrtaion no. by color    | registration_numbers_for_cars_with_colour(space)(Car color)          | registration_numbers_for_cars_with_colour White   |
| Search slot no. by color            | slot_numbers_for_cars_with_colour(space)(Car Color)                  | slot_numbers_for_cars_with_colour White           |
| Search slot no. by registration no. | slot_number_for_registration_number(space)(Registration No.)         | slot_number_for_registration_number KA-01-HH-1234 |

---

## USAGE

Just go to through the Parking_Lot.py and run the code 

This will show you an option of selecting 2 choices i.e. Running Terminal Commands by Press 1 || Running commands saved on file.txt by Press 2

By choosing 1 you can type the commands and their will be output for each command as mentioned below:

$ create_parking_lot 6  
Created a parking lot with 6 slots  

$ park KA-01-HH-1234 White  
Allocated slot number: 1  

$ park KA-01-HH-9999 White  
Allocated slot number: 2  

$ park KA-01-BB-0001 Black  
Allocated slot number: 3  

$ park KA-01-HH-7777 Red  
Allocated slot number: 4  

$ park KA-01-HH-2701 Blue  
Allocated slot number: 5  

$ park KA-01-HH-3141 Black  
Allocated slot number: 6  

$ leave 4  
Slot number 4 is free  

$ status  
Slot No. Registration No Colour  
1 KA-01-HH-1234 White  
2 KA-01-HH-9999 White  
3 KA-01-BB-0001 Black  
5 KA-01-HH-2701 Blue  
6 KA-01-HH-3141 Black  

$ park KA-01-P-333 White  
Allocated slot number: 4  

$ park DL-12-AA-9999 White  
Sorry, parking lot is full  

$ registration_numbers_for_cars_with_colour White  
KA-01-HH-1234, KA-01-HH-9999, KA-01-P-333  

$ slot_numbers_for_cars_with_colour White  
1, 2, 4  

$ slot_number_for_registration_number KA-01-HH-3141  
6  

$ slot_number_for_registration_number MH-04-AY-1111  
Not found  

$ exit



By choosing 2 the Input.txt will run and print the output of each command.

This will be input command we have saved in:

Input:

create_parking_lot 6

park KA-01-HH-1234 White jhaamit3214@gmail.com

park KA-01-HH-9999 White jhaamit3214@gmail.com

park KA-01-BB-0001 Black jhaamit3214@gmail.com

park KA-01-HH-7777 Red jhaamit3214@gmail.com

park KA-01-HH-2701 Blue jhaamit3214@gmail.com

park KA-01-HH-3141 Black jhaamit3214@gmail.com

leave Slot4

status

park KA-01-P-333 White jhaamit3214@gmail.com

park DL-12-AA-9999 White jhaamit3214@gmail.com

registration_numbers_for_cars_with_colour White

slot_numbers_for_cars_with_colour White

slot_number_for_registration_number KA-01-HH-1234

slot_number_for_registration_number MH-04-AY-1111

Output:

This will prvoide us the Ouput as as show below:

Created a parking lot with 6 slots

Allocated slot number: 1  
Allocated slot number: 2  
Allocated slot number: 3  
Allocated slot number: 4  
Allocated slot number: 5  
Allocated slot number: 6

Slot number 4 is free 

Slot No. Registration No Colour

1 KA-01-HH-1234 White  Jhaamit3214@gmail.com

2 KA-01-HH-9999 White  Jhaamit3214@gmail.com

3 KA-01-BB-0001 Black  Jhaamit3214@gmail.com

5 KA-01-HH-2701 Blue   Jhaamit3214@gmail.com

6 KA-01-HH-3141 Black  Jhaamit3214@gmail.com

Allocated slot number: 4

Sorry, parking lot is full

KA-01-HH-1234, KA-01-HH-9999, KA-01-P-333

1, 2, 4

6

Not found



---

---
