# Hacker Rank
# Given the time in numerals we may convert it into words

hour = int(input())
mins = int(input())

hour_list = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve']

mins_list = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'quarter', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'twenty one', 'twenty two', 'twenty three', 'twenty four', 'twenty five', 'twenty six', 'twenty seven', 'twenty eight', 'twenty nine', 'half']

time_str = ''

if mins <= 30:
    if mins == 0:
        time_str = '{} o\' clock'.format(hour_list[hour])
    elif mins == 15 or mins == 30:
        time_str = '{} past {}'.format(mins_list[mins], hour_list[hour])
    elif mins == 1:
        time_str = '{} minute past {}'.format(mins_list[mins], hour_list[hour])
    else:
        time_str = '{} minutes past {}'.format(mins_list[mins], hour_list[hour])
    print(time_str)

else:
    hour += 1
    mins = 60 - mins

    if mins == 15:
        time_str = '{} to {}'.format(mins_list[mins], hour_list[hour])
    else:
        time_str = '{} minutes to {}'.format(mins_list[mins], hour_list[hour])
    print(time_str)