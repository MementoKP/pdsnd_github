import time
import pandas as pd
import numpy as np

# We give the diferents options for each argument

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_NAMES = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

WEEKDAY_NAMES = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city_selection = ''
    while city_selection.lower() not in CITY_DATA:
        city_selection = input("\nWhich city would you like to select? chicago, new york city or washington?\n")
        if city_selection.lower() in CITY_DATA:
            city=city_selection.lower()
            #if we get the right city name
            print("\nPerfect, let's continue\n")
        else:
            #If we don't get a valid answer
            print("\nWe are sorry, you have selected a not valid input. Please, try again.\n")

    # TO DO: get user input for month (all, january, february, ... , june)

    month_selection = ''
    while month_selection.lower() not in MONTH_NAMES:
        month_selection = input("\nWhich month would you like to select? january, february, march, april, may, june or all\n")
        if month_selection.lower() in MONTH_NAMES:
            month = month_selection.lower()
            #if we get the right month name
            print("\nPerfect, let's continue\n")
        else:
            #If we don't get a valid answer
            print("\nWe are sorry, you have selected a not valid input. Please, try again.\n")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    day_selection = ''
    while day_selection.lower() not in WEEKDAY_NAMES:
        day_selection = input("\nWhich day would you like to select? monday, tuesday, wednesday, thursday, friday, saturday, sunday or all\n")
        if day_selection.lower() in WEEKDAY_NAMES:
            day = day_selection.lower()
            print("\nPerfect, let's continue\n")
            #if we get the right month name
        else:
            #If we don't get a valid answer
            print("\nWe are sorry, you have selected a not valid input. Please, try again.\n")

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

# load data file csv and turn it to dataframe

    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time to datetime

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # # extract month and day of week from Start Time and create new columns. We extract hour too to answer the most common hour later.

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # Now is time to filter by months and getting the integers from the months index:

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # New df

        df = df[df['month'] == month]

    # Time to filter by days.

    if day != 'all':
        # New df

        ddf = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):

    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month. We can get it using the mode function.

    common_month = df['month'].mode()[0]
    print(common_month)

    # TO DO: display the most common day of week. We can get it using the mode function.

    common_day_of_week = df['day_of_week'].mode()[0]
    print("\nThe most common day of week is: \n" + str(common_day_of_week))

    # TO DO: display the most common start hour. We can get it using the mode function.

    common_start_hour = df['hour'].mode()[0]
    print("\nThe most common start hour is: \n" + str(common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station. We can get it using the mode function.

    common_start_station = df['Start Station'].mode()[0]
    print("\nThe most commonly used start station for your selection is: \n" + str(common_start_station))


    # TO DO: display most commonly used end station. We can get it using the mode function.

    common_end_station = df['End Station'].mode()[0]
    print("\nThe most commonly used end station for your selection is: \n" + str(common_end_station))

    # TO DO: display most frequent combination of start station and end station trip. We can get it using the mode function.

    df['combination'] = df['Start Station'] + ' to ' + df['End Station']
    frequent_combination = df['combination'].mode()[0]
    print("\nThe most frequent combination of start station and end station trip is : \n" + str(frequent_combination))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

   # TO DO: display total travel time. We can get it using the sum function.

    total_travel_duration = df['Trip Duration'].sum()
    print("\nThe total travel duration for your selection is: \n" + str(total_travel_duration))

    # TO DO: display mean travel time. We can get it using the mean function.

    mean_travel_duration = df['Trip Duration'].mean()
    print("\nThe mean travel time for your selection is: \n" + str(mean_travel_duration))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types. We can get it using the counting value function.

    user_types = df['User Type'].value_counts()
    print("\nThe user types counting for your selection is: \n" + str(user_types))

    #Pay atention that there is no gender or births info for Washington city so we have to exclude it for the next "to do" points.

    if city != 'washington':

        # TO DO: Display counts of gender. We can get it using the counting value function.

        gender = df['Gender'].value_counts()
        print("\nThe counting of user gender for your selection is: \n" + str(gender))

        # TO DO: Display earliest, most recent, and most common year of birth. We can get it using the min, max and mode functions.

        earliest_year_birth = df['Birth Year'].min()
        most_recent_year_birth = df['Birth Year'].max()
        most_common_year_birth = df['Birth Year'].mode()[0]
        print("\nEarliest birth for your selection is: {}\n".format(earliest_year_birth))
        print("\nMost recent birth for your selection is: {}\n".format(most_recent_year_birth))
        print("\nMost common birth for your selection is: {}\n".format(most_common_year_birth))
    else:
        print("\nThere is no personal user info for this city\n")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    #Now is time to give the chance to sroll 5 by 5 for more data info for the selection.

    x = 1
    while True:
        raw = input("n\nWould you like to see some raw data (5 raws)? Enter yes or no.\n")
        if raw.lower() == 'yes':
            x = x+5
            print(df[x:x+5])

        else:
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
