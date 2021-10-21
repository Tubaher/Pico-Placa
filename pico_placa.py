""" Pico&Plate predictor
It takes a license plate number (the full number), a date and a time.
Then it determines if the car can be in the road.

pico_placa,py <plate_number> <date> <time>"""


import argparse
import datetime
from typing import Mapping

parser = argparse.ArgumentParser(description='Determine if a car should be in the road based on Pico&Placa.')
parser.add_argument('plate_number', type=str, help='full number of the plate, seven characters. Three letters, four numbers wit no hyphen.')
parser.add_argument('date', type=str, help='date of the query in format Year_Month_Day.')
parser.add_argument('time', type=str, help='time of the query in format Hour:Minute.')


class Plate():
    def __init__(self, plate_number) -> None:
        self.plate_number = plate_number.lower()

    def validate_plate(self):
        """ Validate if the plate has the format 3 letters (no ñ) and 4 numbers. 
            input : self
            output : boolean"""
        is_valid = True

        # check if the plate has the right length
        len_plate = len(self.plate_number)
        # it shouldn't be more or less than six numbers
        if (len_plate != 7):
            print(f'The lenght of the plate number is more or less than 7. It has {len_plate} numbers!.')
            is_valid = False

        else:
            for i,number in enumerate(self.plate_number):
                # first 3 characters should be letters and not ñ
                if i >= 0 and i < 3:
                    is_letter = (number.isalpha() and number != 'ñ')
                    # break condition and suggestion about the error
                    if not is_letter:
                        print('The plate has not a valid format. Remember LLL#### with no ñ. There is not 3 letters.')
                        is_valid = False
                        break 
                else:
                    # last 4 characters should be numbers
                    is_number = number.isnumeric()
                    # break condition and suggestion about the error
                    if not is_number:
                        print('The plate has not a valid format. Remember LLL#### with no ñ. There is not 4 numbers.')
                        is_valid = False
                        break
        return is_valid

class Car():
    """ Class to handle cars and their status on the road """

    def __init__(self, date, time, plate) -> None:
        self.date = date
        self.time = time
        self.plate = plate

    def validate_date(self):
        """ Validate if the given date is in the required format YY_mm_dd"""

        # control validation
        validated = True
        try:
            # from string to datetime
            self.date = datetime.datetime.strptime(self.date, '%Y_%m_%d')
        except:
            print('The date is not in the right format %Y_%m_%d')
            validated = False

        return validated

    def validate_time(self):
        """ Validate if the given time is in the format required %H:%M """
        
        validated = True
        try:
            # from string to datetime
            self.time = datetime.datetime.strptime(self.time, '%H:%M')
        except:
            print('The time is not in the right format %H:%M')
            validated = False

        return validated

    def pico_day(self, last_digit):
        """ Check if for the given digit in the given date is there some Pico&placa restriction """

        # control check if is pico day for that digit
        is_pico_day = False

        # dict with restrictions per day
        p_days = {
            1 : 'Monday',
            2 : 'Monday',
            3 : 'Tuesday',
            4 : 'Tuesday',
            5 : 'Wednesday',
            6 : 'Wednesday',
            7 : 'Thursday',
            8 : 'Thursday',
            9 : 'Friday',
            0 : 'Friday' 
        }

        # get the pico day for that digit
        p_day = p_days[eval(last_digit)]

        # check if the given date match with the pico day for that digit
        if datetime.datetime.strftime(self.date, '%A') == p_day:
            is_pico_day = True


        return is_pico_day

    def pico_time(self):
        """ Check if the car at that time is in a restricted schedule """

        # control variable for restriction
        restricted = False

        # times for Pico&Placa in the morning
        start_am = datetime.datetime.strptime('07:00', '%H:%M')
        end_am = datetime.datetime.strptime('09:30', '%H:%M')

        # times for Pico&Placa at night
        start_pm = datetime.datetime.strptime('16:00', '%H:%M')
        end_pm = datetime.datetime.strptime('19:30', '%H:%M')

        # Desicion making for restriction
        if self.time >= start_am and self.time <= end_am:
            restricted = True
        elif self.time >= start_pm and self.time <= end_pm:
            restricted = True

        return restricted

    def on_road(self):
        """ Check  if the car should be on the road or not
        according to Pico&Placa"""
        
        # control variables
        allowed = True
        issue = False

        # validation of given arguments
        v_plate = self.plate.validate_plate()
        v_date = self.validate_date()
        v_time = self.validate_time()
        
        # no issues to check the Pico & Placa alg
        if not (v_plate and v_date and v_time):
            issue = True

        # if all arguments are verified
        if not issue:
            last_digit = self.plate.plate_number[-1]

            # check if there is a restriction for that number today
            if self.pico_day(last_digit):

                # check if the car is in the restricted schedule
                if self.pico_time():
                    allowed = False
        
        else:
            print('Check the format for arguments and repeat.')
            allowed = False
        
        return allowed


def main():
    # collect arguments 
    args = parser.parse_args()
    
    # create instances
    plate = Plate(args.plate_number)
    car = Car(args.date, args.time, plate)

    # print the result
    print(car.on_road())

if __name__ == "__main__":
    main()