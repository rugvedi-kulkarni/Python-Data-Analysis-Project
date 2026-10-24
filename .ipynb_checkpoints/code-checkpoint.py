# Python data analysis - using core python
'''
# Count students from region A -> expected a single output

count = 0
for line in open("Datasets/student_record.txt"):
    each_field = line.strip().split(";")
    region_code = each_field[0]
    if region_code == "A":
        count += 1

print(f'Students from region A: {count}')


# Calculate the average Maths marks for region B (Assuming marks is at 6th position)

marks = []
for line in open("Datasets/student_record.txt"):
    each_field = line.strip().split(";")
    region = each_field[0]
    
    region_math_marks = each_field[5]
    convert_marks = float(region_math_marks) # converting string into float
    
    if region == "B":
        marks.append(convert_marks)

avg_math_marks = sum(marks) / len(marks)
print(f'Average marks from region B is {avg_math_marks}') 


# Count students who scored above 50 in Maths

count = 0
for line in open("Datasets/student_record.txt"):
    each_feild = line.strip().split(";")
    
    maths_marks = each_feild[5]
    converted_marks = float(maths_marks)

    if converted_marks > 50:
        count += 1

print(f'Count of students who scored > 50: {count}')


# find the highest math marks
# empty list to store highest marks
marks = [] 

for line in open("Datasets/student_record.txt"):
    each_feild = line.strip().split(";")
    
    maths_marks = each_feild[5] 
    converted_marks = float(maths_marks)
    
    marks.append(converted_marks)

max_marks = max(marks) # aggregation function
print(f'Highest marks of student: {max_marks}')

# Calculate the pass percentage
# Assume a Maths mark of 35 or more is a pass. Calculate the percentage of students who passed.
# Formula: passed students ÷ total students × 100

marks = [] # empty list to store marks >= 35
total_students = 0

for line in open("Datasets/student_record.txt"):
    each_feild = line.strip().split(";")
    total_students += 1
    
    
    maths_marks = each_feild[5]
    converted_marks = float(maths_marks)
    
    if converted_marks >= 35:
        marks.append(converted_marks)

passed_students = len(marks) # total number of student scored >= 35 in maths
percentage = passed_students / total_students * 100
print(f'Percentage if passed students: {percentage}')


# intermediate level

# Compare average Maths marks across regions. Calculate the average Maths marks separately for regions A and B.
# Goal: Print both averages and identify which region has the higher average.


region_marks_A = []
region_marks_B = []

for line in open("Datasets/student_record.txt"):
    each_field = line.strip().split(";")
    
    region_code = each_field[0]
    
    maths_marks = each_field[5]
    math_marks_converted = float(maths_marks)

    if region_code == "A":
        region_marks_A.append(math_marks_converted)
    elif region_code == "B":
        region_marks_B.append(math_marks_converted)

avg_marks_A = sum(region_marks_A) / len(region_marks_A)
avg_marks_B = sum(region_marks_B) / len(region_marks_B)

print(f'Average marks for region A is {avg_marks_A}')
print(f'Average marks for region B is {avg_marks_B}')

if avg_marks_A > avg_marks_B:
    print("Region A has highest everage marks")
else:
    print("Region B has highest everage marks")


# Find the highest-scoring student in region A.Find the student ID and Maths marks of the student with the highest Maths score in region A.

marks = []
ids = []
name = []

for line in open("Datasets/student_record.txt"):
    each_field = line.strip().split(";")
    
    region_code = each_field[0]
    student_id = each_field[1]
    name_student = each_field[2]
    
    maths_marks = float(each_field[5])
    if region_code == "A":
        ids.append(student_id)
        marks.append(maths_marks)  
        name.append(name_student)

max_marks = max(marks)

for i in range(len(marks)):
    if marks[i] == max_marks:
        print(f'Student name: {name[i]}, Maximum marks: {max_marks}, Index: {i}, Position: {i + 1}, Student ID: {ids[i]}')
        break

print(len(marks))
print(len(ids))

# Count students in a marks range. Count students whose Maths marks are between 40 and 70, inclusive.
count = 0
for line in open(Datasets/student_record.txt):
    each_field = line.strip().split(";")
    math_marks = int(float(each_field[5]))

    if math_marks >= 40 and math_marks <= 70:
        count += 1

print(f'Number of student scored between (40 - 70): {count}')


# Find the average for high-scoring students
# Calculate the average Maths marks only for students who scored at least 75.
#Challenge: Also count how many students qualified for the calculation. 

highest_marks = []
count = 0

for line in open("Datasets/student_record.txt"):
    each_field = line.strip().split(";")
    math_marks = int(float(each_field[5]))

    if math_marks >= 75:
        highest_marks.append(math_marks)
        count += 1

avg = sum(highest_marks) / len(highest_marks)
print(f'Average of students who scored at least 75 is {avg}')
print(f'Total number of students qualified for the calculation is {count}')   

# Compare pass percentages between regions
# Using the pass threshold of 35, calculate the pass percentage for regions A and B separately.
# Goal: Determine which region has the higher pass percentage, rather than merely the greater number of passes.
    
region_marks_A = []
region_marks_B = []
total_student_passed_A = 0
total_student_passed_B = 0

for line in open("Datasets/student_record.txt"):
    each_field = line.strip().split(";")
    math_marks = float(each_field[5])

    region_code = each_field[0]

    if region_code == "A":
        region_marks_A.append(math_marks)
    elif region_code == "B":
        region_marks_B.append(math_marks)

for i in range(len(region_marks_A)):

    if region_marks_A[i] >= 35:
        total_student_passed_A += 1

for j in range(len(region_marks_B)):

    if region_marks_B[j] >= 35:
        total_student_passed_B += 1
        
pass_per_region_A = total_student_passed_A / len(region_marks_A) * 100
pass_per_region_B = total_student_passed_B / len(region_marks_B) * 100

if pass_per_region_A > pass_per_region_B:
    print("Region A has higher pass percentage in maths\n")
elif pass_per_region_B > pass_per_region_B:
    print("Region B has higher pass percentage in maths\n")
else:
    print("Both has higher pass percentage in maths\n")
'''
# Advanced level
# Create a marks distribution

