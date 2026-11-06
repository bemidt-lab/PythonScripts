# User-defined function to calculate total uptime
def calculate_total_uptime(hours_day1, hours_day2, hours_day3, hours_day4, hours_day5):
    total_uptime = hours_day1 + hours_day2 + hours_day3 + hours_day4 + hours_day5
    return total_uptime

# Call the function with recorded daily uptime values
weekly_uptime = calculate_total_uptime(24, 24, 23, 24, 22)

# Display the returned result
print("Total weekly server uptime (hours):", weekly_uptime)