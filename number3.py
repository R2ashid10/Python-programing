def weekly_temperatures():
    temperatures = []
    
    for day in range(7): 
        temp = float(input(f"Enter temperature of day {day + 1}:"))
        temperatures.append(temp)
    
    highest_temp = max(temperatures)
    lowest_temp = min(temperatures)
    average_temp = sum(temperatures) / len(temperatures)
    total_temp = sum(temperatures)

    print(f"Highest temperature of the week: {highest_temp:.2f}")
    print(f"Lowest temperature of the week: {lowest_temp:.2f}")
    print(f"Average temperature of the week: {average_temp:.2f}")
    print(f"Total of all temperatures of the week: {total_temp:.2f}")

weekly_temperatures()
