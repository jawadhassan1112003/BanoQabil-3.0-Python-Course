# Jawad Hassan 
# 56437
# jawadhassan1112003@gmail.com

# Nazeef
# ------
# ----------------------------

# Prompt the user to enter marks for 5 subjects
print("Enter Marks Of 5 Subjects")

# Prompt the user to enter subject names and marks
subject1 = input("Enter name of subject 1: ")
a = int(input(f"Enter marks for {subject1}: "))

subject2 = input("Enter name of subject 2: ")
b = int(input(f"Enter marks for {subject2}: "))

subject3 = input("Enter name of subject 3: ")
c = int(input(f"Enter marks for {subject3}: "))

subject4 = input("Enter name of subject 4: ")
d = int(input(f"Enter marks for {subject4}: "))

subject5 = input("Enter name of subject 5: ")
e = int(input(f"Enter marks for {subject5}: "))

# Check if all the marks are greater than or equal to 33
if a >= 33 and b >= 33 and c >= 33 and d >= 33 and e >= 33:
    print("---------------")
    # If all marks are >= 33, print "Result: PASS"
    print("Result: PASS")
    # Calculate the percentage
    per = (a + b + c + d + e) / 5
    # Print the calculated percentage
    print("Percentage:", per)
    # Determine the grade
    if per >= 90:
        grade = 'A'
    elif per >= 75:
        grade = 'B'
    elif per >= 60:
        grade = 'C'
    elif per >= 45:
        grade = 'D'
    else:
        grade = 'E'
    print("Grade:", grade)
    print("---------------")
else:
    # If any mark is less than 33, print "Result: FAIL"
    print("---------------")
    print("Result: FAIL")
    print("---------------")

# Print subject names and marks
print(f"\nMarks for each subject:")
print(f"{subject1}: {a}")
print(f"{subject2}: {b}")
print(f"{subject3}: {c}")
print(f"{subject4}: {d}")
print(f"{subject5}: {e}")

print("--Code End--")
