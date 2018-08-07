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

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Would you like to see data for chicago,new york city,or washington?').lower()
    while city not in [ 'chicago','new york city','washington'] :
        city=input('Hello!The city you choose seems not in the US bikeshare data,please choose the city again.').lower()

	

    # TO DO: get user input for month (all, january, february, ... , june)

    month = input('Which month?january,february,march,april,may,june,or all?').lower()
    while month not in [ 'january','february','march','april','may','june','all'] :
        month = input('Hello!The month you choose seems not right,please choose the month again.').lower()
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day=input('Which day?monday,tuesday,wednesday,thursday,friday,saturday,sunday,or all?').lower()
    while day not in [ 'monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']:
        day = input('Hello!The day you choose seems not right,please choose the day again.').lower()
    print('-'*40)
    return city,month,day


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
    df = pd.read_csv(CITY_DATA[city]) 
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        months=['january','february','march','april','may','june']
        month=months.index(month)+1
        df=df[df['month']==month]
    if day != 'all':
        df=df[df['day_of_week']==day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    month_popular=df['month'].mode()[0]
    month_popular_count=df[df['month']==month_popular].count()[0]
    print('Most popular month:{},Count:{}'.format(month_popular,month_popular_count))

    # TO DO: display the most common day of week
    week_popular=df['day_of_week'].mode()[0]
    week_popular_count=df[df['day_of_week']==week_popular].count()[0]
    print('Most popular week:{},Count:{}'.format(week_popular,week_popular_count))
	
    # TO DO: display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    hour_popular=df['hour'].mode()[0]
    hour_popular_count=df[df['hour']==hour_popular].count()[0]
    print('Most popular hour:{},Count:{}'.format(hour_popular,hour_popular_count))
    #print('Filter:city is {} ,month is {},day is {}'.format(city,month,day))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station_popular=df['Start Station'].mode()[0]
    start_station_popular_count=df[df['Start Station']==start_station_popular].count()[0]
    print('Start Station:{},Count:{}'.format(start_station_popular,start_station_popular_count))
    # TO DO: display most commonly used end station
    end_station_popular=df['End Station'].mode()[0]
    end_station_popular_count=df[df['End Station']==end_station_popular].count()[0]
    print('End Stationt Station:{},Count:{}'.format(end_station_popular,end_station_popular_count))
    # TO DO: display most frequent combination of start station and end station trip
    df['combination_station']='Start Station:'+df['Start Station']+'   End Station:'+df['End Station']
    #print(df.head())
    combination_station_popular=df['combination_station'].mode()[0]
    combination_station_popular_count=df[df['combination_station']==combination_station_popular].count()[0]
    print('Combination_station_popular:{},Count:{}'.format(combination_station_popular,combination_station_popular_count))
    #print('\nThis took %s seconds.' % (time.time() - start_time))
    #print('-'*40)




def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['travle time']=(pd.to_datetime(df ['End Time'])-pd.to_datetime(df ['Start Time'])).dt.total_seconds() 
    total_travel_time=df['travle time'].sum()
    print('Total travel time:',total_travel_time,'seconds')
    # TO DO: display mean travel time
    mean_travel_time=df['travle time'].mean()
    print('Mean travel time:',mean_travel_time,'seconds')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(city,df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('What is the breakdown of users?')
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    if city != 'washington':
        print('What is the breakdown of gender?')
        user_gender = df['Gender'].value_counts()
        print(user_gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    if city != 'washington':
        print('What is the oldest,youngest,and most popular year of birth respectively?')
        user_min_year = df['Birth Year'].min()
        user_max_year = df['Birth Year'].max()
        user_popular_year = df['Birth Year'].mode()[0]
        print(user_min_year,user_max_year,user_max_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(city,df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
