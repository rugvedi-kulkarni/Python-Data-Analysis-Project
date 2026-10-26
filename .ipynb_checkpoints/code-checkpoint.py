"""
Student data analysis - using core python
Hereafter, assume marks of maths is at 5th index
"""

# def file_reading():
#     list_lines = []
    
#     with open("Datasets/student_record.txt") as file:
#         for line in file:
#             each_field = line.strip().split(";")

# Count students from region A -> expected a single output
count_A = 0

with open("Datasets/student_record.txt") as file:
    for line in file:
        each_field = line.strip().split(";")
        region_code = each_field[0]
        
        if "A" in region_code:
            count_A += 1  

if count_A:
    print(f"Students from region A: {count_A}")
else:
    print(f'No students from region A')

print("=========================================================")

# Calculate the average Maths marks for region B 
'''
sum_math_marks = 0
rB_students = 0

with open("Datasets/student_record.txt") as file:

    for line in file:
        
        each_field = line.strip().split(";")

        region_code = each_field[0]
    
        region_math_marks = float(each_field[5])
        
        if region_code == "B":
            sum_math_marks += region_math_marks
            rB_students  = rB_students + 1
        
        
if rB_students != 0:
    avg_math_marks = sum_math_marks / rB_students
    print(f'Average marks from region B is {avg_math_marks}') 

else:
    print(f'Division-by-zero error')

print("=======================================================")


# Count students who scored above 50 in Maths

count = 0
with open("Datasets/student_record.txt") as file:
    for line in file:

        each_feild = line.strip().split(";")
    
        maths_marks = each_feild[5]
        converted_marks = float(maths_marks)

        if converted_marks > 50:
            count += 1
        
if count:
    print(f'Count of students who scored > 50: {count}')

print("========================================")

# find the highest math marks

marks = [] 

with open("Datasets/student_record.txt") as file:
    for line in file:

        each_feild = line.strip().split(";")
    
        maths_marks = float(each_feild[5]) 
      
        marks.append(maths_marks)

max_marks = max(marks) # aggregation function
print(f'Highest marks of student: {max_marks}')

print("========================================")

# Calculate the pass percentage
# Assume a Maths mark of 35 or more is a pass. Calculate the percentage of students who passed.
# Formula: passed students ÷ total students × 100

marks = [] 
total_students = 0

with open("Datasets/student_record.txt") as file:
    for line in file:
    
        each_feild = line.strip().split(";")
        total_students += 1  
    
        maths_marks = float(each_feild[5])
    
        if maths_marks >= 35:
            marks.append(maths_marks)

if marks:
    passed_students = len(marks) # total number of student scored >= 35 in maths
    percentage = passed_students / total_students * 100
    print(f'Percentage if passed students: {percentage}')

print("========================================")


# Compare average Maths marks across regions. Calculate the average Maths marks separately for regions A and B.
# Goal: Print both averages and identify which region has the higher average.


region_marks_A = []
region_marks_B = []

with open("Datasets/student_record.txt") as file:
    for line in file:
        each_field = line.strip().split(";")
    
        region_code = each_field[0]
    
        maths_marks = float(each_field[5])

        if region_code == "A":
            region_marks_A.append(maths_marks)
        
        elif region_code == "B":
            region_marks_B.append(maths_marks)

if region_marks_A:
    avg_marks_A = sum(region_marks_A) / len(region_marks_A)
    
if region_marks_B:
    avg_marks_B = sum(region_marks_B) / len(region_marks_B)

    print(f'Average marks for region A is {avg_marks_A}')
    print(f'Average marks for region B is {avg_marks_B}')
else:
    print("No marks for region A and region B")

if avg_marks_A > avg_marks_B:
    print("Region A has highest average marks")
elif avg_marks_B >avg_marks_A:
    print("Region B has highest average marks")
else:
    print("Both region have highest average marks")

print("===================================================")


# Find the highest-scoring student in region A.
# Find the student ID and Maths marks of the student with the highest Maths score in region A.

marks = []
ids = []


with open("Datasets/student_record.txt") as file:
    for line in file:
        each_field = line.strip().split(";")
    
        region_code = each_field[0]
        student_id = each_field[1]
    
        maths_marks = float(each_field[5])
    
        if region_code == "A":
            ids.append(student_id)
            marks.append(maths_marks) 

if marks:
    max_marks = max(marks)

idx_max_marks = marks.index(max_marks)

print(f'Maximum marks: {max_marks}, Student ID: {ids[idx_max_marks]}')  
print("=======================================================")

# Count students in a marks range. Count students whose Maths marks are between 40 and 70, inclusive.

count = 0

with open("Datasets/student_record.txt") as file:
    for line in file:
        each_field = line.strip().split(";")

        if type(each_field[5]) == str:
            math_marks = float(each_field[5])
            
        if 40 <= math_marks <= 70:
            count += 1
            
# print(count)
if count:
    print(f'Number of student scored between (40 - 70): {count}')
else:
    print(f'No student scored between (40 - 70)')

print("================================================")

# Find the average for high-scoring students
# Calculate the average Maths marks only for students who scored at least 75.
# Challenge: Also count how many students qualified for the calculation. 

highest_marks = []
count = 0

with open("Datasets/student_record.txt") as file:
    for line in file:
        each_field = line.strip().split(";")
        math_marks = float(each_field[5])

        if math_marks >= 75:
            highest_marks.append(math_marks)
            count += 1

if highest_marks:
    avg = sum(highest_marks) / len(highest_marks)

print(f'Average of students who scored at least 75 is {avg}')

if count:
    print(f'Total number of students qualified for the calculation is {count}')  
else:
    print(f'No student is qualified for calculation')

print("=================================================")

# Compare pass percentages between regions
# Using the pass threshold of 35, calculate the pass percentage for regions A and B separately.
# Goal: Determine which region has the higher pass percentage, rather than merely the greater number of passes.
    
total_student_passed_A = 0
total_student_passed_B = 0
student_A = 0
student_B = 0

with open("Datasets/student_record.txt") as file:
    for line in file:
        each_field = line.strip().split(";")

        region_code = each_field[0]
        math_marks = float(each_field[5])
    
        if region_code == "A":
            student_A += 1
        
            if math_marks >= 35:
                total_student_passed_A += 1
            
        if region_code == "B":
            student_B += 1

            if math_marks >= 35:
                total_student_passed_B += 1  

pass_A = total_student_passed_A / student_A * 100
pass_B = total_student_passed_B / student_B * 100

if pass_A > pass_B:
    print("Region A has higher pass percentage")
elif pass_B > pass_A:
    print("Region B has higher pass percentage")
else:
    print("Both region has same pass percentage")

print("============================================")

# Create a marks distribution

# Count how many students fall into each group:
# - Below 35
# - 35–49
# - 50–69
# - 70 and above
# Goal: Print the count for each group.


print("=========Marks distribution=========\n")

group_1_count = 0
group_2_count = 0
group_3_count = 0
group_4_count = 0

with open("Datasets/student_record.txt") as file:
    for line in file:
        each_field = line.strip().split(";")
        math_marks = float(each_field[5])

        if math_marks < 35: group_1_count += 1
        
        if math_marks >= 35 and math_marks <= 49: group_2_count += 1
        
        if math_marks >= 50 and math_marks <= 69: group_3_count += 1
        
        if math_marks >= 70: group_4_count += 1


print(f'Total students scores marks below 35: {group_1_count}')       
print(f'Total students scores marks between (35 - 49): {group_2_count}')       
print(f'Total students scores marks between (50 - 69): {group_3_count}')       
print(f'Total students scores marks 70 or above: {group_4_count}')       

print("===================================================")


# Find the difference between the highest and lowest marks
# Find both values and calculate the range:
# range = highest mark - lowest mark
# Goal: Report the spread of Maths marks across the dataset.

marks = []

with open("Datasets/student_record.txt") as file:
    for line in file:
        each_field = line.strip().split(";")

        math_marks = float(each_field[5])

        # Additional changes
        # if math_marks < 0:
        #     new_math_marks = 0
        #     print(each_field)
            
        marks.append(math_marks)

highest_marks = max(marks)
lowest_marks = min(marks)

range_marks = highest_marks - lowest_marks

print(f'Range of highest {highest_marks} and lowest marks {lowest_marks} is {range_marks}')

print("=========================================================")



# Analyze a specific student
# Given a student ID, search the file and print that student's name, region and Maths marks.
# Goal: Stop searching once the student is found, if your file contains unique ID


student_id = 84076
student_info = {}

with open("Datasets/student_record.txt") as file:
    for line in file:
        each_field = line.strip().split(";")

        if int(each_field[1]) == student_id:
            student_name = each_field[2]
            student_region = each_field[0]
            student_math_marks = each_field[5]
        
            break

student_info  = {
    "student_id": student_id,
    "student_name": student_name,
    "student_region":student_region,
    "student_math_marks": student_math_marks
}

print(student_info)

print("========================================================================")

# Skip invalid marks, count how many records were skipped, and calculate the average from valid marks only.

valid_marks = []
skipped_records = 0

with open("Datasets/student_record.txt") as file:
    for line in file:
        each_field = line.strip().split(";")
        math_marks = float(each_field[5])

        if 0 <= math_marks <= 100:
            valid_marks.append(math_marks)
        else:
            skipped_records += 1

print(f'{skipped_records} records were skipped')

if valid_marks:
    avg_valid_marks = sum(valid_marks) / len(valid_marks)
    
print(f'Average of valid marks: {avg_valid_marks}')

print("==========================================================")

# Analyze one lakh records without storing every mark
# Calculate the average Maths marks for region A without creating a list of all its marks.
# Goal: Maintain only a running total and a count.

_marks_A = 0
total = 0

try:  
    with open("Datasets/student_record.txt") as file:
        for line in file:
            each_field = line.strip().split(";")
    
            region_code = each_field[0]
            math_marks = float(each_field[5])
    
            if region_code == 'A':
                _marks_A += math_marks
                total += 1

except FileNotFoundError:
    print("Student Record not found")
    
else:   

    print(f'Total number of students in region A: {total}')

    avg_marks = _marks_A / total
    print(f'Average marks of student in region A: {avg_marks}') 
    
finally:
    print("End of the program")

'''