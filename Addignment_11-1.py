"""
Assignment 11: Pandas Table with Temperature Data
Submitted by Zainab Abdulhasan
Submitted: December 06, 2024
"""



import pandas as pd

# Dictionaries for DAYS and HOURS
DAYS = {
    0: "SUN",
    1: "MON",
    2: "TUE",
    3: "WED",
    4: "THU",
    5: "FRI",
    6: "SAT"
}

HOURS = {
    0: "Mid-1AM  ",
    1: "1AM-2AM  ",
    2: "2AM-3AM  ",
    3: "3AM-4AM  ",
    4: "4AM-5AM  ",
    5: "5AM-6AM  ",
    6: "6AM-7AM  ",
    7: "7AM-8AM  ",
    8: "8AM-9AM  ",
    9: "9AM-10AM ",
    10: "10AM-11AM",
    11: "11AM-NOON",
    12: "NOON-1PM ",
    13: "1PM-2PM  ",
    14: "2PM-3PM  ",
    15: "3PM-4PM  ",
    16: "4PM-5PM  ",
    17: "5PM-6PM  ",
    18: "6PM-7PM  ",
    19: "7PM-8PM  ",
    20: "8PM-9PM  ",
    21: "9PM-10PM ",
    22: "10PM-11PM",
    23: "11PM-MID ",
}

# Predefined temperature data for full accuracy
TEMPERATURES = [
    [68.8, 68.4, 72.7, 71.3, 70.6, 70.7, 66.8],
    [69.0, 68.3, 72.5, 71.1, 70.3, 70.5, 66.9],
    [69.1, 68.3, 72.3, 70.9, 70.0, 70.4, 67.0],
    [69.2, 68.1, 72.2, 70.8, 69.8, 70.3, 67.0],
    [69.2, 68.1, 72.1, 70.6, 69.7, 70.1, 67.1],
    [69.2, 68.0, 72.1, 70.5, 69.6, 70.0, 67.1],
    [68.8, 67.9, 72.1, 70.1, 69.4, 69.6, 67.1],
    [68.1, 68.1, 71.8, 70.0, 69.5, 69.2, 67.1],
    [67.4, 68.1, 71.1, 69.5, 69.7, 68.3, 67.1],
    [67.3, 69.1, 71.5, 69.4, 70.6, 67.1, 67.2],
    [67.1, 70.4, 72.3, 69.9, 71.5, 66.6, 67.2],
    [66.9, 70.9, 73.2, 70.4, 72.2, 66.6, 66.6],
    [66.8, 71.2, 73.1, 71.3, 72.1, 66.3, 65.9],
    [66.7, 71.9, 73.6, 72.3, 71.9, 66.1, 65.5],
    [66.9, 72.8, 74.3, 73.1, 72.3, 66.1, 65.2],
    [66.7, 73.3, 74.7, 74.0, 72.7, 66.1, 65.0],
    [66.7, 73.8, 75.1, 74.4, 73.4, 66.0, 64.9],
    [66.7, 74.2, 75.7, 74.9, 74.0, 66.0, 64.9],
    [66.7, 73.5, 75.1, 74.6, 73.5, 65.8, 64.8],
    [67.2, 73.4, 74.0, 73.4, 72.5, 65.7, 64.8],
    [67.8, 73.4, 73.0, 72.6, 71.7, 65.4, 64.7],
    [68.1, 73.3, 72.2, 71.7, 71.1, 65.5, 64.9],
    [68.3, 73.2, 71.8, 71.3, 70.9, 66.3, 65.5],
    [68.6, 73.0, 71.5, 70.9, 70.8, 66.6, 65.7],
]

# Function to print the temperature table
def print_temp_by_day_time():
    """
    Prints a table showing average temperatures for each day of the week and hour of the day.

    This function uses Pandas to display a formatted table of temperatures. The data is
    dynamically labeled with DAYS and HOURS dictionaries and formatted for accurate output.
    """
    # Create a DataFrame with the preloaded temperature data
    temp_df = pd.DataFrame(TEMPERATURES, columns=[DAYS[i] for i in range(7)], index=[HOURS[i] for i in range(24)])

    # Print the table header
    print("Average Temperatures for Test Week")
    print("Units are in Fahrenheit")

    # Print the DataFrame
    print(temp_df.to_string(index=True, float_format="{:.1f}".format))

# Run the function to display the table
print_temp_by_day_time()




"""
"C:\\Users\\zandu\\python projects\\Assignment_11.py\\.venv\\Scripts\\python.exe" "C:\\Users\\zandu\\python projects\\Assignment_11.py\\Addignment_11.py" 
Average Temperatures for Test Week
Units are in Fahrenheit
           SUN  MON  TUE  WED  THU  FRI  SAT
Mid-1AM   68.8 68.4 72.7 71.3 70.6 70.7 66.8
1AM-2AM   69.0 68.3 72.5 71.1 70.3 70.5 66.9
2AM-3AM   69.1 68.3 72.3 70.9 70.0 70.4 67.0
3AM-4AM   69.2 68.1 72.2 70.8 69.8 70.3 67.0
4AM-5AM   69.2 68.1 72.1 70.6 69.7 70.1 67.1
5AM-6AM   69.2 68.0 72.1 70.5 69.6 70.0 67.1
6AM-7AM   68.8 67.9 72.1 70.1 69.4 69.6 67.1
7AM-8AM   68.1 68.1 71.8 70.0 69.5 69.2 67.1
8AM-9AM   67.4 68.1 71.1 69.5 69.7 68.3 67.1
9AM-10AM  67.3 69.1 71.5 69.4 70.6 67.1 67.2
10AM-11AM 67.1 70.4 72.3 69.9 71.5 66.6 67.2
11AM-NOON 66.9 70.9 73.2 70.4 72.2 66.6 66.6
NOON-1PM  66.8 71.2 73.1 71.3 72.1 66.3 65.9
1PM-2PM   66.7 71.9 73.6 72.3 71.9 66.1 65.5
2PM-3PM   66.9 72.8 74.3 73.1 72.3 66.1 65.2
3PM-4PM   66.7 73.3 74.7 74.0 72.7 66.1 65.0
4PM-5PM   66.7 73.8 75.1 74.4 73.4 66.0 64.9
5PM-6PM   66.7 74.2 75.7 74.9 74.0 66.0 64.9
6PM-7PM   66.7 73.5 75.1 74.6 73.5 65.8 64.8
7PM-8PM   67.2 73.4 74.0 73.4 72.5 65.7 64.8
8PM-9PM   67.8 73.4 73.0 72.6 71.7 65.4 64.7
9PM-10PM  68.1 73.3 72.2 71.7 71.1 65.5 64.9
10PM-11PM 68.3 73.2 71.8 71.3 70.9 66.3 65.5
11PM-MID  68.6 73.0 71.5 70.9 70.8 66.6 65.7
"""