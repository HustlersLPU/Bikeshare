## import all necessary packages and functions.
import csv # read and write csv files
from datetime import datetime # operations to parse dates
from pprint import pprint # use to print data structures like dictionaries in
                          # a nicer way than the base print function.

def print_first_point(filename):
    """
    This function prints and returns the first data point (second row) from
    a csv file that includes a header row.
    """
    # print city name for reference
    city = filename.split('-')[0].split('/')[-1]
    print('\nCity: {}'.format(city))
    
    with open(filename, 'r') as f_in:
        ## TODO: Use the csv library to set up a DictReader object. ##
        ## see https://docs.python.org/3/library/csv.html           ##
        trip_reader =csv.DictReader(f_in)
        
        ## TODO: Use a function on the DictReader object to read the     ##
        ## first trip from the data file and store it in a variable.     ##
        ## see https://docs.python.org/3/library/csv.html#reader-objects ##
        #first_trip={}
        #for row in trip_reader:
            #first_trip=row
        first_trip=next(trip_reader)
       
        
        ## TODO: Use the pprint library to print the first trip. ##
        ## see https://docs.python.org/3/library/pprint.html     ##
        pprint(first_trip)
        
    # output city name and first trip for later testing
    return (city, first_trip)

# list of files for each city
data_files = ['NYC-CitiBike-2016.csv',
              'Chicago-Divvy-2016.csv',
              'Washington-CapitalBikeshare-2016.csv',]

# print the first trip from each file, store in dictionary
example_trips = {}
for data_file in data_files:
    city, first_trip = print_first_point(data_file)
    example_trips[city] = first_trip


def duration_in_mins(datum, city):
    """
    Takes as input a dictionary containing info about a single trip (datum) and
    its origin city (city) and returns the trip duration in units of minutes.
    
    Remember that Washington is in terms of milliseconds while Chicago and NYC
    are in terms of seconds. 
    
    HINT: The csv module reads in all of the data as strings, including numeric
    values. You will need a function to convert the strings into an appropriate
    numeric type when making your transformations.
    see https://docs.python.org/3/library/functions.html
    """
    
    # YOUR CODE HERE
   # duration=[]
    #datum=first_trip
    #example_trips=first_trip
    
    if city=='NYC':
        duration=float(datum['tripduration'])/60
    elif city=='Chicago':
        duration=float(datum['tripduration'])/60
    else:
        duration=float(datum['Duration (ms)'])/(1000*60)
    return duration



# Some tests to check that your code works. There should be no output if all of
# the assertions pass. The `example_trips` dictionary was obtained from when
# you printed the first trip from each of the original data files.
tests = {'NYC': 13.9833,
         'Chicago': 15.4333,
         'Washington': 7.1231}


def time_of_trip(datum, city):
    """
    Takes as input a dictionary containing info about a single trip (datum) and
    its origin city (city) and returns the month, hour, and day of the week in
    which the trip was made.
    
    Remember that NYC includes seconds, while Washington and Chicago do not.
    
    HINT: You should use the datetime module to parse the original date
    strings into a format that is useful for extracting the desired information.
    see https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
    """
    
    # YOUR CODE HERE
    if city=='NYC':
        datetime_object=datetime.strptime((datum['starttime']),'%m/%d/%Y %H:%M:%S')
        month=int(datetime_object.strftime('%m'))
        hour=int(datetime_object.strftime('%H'))
        day_of_week=datetime_object.strftime('%A')
        return(datetime_object.month,datetime_object.hour,day_of_week)
    elif city=='Chicago':
        datetime_object2=datetime.strptime((datum['starttime']),'%m/%d/%Y %H:%M')
        month=int(datetime_object2.strftime('%m'))
        hour=int(datetime_object2.strftime('%H'))
        day_of_week=datetime_object2.strftime('%A')
        return(datetime_object2.month,datetime_object2.hour,day_of_week)
    else:
        datetime_object3=datetime.strptime((datum['Start date']),'%m/%d/%Y %H:%M')
        month=int(datetime_object3.strftime('%m'))
        hour=int(datetime_object3.strftime('%H'))
        day_of_week=datetime_object3.strftime('%A')
        return (datetime_object3.month, datetime_object3.hour, day_of_week)
    


# Some tests to check that your code works. There should be no output if all of
# the assertions pass. The `example_trips` dictionary was obtained from when
# you printed the first trip from each of the original data files.
tests = {'NYC': (1, 0, 'Friday'),
         'Chicago': (3, 23, 'Thursday'),
         'Washington': (3, 22, 'Thursday')}

for city in tests:
    assert time_of_trip(example_trips[city], city) == tests[city]



def type_of_user(datum, city):
    """
    Takes as input a dictionary containing info about a single trip (datum) and
    its origin city (city) and returns the type of system user that made the
    trip.
    
    Remember that Washington has different category names compared to Chicago
    and NYC. 
    """
    
    # YOUR CODE HERE
    #user_type=[]
    if city=='NYC':
        user_type=str(datum['usertype'])
    elif city=='Chicago':
        user_type=str(datum['usertype'])
    else:
        if datum['Member Type']=='Registered':
            user_type='Subscriber'
        else:
            user_type='Customer'
    return user_type


