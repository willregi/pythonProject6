#Author name: Regina Williams
#Github username: willregi
#Date: 2/1/2023

def fall_distance(fall_time):
    return 0.5 * 9.8 * fall_time * fall_time
    """Determine the distance an object falls due to gravity in a specific time period."""
time = float(input("Enter the amount of time for which the object is falling:"))
print("Distance the object has fallen is", fall_distance(time))