# Count how many students fall into each group:
# - Below 35
# - 35–49
# - 50–69
# - 70 and above
# Goal: Print the count for each group.

'''
print("=========Marks distribution=========\n")

group_1_count = 0
group_2_count = 0
group_3_count = 0
group_4_count = 0

for line in open("Datasets/student_record.txt"):
    each_field = line.strip().split(";")
    math_marks = float(each_field[5])

    if math_marks < 35:
        group_1_count += 1
    if math_marks >= 35 and math_marks <= 49:
        group_2_count += 1
    if math_marks >= 50 and math_marks <= 69:
        group_3_count += 1
    if math_marks >= 70:
        group_4_count += 1


print(f'Total students scores marks below 35: {group_1_count}')       
print(f'Total students scores marks between (35 - 49): {group_2_count}')       
print(f'Total students scores marks between (50 - 69): {group_3_count}')       
print(f'Total students scores marks 70 or above: {group_4_count}')       
    
# Find the difference between the highest and lowest marks
# Find both values and calculate the range:
# range = highest mark - lowest mark
# Goal: Report the spread of Maths marks across the dataset.

marks = []
for line in open("Datasets/student_record.txt"):
    each_field = line.strip().split(";")
    math_marks = float(each_field[5])

    marks.append(math_marks)

highest_marks = max(marks)
lowest_marks = min(marks)
range_marks = highest_marks - lowest_marks
print(f'Range of highest {highest_marks} and lowest marks {lowest_marks} is {range_marks}')
'''

# Analyze a specific student
# Given a student ID, search the file and print that student's name, region and Maths marks.
# Goal: Stop searching once the student is found, if your file contains unique ID

student_id = "084076"

for line in open("Datasets/student_record.txt"):
    each_field = line.strip().split(";")

    if each_field[1] == student_id: # every value is converted to string
        print(f'Student name is {each_field[2]}')
        print(f'Student region is {each_field[0]}')
        print(f'Student math marks is {each_field[5]}')
        break

# Handle missing or invalid Maths marks
# Some records may have an empty Maths field or a value that cannot be converted to a number.
# Goal: Skip invalid marks, count how many records were skipped, and calculate the average from valid marks only.
  
# Analyze one lakh records without storing every mark
# Calculate the average Maths marks for region A without creating a list of all its marks.
# Goal: Maintain only a running total and a count.
