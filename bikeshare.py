import time
import pandas as pd
import numpy as np
import statistics

"""
TO_DO:
- handle extraneous user input later for city and date filtering
(see lesson referenced in 3.code walkthrough)
"""

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ['chicago', 'new york', 'washington']
    city = input("Would you like to see information for Chicago, New York, or Washington?\n")
    city = city.lower()
    while (city not in cities):
        city = input("Sorry, that is not a valid city, please check your spelling and enter a valid city to proceed.\n")
        city = city.lower()

    # get user input for month (all, january, february, ... , june)
    date = input("Would you like to filter your data by month? (yes or no)\n")
    date = date.lower()

    elig_input = ['yes', 'y', 'no', 'n']
    while (date not in elig_input):
        date = input("Sorry, that is not a valid response, please respond 'yes' or 'no':")
        date = date.lower()

    month = 'all'
    if date == 'yes' or date == 'y':
        month = input("Which month, January, February, March, April, May, or June?\n")
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = month.lower()
        while (month not in months):
            month = input("Sorry, that is an invalid month, please input one of the following months:['January', 'February', 'March', 'April', 'May', 'June']:\n")
            month = month.lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)

    date = 'new'
    date = input("Would you like to filter your data by day of the week? (yes or no)\n")
    date = date.lower()

    elig_input = ['yes', 'y', 'no', 'n']
    while (date not in elig_input):
        date = input("Sorry, that is not a valid response, please respond 'yes' or 'no':")
        date = date.lower()

    day = 'all'
    if date == 'yes' or date == 'y':
        day = input("Which day of the week (please input as 'Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday')\n")
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day = day.lower()
        while(day not in days):
            day = input("Sorry, that is an invalid day, please input a valid day of the week:")
            day = day.lower()
    day = day.lower()

    print (city, month, day)

    print('-'*40)
    return city, month, day


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['weekday_name'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['weekday_name'] == day.title()]

    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("The most common month is: %i." % statistics.mode(df['month']))

    # display the most common day of week
    print("The most common day of the week is: %s." % statistics.mode(df['weekday_name']))

    # display the most common start hour
    print("The most common hour is: %i." % statistics.mode(df['hour']))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("The most common start station is: %s" % statistics.mode(df['Start Station']))


    # display most commonly used end station
    print("The most common end station is: %s" % statistics.mode(df['End Station']))


    # display most frequent combination of start station and end station trip
    df['Round Trip'] = df['Start Station'] + ", " + df['End Station']
    print("The most common combination of start and end station is: %s" % statistics.mode(df['Round Trip']))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("The total travel time for these rides is: %i minutes" % (df['Trip Duration'].sum()/60 + df['Trip Duration'].sum() % 60))


    # display mean travel time
    print("The mean travel time for these rides is %i minutes" % (df['Trip Duration'].mean()/60 + df['Trip Duration'].mean() % 60))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("Total users by type:\n")
    print(df['User Type'].value_counts())
    print("\n")

    # Display counts of gender
    print("Total users by gender:\n")
    print(df['Gender'].value_counts())
    print("\n")


    # Display earliest, most recent, and most common year of birth
    print("The earliest, most recent, and most common year of birth is %i, %i, and %i, respectively"
    % (df['Birth Year'].min(), df['Birth Year'].max(), statistics.mode(df['Birth Year'])))
    print("\n")



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