# Some tests to check that your code works. There should be no output if all of
# the assertions pass. The `example_trips` dictionary was obtained from when
# you printed the first trip from each of the original data files.
tests = {'NYC': 'Customer',
         'Chicago': 'Subscriber',
         'Washington': 'Subscriber'}

for city in tests:
    assert type_of_user(example_trips[city], city) == tests[city]



def condense_data(in_file, out_file, city):
    """
    This function takes full data from the specified input file
    and writes the condensed data to a specified output file. The city
    argument determines how the input file will be parsed.
    
    HINT: See the cell below to see how the arguments are structured!
    """
    
    with open(out_file, 'w') as f_out, open(in_file, 'r') as f_in:
        # set up csv DictWriter object - writer requires column names for the
        # first row as the "fieldnames" argument
        out_colnames = ['duration', 'month', 'hour', 'day_of_week', 'user_type']        
        trip_writer = csv.DictWriter(f_out, fieldnames = out_colnames)
        trip_writer.writeheader()
        
        ## TODO: set up csv DictReader object ##
        trip_reader =list(csv.DictReader(f_in))

        # collect data from and process each row
        for row in trip_reader:
            # set up a dictionary to hold the values for the cleaned and trimmed
            # data point
            new_point ={}
            
            ## TODO: use the helper functions to get the cleaned data from  ##
            ## the original data dictionaries.                              ##
            ## Note that the keys for the new_point dictionary should match ##
            ## the column names set in the DictWriter object above.         ##
            new_point['duration']=duration_in_mins(row,city)
            new_point['hour']=time_of_trip(row,city)[1]
            #new-point['hour']=time_of_trip(row,city)
            new_point['day_of_week']=time_of_trip(row,city)[2]
            new_point['user_type']=type_of_user(row,city)
            
           
            trip_writer.writerow(new_point)
            
# Run this cell to check your work
city_info = {'Washington': {'in_file': 'Washington-CapitalBikeshare-2016.csv',
                            'out_file': 'Washington-2016-Summary.csv'},
             'Chicago': {'in_file': 'Chicago-Divvy-2016.csv',
                         'out_file': 'Chicago-2016-Summary.csv'},
             'NYC': {'in_file': 'NYC-CitiBike-2016.csv',
                     'out_file': 'NYC-2016-Summary.csv'}}

for city, filenames in city_info.items():
    condense_data(filenames['in_file'], filenames['out_file'], city)
    print_first_point(filenames['out_file'])



def number_of_trips(filename):
    """
    This function reads in a file with trip data and reports the number of
    trips made by subscribers, customers, and total overall.
    """
    with open(filename, 'r') as f_in:
        # set up csv reader object
        
        # initialize count variables
        reader = csv.DictReader(f_in)
        n_subscribers = 0
        n_customers = 0
        #length_subs= 0
        #length_cust= 0
        #n_c=0
        n=0
        m=0
        # tally up ride types
        for row in reader:
            if row['user_type'] == 'Subscriber':
                n_subscribers += 1
                #length_subs+=float(row['duration'])
            elif row['user_type']=='Customer':
                n_customers += 1
            elif row['user_type']=='Registered':
                n+=1
                #n=subscriber
            else:
                m+=1
                #m=customer
                
               # length_cust+=float(row['duration'])
        
        # compute total number of rides
        n_total = n_subscribers + n_customers+n+m
        
        #average_subs=length_subs/n_subscribers
        #average_cust=length_cust/n_customers
        sp1=n/n_total
        cp1=m/n_total
        subs_prop=(n_subscribers/n_total)*100
        cust_prop=(n_customers/n_total)*100
        # return tallies as a tuple
        #print(n_total)
        return(n_subscribers, n_customers,n,m,n_total,subs_prop,cust_prop,sp1,cp1)

#######
data_files=['NYC-2016-Summary.csv',
'Chicago-2016-Summary.csv',
'Washington-2016-Summary.csv']
            
#data_file = './examples/BayArea-Y3-Summary.csv'

for data_file in data_files:
    print(number_of_trips(data_file))




def city_analysis(filename):
    with open(filename,'r') as f_in:
        reader=csv.DictReader(f_in)
        n1_subs=0
        n1_cust=0
        total_subs_duration=0
        total_cust_duration=0
        for row in reader:
            user_type=row['user_type']
            duration=float(row['duration'])
            if user_type=='subscriber':
                n1_subs+=1
                total_subs_duration+=duration
            elif user_type=='Customer':
                n1_cust+=1
                total_cust_duration+=duration
            
          
        average_subs=total_subs_duration/n1_subs
        average_cust=total_cust_duration/n1_cust
        #print(n1_subs,n1_cust,average_subs,_average_cust)
        return(n1_subs,n1_cust,average_subs,average_cust)
        




data_file_city='NYC-2016-Summary.csv'
#data_file_city[4]=n_ave_subscriber
#data_file_city[5]=n_ave_customers
for data_file in data_file_city:
    print(city_analysis(data_file))

    
                                 
def data_analysis_city(filename,city):
	
