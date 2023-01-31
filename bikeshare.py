import time
import pandas as pd
import numpy as np
#Made by Yasser Al-Ali
#31/1/2023
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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Which city would you like to choose?").lower()
        # city = 'chicago'
        if city not in ('chicago', 'new york city', 'washington'):
            print("This city doesn't exist, please try again")
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Which month would you like to choose?").lower()
        # month = 'may'
        if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            print("This month is not included, please try again")
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Which day would you like to choose?").lower()
        # day = 'sunday'
        if day not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'):
            print("This day doesn't exist, please try again")
            continue
        else:
            break

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
    months = ('january', 'february', 'march', 'april', 'may', 'june', 'all')
    days = ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all')

    df = pd.read_csv(CITY_DATA[city])
    # print("flag 1: Before ", df.shape[0])
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["month"] = df["Start Time"].dt.month_name()
    df["month"] = df['month'].str.lower()
    df["week day"] = df["Start Time"].dt.day_name()
    df['week day'] = df['week day'].str.lower()
    df['Start Hour'] = df['Start Time'].dt.hour

    
    if month != 'all':
    
        df = df[df['month'] == month]
 
        
        
    if day != 'all':
       
        df = df[df['week day'] == day]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df["month"].mode()[0]
    # print("flag 1211212121212")
    # print(df.mode()['month'])
    # common_month = df.mode()['month'][0]
    print("The most common month is ", common_month)

    # TO DO: display the most common day of week
    common_day = df["week day"].mode()[0]
    print("The most common day is ", common_day)

    # TO DO: display the most common start hour
    df["hour"] = df["Start Time"].dt.hour
    common_hour = df["hour"].mode()[0]
    print("The most common hour is ", common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df["Start Station"].value_counts().idxmax()
    print("The most commonly used start station is ", start_station)

    # TO DO: display most commonly used end station
    end_station = df["End Station"].value_counts().idxmax()
    print("The most commonly used end station is ", end_station)

    # TO DO: display most frequent combination of start station and end station trip
    common_combination = df.groupby(["Start Station", "End Station"]).count()
    print("The most commonly used combination of stations is ", common_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df["Trip Duration"].sum()
    print("The total travel time is ", total_time)

    # TO DO: display mean travel time
    mean_time = df["Trip Duration"].mean()
    print("The mean travel time is ", mean_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""
    if city == 'washington':
        return
    else:
        print('\nCalculating User Stats...\n')
        start_time = time.time()

        # TO DO: Display counts of user types
        user_type = df["User Type"].nunique()
        print("The counts of user types is ", user_type)

        # TO DO: Display counts of gender
        gender = df["Gender"].nunique()
        print("The counts of genders are ", user_type)

        # TO DO: Display earliest, most recent, and most common year of birth
        earliest = df["Birth Year"].min()
        recent = df["Birth Year"].max()
        common = df["Birth Year"].mode()
        print("The earliest, most recent, and most common year of birth are ", earliest, recent, common)

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)

def display_data(df):
    """Display 5 rows at a time"""
    view_data = input('\n would you like to view 5 rows of data? [Y]es, or [N]o').capitalize()
    start_index=0
    while(view_data=='Y'):
        print(df.iloc[start_index:start_index+5])
        print("flag 11")

        start_index+=5
        view_data = input("continue? [Y]/[N]").capitalize()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        # df.head(10)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print("Thank you, and have a nice day")
            break


if __name__ == "__main__":
    main()