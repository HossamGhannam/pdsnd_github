import time
import pandas as pd
import numpy as np

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
    city = None
    city = input("Please enter one of the following city (Chicago, New York City or Washington): \n").lower()
    #validating the user entry
    while city.lower() not in ['chicago', 'new york city', 'washington']:
        print('Sorry, you entered a city that does not exists! Please try again \n')
        city = input("Please enter one of the following city (Chicago, New York City or Washington), again: \n").lower()

    # get user input for month (all, january, february, ... , june)
    month = None
    month = input("Please enter a month (january, february, march, april, may, june), or enter all (for all months): \n").lower()
    #validating the user entry
    while month not in ['all','january', 'february', 'march', 'april', 'may', 'june']:
        print('Sorry, you entered a month that does not exists! Please try again')
        month = input("Please enter a month (january, february, march, april, may, june), or enter all (for all months) again: \n").lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = None
    day = input("Please enter a day (saturday, sunday, monday, tuesday, wednesday, thursday, friday), or all (for all days) : \n").lower()
    #validating the user entry
    while day not in ['all', 'saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']:
        print('Sorry, you entered a day that does not exists! Please try again\n')
        day = input("Please enter a day (saturday, sunday, monday, tuesday, wednesday, thursday, friday), or all (for all days) : \n").lower()

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
     # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()
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
        df = df[df['day'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print("The most common month is: ", common_month)

    # display the most common day of week
    common_day = df['day'].mode()[0]
    print("The most common day is: ", common_day)

    # display the most common start hour
    common_start_hour = df['hour'].mode()[0]
    print("The most common start hour is: ", common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("The most common start station is: ", common_start_station)


    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("The most common end station is: ", common_end_station)


    # display most frequent combination of start station and end station trip
    df['start_end_station_combined'] = df['Start Station'] + ' - ' + df['End Station']
    frequent_start_end_station = df['start_end_station_combined'].mode()[0]
    print("The most frequent combination of start station and end station trip is: ", frequent_start_end_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total tavel time is: ", round(total_travel_time), 'sec.')

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time is: ', round(mean_travel_time), 'sec.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    count_user_types = df['User Type'].value_counts().to_string()
    print('Count of user types:\n', count_user_types)

    # Display counts of gender
    if 'Gender' in df.columns:
        count_gender = df['Gender'].value_counts().to_string()
        print('\nCounts of gender:\n',count_gender)
    else:
        print('\nGender Info Does Not Exists!\n')



    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birth = df['Birth Year'].min()
        print("\nEarliest year of birth is: ",int(earliest_birth))
        recent_birth = df['Birth Year'].max()
        print("Recent year of birth is: ",int(recent_birth))
        common_birth = df['Birth Year'].mode()[0]
        print("Most common year of birth is: ",int(common_birth))
    else:
        print('Year of Birth Info Does Not Exists!\n')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        DisplayCounter = 0

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        DisplayData = input('\nWould you like to see more data? Enter yes or no\n')
        while DisplayData.lower() in 'yes':
            pd.set_option('display.max_columns',200)
            print(df.iloc[DisplayCounter : DisplayCounter + 5])
            DisplayCounter = DisplayCounter + 5
            DisplayData = input('\nWould you like to see more data? Enter yes or no Please\n')

        restart = input('\nWould you like to restart? Enter yes or no Please.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
