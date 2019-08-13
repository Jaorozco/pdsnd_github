"""
Udacity Bikeshare Python Project
Author: Juan Orozco
Date:July 31st 2019
"""
import time
import pandas as pd
import numpy as np

city_info = { 'new york city': 'new_york_city.csv',
             'chicago': 'chicago.csv',
              'washington': 'washington.csv' }

def filters_setup():
    """
    Asks user to specify a city, month, and day to analyze.

    IT returns:
        (str) city - name of the city 
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    print('Data is available for Chicago, New York City, or Washington')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Please input the city name: ").lower()
          
    while city not in ['chicago', 'new york city', 'washington']:
        city = input(
        "The city you provided is not valid! Please select another city: ").lower()

    # get user input for month (all, january, february, ... , june)
    month = input("Please enter the month you desire to analyze: ").lower()
    
    while month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
        month = input(
        "Month requested is not available! Please select another month: ").lower()
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Please enter name of the day of the week you wish to analyze: ").lower()
    
    while day not in ['all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']:
        day = input(
        "Day requested is not available! Please input another day: ").lower()

    print('-'*40)
    return city, month, day
          

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(city_info[city])

    # Convert the Start and End Time columns to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].apply(lambda x: x.month)
    df['day_of_week'] = df['Start Time'].apply(lambda x: x.strftime('%A').lower())

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df.loc[df['month'] == month,:]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df.loc[df['day_of_week'] == day,:]

    return df

def time_info(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("The most common month for our data is: {}".format(
        str(df['month'].mode().values[0]))        )

    # display the most common day of week
    print("The most common day of the week for our data is: {}".format(
        str(df['day_of_week'].mode().values[0])))

    # display the most common start hour
    df['start_hour'] = df['Start Time'].dt.hour
    print("The most common start hour for our data is: {}".format(
        str(df['start_hour'].mode().values[0])))

    print("\nThe analysis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def station_info(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("The most common start station is: {} ".format(
        df['Start Station'].mode().values[0])
    )

    # display most commonly used end station
    print("The most common end station is: {}".format(
        df['End Station'].mode().values[0])
    )

    # display most frequent combination of start station and end station trip
    df['routes'] = df['Start Station']+ " " + df['End Station']
    print("The most common start and end station combo is: {}".format(
        df['routes'].mode().values[0])
    )

    print("\nThe analysis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_data(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    df['duration'] = df['End Time'] - df['Start Time']
    # display total travel time
    print("The total travel time is: {}".format(
        str(df['duration'].sum()))
    )

    # display mean travel time
    print("The mean travel time is: {}".format(
        str(df['duration'].mean()))
    )

    print("\nThe analysis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_info(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("Below is the breakdown of users by type:")
    print(df['User Type'].value_counts())

    # Display counts of gender
    if city in ['chicago', 'new york city']:
        # Display counts of gender
        print("Below are the demographics by Gender:")
        print(df['Gender'].value_counts())

        # Display earliest, most recent, and most common year of birth
        print("The earliest birth year in the data is: {}".format(
            str(int(df['Birth Year'].min())))
        )
        print("The latest birth year in the data is: {}".format(
            str(int(df['Birth Year'].max())))
        )
        print("The most common birth year in the data is: {}".format(
            str(int(df['Birth Year'].mode().values[0])))
        )

    # Display earliest, most recent, and most common year of birth
    print("\nThe analysis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_rawdata(df):
    """Displays the numbers of rows desired by the user"""   
    
    start_row = 0
    end_row = 5
    
    display_active = input("Do you want to see 5 rows of raw data? Enter yes or no:").lower()
    
    if display_active == 'yes':
       while end_row <= df.shape[0] - 1:
        
            print(df.iloc[start_row:end_row,:])
            start_row += 5
            end_row += 5
            
            end_display = input("Do you wish to continue seeing data? Enter yes or no: ").lower()
            if end_display == 'no':
                break
    
def main():
    while True:
        city, month, day = filters_setup()
        df = load_data(city, month, day)

        time_info(df)
        station_info(df)
        trip_duration_data(df)
        user_info(df, city)
        display_rawdata(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()