# Pico-Placa
The following repository is an Pico & placa predictor made in python.

Pico&Placa is a way to control the vehicle traffic in Quito. The following repository take all the rules exposed in
https://revistas.uide.edu.ec/index.php/innova/article/view/300/309 which defines when a vehicle can be on the road or not.

This rules are:
restricted schedule: from 7:00 to 9:00, and from 16:00 to 19:30. \
restricted vehicles according to the last digit in its license plate.

Monday : 1,2
Tuesday : 3,4
Wednesday: 5,6
Thursday: 7,8
Friday: 9,0

Vehicles that are between these rules are not allowed to be on the road.

To test the code you will need to follow these steps:

Install the dependencies:
```bash
pip install -r requirements.txt
```
Then, excecute the command:
```bash
python pico_placa.py -h
```
This will output all the info for the right arguments. In an overview
the program needs:
```bash
python pico_placa.py <plate_number> <date> <time>
```
where:

**plate_number** -> It is a string of 7 characters representing the plate number with no hyphen. (Following the format for the most common plates in Ecuador 3 letters, no ñ, and 4 numbers) *Ex: PCR1274*. \
**date** -> It is a string with the evaluation date for the Pico&Placa restriction. The format expected is YYYY_mm_dd.\
**time** -> It is a string with the time to evaluate the restriction. The format is HH:MM.

The ouput of the program is:\
**True** if the car is allowed to be on the road.
**False** if the car is not allowed to be on the road due to restrictions.

An automatic test is included locally and in the Github repository. For the local test, you need to run:
```bash
pytest
```
It will excecute all the proposed unit test for the Pico&Placa predictor. Then, in the cloud you can see the unit test before merging in the Github actions tab of the repository. 

