import value_return

def get_time():

    epoch_seconds = int(input("Please enter the Epoch time: "))
    hour = value_return.get_hour(epoch_seconds)
    minute = value_return.get_minutes(epoch_seconds)
    second = value_return.get_seconds(epoch_seconds)

    print("{:02d}".format(hour) + ":" + "{:02d}".format(minute) + ":" + "{:02d}".format(second))
