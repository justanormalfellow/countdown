import time


def countdown(result, current_time):
    '''
    This function basically gets the time difference in seconds and
    divide the value between year, day, hour and so on using division
    and the modulus "%" by using the divmod function.

    '''
    time_diff = result - current_time
    if time_diff < 0:
        print("haha very funny")
    
    # Convert the time difference to a human-readable format
    days, remainder = divmod(time_diff, 86400)
    hours, remainder = divmod(remainder, 3600)   
    minutes, seconds = divmod(remainder, 60)     

    print(f"Time difference: {int(days)} days, {int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds.")


current_time_tuple = time.localtime() # get struct_time of time of debugg
current_time_unix = time.mktime(current_time_tuple) #turns to unix time for calculations

time_after = input("Give a date (e.x '12 August, 2036'): ")
print()

result = time.strptime(time_after, "%d %B, %Y") #stores values as time tuple 
result_unix = time.mktime(result) #turns user's date into time tuple


while True:
    countdown(result_unix, current_time_unix)
    current_time_unix = time.time() #updates time

    # Check if the time difference reaches zero
    if current_time_unix >= result_unix:
        print("Time difference reached zero.")
        break

    time.sleep(1)  # Update every second
