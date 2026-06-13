error_count = 0

# Open log file for reading
with open("logs.txt", "r") as logfile:
    lines = logfile.readlines()

# Open error file for writing
with open("errors.txt", "w") as errorfile:
    for line in lines:
        if "ERROR" in line:
            errorfile.write(line)
            error_count += 1

print(f"Total Errors Found: {error_count}")