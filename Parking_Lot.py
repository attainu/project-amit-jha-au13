class ParkingLot:
    def __init__(self):
        self.parking = {}
        self.total_car = 0
        self.total_slot = 1

    def make_parking(self, total_space=1):
        #self.parking = {}
        total_space = int(total_space) 
        i =  1
        while (i <= total_space):
            self.parking[( 'Slot' + str(i)).lower()] = {}
            i += 1
        print("Created a parking lot with", len(self.parking), "slots")
        #self.total_car = 0
        self.total_slot = len(self.parking)

    def ParkCar(self, regno, color, email):
        current_time = datetime.now().time()
        for key, values in self.parking.items():
            if values == {}:
                values['regno'] = regno
                values['color'] = color
                values['park_time'] = current_time
                values['email'] = email

                print("Allocated slot number: ", key)
                self.total_car += 1
                return

    def LeaveParkingSlot(self, slot):
        if slot in self.parking.keys():
            if self.parking[slot] != {}:
                car_data = self.parking[slot]
                duration = self.timeDuration(car_data['park_time'])
                print("Slot number", slot, "is free.")
                print("Duration Parked", duration)
                self.total_car -= 1
                self.parking[slot] = {}
            else:
                print("Slot number", slot, "is already free")
        else:
            print("Slot number", slot, "is not Present")

    def timeDuration(self, start):
        end = datetime.now().time()
        t1 = timedelta(hours=start.hour,
                       minutes=start.minute, seconds=start.second)
        t2 = timedelta(
            hours=end.hour, minutes=end.minute, seconds=end.second)
        return t2 - t1

    def PrintParkingLot(self):
        print("Slot No. Registration No Colour Entry_Time Duration Email")
        for key, values in self.parking.items():
            if values != {}:
                duration = self.timeDuration(values['park_time'])
                curr_time = values['park_time'].strftime("%H:%M:%S")
                print(key, values['regno'], values['color'],
                      curr_time, duration, values['email'])

    def FetchRegNoByColor(self, color):
        notFound = True
        for key, values in self.parking.items():
            if self.parking[key] != {}:
                if self.parking[key]['color'] == color:
                    if notFound:
                        print(values['regno'], end="")
                        notFound = False
                    else:
                        print(",", values['regno'])
        if notFound:
            print("Not found")

    def FetchSlotByColor(self, color):
        notFound = True
        for key in self.parking:
            if self.parking[key] != {}:
                if self.parking[key]['color'] == color:
                    if notFound:
                        print(key, end="")
                        notFound = False
                    else:
                        print(",", key)
        if notFound:
            print("Not found")

    def FetchSlotByRegNo(self, regno):
        for key, values in self.parking.items():
            if values != {}:
                if values['regno'] == regno:
                    print(key)
                    return
        print("Not found")

    def isNotFull(self):
        return 1 if self.total_car != self.total_slot else 0

    def isEmpty(self):
        return self.total_car == 0 


    def carNotExist(self, regno):
        for key in self.parking:
            if self.parking[str(key)] != {}:
                if self.parking[str(key)]['regno'] == regno:
                    return 0
        return 1
  
if __name__ == "__main__":
    from datetime import datetime, timedelta
    import re
    
    NewParking = ParkingLot()

    a = int(input("1 for Terminal Input and 2 for Executing File"))
    if a == 2:
        input_file = open("E:/Project/Input.txt", "r")
    while(True):
        if (a == 1):
            take = input().lower().split(" ")
        elif (a == 2):
            all_input_lines = input_file.readline()
            all_input_lines = all_input_lines.lower().replace('\n', '')
            take = all_input_lines.split(" ")
            if take[0] == '':
                break
       
            
        if take[0] == 'create_parking_lot':
            if len(take) == 2:
                NewParking.make_parking(take[1])
            elif len(take) == 1:
                NewParking.make_parking()
                

        elif take[0] == 'park':
            if NewParking.isNotFull():
                if NewParking.carNotExist(take[1]):
                    NewParking.ParkCar(take[1], take[2], take[3])
                else:
                    print("Sorry, Same Car Already Park")
            else:
                print("Sorry, parking lot is full")

        elif take[0] == 'leave':
            if(NewParking.isEmpty()):
                print("Parking Slot is Empty")
            else:
                NewParking.LeaveParkingSlot(take[1])

        elif take[0] == 'status':
            
            if(NewParking.isEmpty()):
                print("Parking Slot is Empty")
            else:
                NewParking.PrintParkingLot()
            
        elif take[0] == 'registration_numbers_for_cars_with_colour':
            if(NewParking.isEmpty()):
                print("Parking Slot is Empty")
            else:
                NewParking.FetchRegNoByColor(take[1])

        elif take[0] == 'slot_numbers_for_cars_with_colour':
            if(NewParking.isEmpty()):
                print("Parking Slot is Empty")
            else:
                NewParking.FetchSlotByColor(take[1])

        elif take[0] == 'slot_number_for_registration_number':
            if(NewParking.isEmpty()):
                print("Parking Slot is Empty")
            else:
                NewParking.FetchSlotByRegNo(take[1])

        elif take[0] == 'exit':
            break
        print()
        
    if a == 2:
        input_file.close()
