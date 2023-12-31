def convert24(time):
    # Splitting hours and minutes
    time_parts = time[:-2].split(':')
    hours = int(time_parts[0])
    minutes = int(time_parts[1]) if len(time_parts) > 1 else 0

    # Checking if last two elements of time are PM and first two elements are 12
    if time[-2:] == "pm" and hours == 12:
        return f"{hours:02d}:{minutes:02d}"

    # Checking if last two elements of time are AM and first two elements are 12
    if time[-2:] == "am" and hours == 12:
        return f"00:{minutes:02d}"

    # Checking if last two elements of time are PM
    elif time[-2:] == "pm":
        return f"{hours + 12:02d}:{minutes:02d}"

    else:
        # Checking if last two elements of time are AM
        return f"{hours:02d}:{minutes:02d}" 
print(convert24("4:20pm"))   
print (convert24("2200"))
