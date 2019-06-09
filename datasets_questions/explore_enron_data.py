#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import cPickle as pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))

# number of keys in the dict
print(len(enron_data))

# number of features for each person. To do this we first want to print out the name of the first person
print(enron_data.keys()[0])
# then we can access the features dict with that key
print "Number of features per person: ", len(enron_data["METTS MARK"])

# number of 'poi' features in the dataset
num_poi = 0
for key in enron_data:
	if enron_data[key]['poi'] == 1:
		num_poi += 1
print "Number of PoIs in this dataset:", num_poi

# number of PoI total
f = open("../final_project/poi_names.txt")
file_list = f.readlines()
file_list = file_list[2:] # we want [2:] because the first two lines are a URL and a whitespace
f.close()
print(len(file_list))

# from here on out I would like to see all of the names of the features for easy access whenever I run this file
print "Feature keys:", enron_data["PRENTICE JAMES"].keys()

# total stock belonging to James Prentice
print "James Prentice stock:", enron_data["PRENTICE JAMES"]["total_stock_value"]

# email messagers from Wesley Colwell to persons of interest
print "E-mails from Wesley Colwell to PoIs:", enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

# value of stock options exercised by Jeffrey K Skilling
print "Jeffrey K Skilling stock option value:", enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

# answer to who took home the most money
print "Skilling money: ", enron_data["SKILLING JEFFREY K"]["total_payments"]
print "Lay money: ", enron_data["LAY KENNETH L"]["total_payments"]
print "Fastow money: ", enron_data["FASTOW ANDREW S"]["total_payments"]

# let's see if we can't find some "unfilled" feature to see what the value is
print "Feature keys:", enron_data["PRENTICE JAMES"].values()

# number of people with a salary and a known e-mail address
num_people_with_salary = 0
num_known_email_addresses = 0
for key in enron_data:
	if enron_data[key]['salary'] != 'NaN':
		num_people_with_salary += 1

for key in enron_data:
	if enron_data[key]['email_address'] != 'NaN':
		num_known_email_addresses += 1
print "Number of people with salaries: ", num_people_with_salary
print "Number of people with known e-mail addresses: ", num_known_email_addresses

# number of people that have 'NaN' as a total payment (as both a raw number and percentage of whole dataset)
num_nan_total_payments = 0
for key in enron_data:
    if enron_data[key]["total_payments"] == "NaN":
        num_nan_total_payments += 1
        
print "Number of people with 'NaN' as total payment: ", num_nan_total_payments
print "As a percentage of the whole dataset: ", (float(num_nan_total_payments) / len(enron_data.keys())) * 100

# number of POIs that have 'NaN' as total payment
num_poi_nan_payments = 0
for key in enron_data:
    if enron_data[key]['poi'] == 1 and enron_data[key]["total_payments"] == "NaN":
        num_poi_nan_payments += 1
        
print "Number of POIs with 'NaN' as total payment: ", num_poi_nan_payments