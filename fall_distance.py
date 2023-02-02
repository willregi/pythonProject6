#Author name: Regina Williams
#Github username: willregi
#Date: 2/1/2023

def fall_distance(fall_time):
    return 0.5 * 9.8 * fall_time * fall_time
    dist = fall_distance(4.5)
    #"""Determine the distance an object falls due to gravity in a specific time period."""
time = float(input("Fall time:"))
print("dist", fall_distance(time))