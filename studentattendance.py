# Read attendance records
with open("attendance.txt", "r") as file:
    records = file.readlines()

total_students = 0
present_students = 0
absent_students = 0

# Process records
for record in records:
    name, status = record.strip().split(",")

    total_students += 1

    if status == "Present":
        present_students += 1
    elif status == "Absent":
        absent_students += 1

# Create report content
report = f"""Attendance Report
-----------------
Total Students : {total_students}
Present Students : {present_students}
Absent Students : {absent_students}
"""

# Write report to file
with open("report.txt", "w") as file:
    file.write(report)

print("Report generated successfully!")