""" Pico&Plate predictor
It takes a license plate number (the full number), a date and a time.
Then it determines if the car can be in the road.

pico_placa,py <plate_number> <date> <time>"""


import argparse

parser = argparse.ArgumentParser(description='Determine if a car should be in the road based on Pico&Placa')
parser.add_argument('plate_number', type=str, help='full number of the plate')
parser.add_argument('date', type=str, help='date of the query in format Year-Month-Day')
parser.add_argument('time', type=str, help='time of the query in format Hour:Minute')

args = parser.parse_args()