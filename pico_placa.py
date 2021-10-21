""" Pico&Plate predictor
It takes a license plate number (the full number), a date and a time.
Then it determines if the car can be in the road.

pico_placa,py <plate_number> <date> <time>"""


import argparse
from typing import Mapping

parser = argparse.ArgumentParser(description='Determine if a car should be in the road based on Pico&Placa')
parser.add_argument('plate_number', type=str, help='full number of the plate')
parser.add_argument('date', type=str, help='date of the query in format Year-Month-Day')
parser.add_argument('time', type=str, help='time of the query in format Hour:Minute')


class Plate():
    def __init__(self, plate_number) -> None:
        self.plate_number = plate_number.lower()

    def validate_plate(self):
        """ Validate if the plate has the format 3 letters (no ñ-Ñ) and 3 numbers. 
            input : self
            output : boolean"""
        is_valid = True

        # check if the plate has the right length
        len_plate = len(self.plate_number)
        # it shouldn't be more or less than six numbers
        if (len_plate != 6):
            print(f'The lenght of the plate number is more than 6. It has {len_plate} numbers!.')
            is_valid = False

        else:
            for i,number in enumerate(self.plate_number):
                # first 3 characters should be letters and not ñ
                if i >= 0 and i < 3:
                    is_letter = (number.isalpha() and number != 'ñ')
                    # break condition and suggestion about the error
                    if not is_letter:
                        print('The plate has not a valid format. Remember LLL### with no ñ. There is not 3 letters.')
                        is_valid = False
                        break 
                else:
                    # last 3 characters should be numbers
                    is_number = number.isnumeric()
                    # break condition and suggestion about the error
                    if not is_number:
                        print('The plate has not a valid format. Remember LLL### with no ñ. There is not 3 numbers.')
                        is_valid = False
                        break
        return is_valid



            



def main():
    args = parser.parse_args()
    print(True)

if __name__ == "__main__":
    main()