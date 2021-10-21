# Pico-Placa
The following repository is an Pico & placa predictor made in python.
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

