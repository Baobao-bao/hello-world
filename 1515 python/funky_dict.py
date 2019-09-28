# funky_dict.py
#
# This program has a bunch of functions to add, remove, update, and delete
# items in a dictionary.
#
# You will write the code for each function, and then uncomment the 
# appropriate line in the tests() function to check your work.
#

# Step 1: create a new dictionary called 'course_enrollment'. Your dictionary
#         will use a course number as the key, and store the number of 
#         enrolled students as the value. Initialize your dictionary with
#         the following 3 key value pairs:
#                                            ACIT1234 : 25
#                                            ACIT3456 : 19
#                                            MATH0001 : 15

### Put your Step 1 code here

course_enrollment = {
    'ACIT1234' : 25,
    'ACIT3456' : 19,
    'MATH0001' : 15,
}
# Step 2: complete the function add_course(course_number) which should add
#         a new course with the specified number into the dictionary, setting
#         the number of students to zero, and printing a line saying 
#         'Course [number] added with 0 students'. This function returns the
#         course_number

def add_course(course_number):
    #### your code goes here
    course_enrollment[course_number] = 0 
    print('Course',course_number, 'added with 0 students')
    return course_number
    
# Step 3: complete the function delete_course(course_number) which should 
#         remove the specified course from the dictionary, and print a
#         line saying 'Course [number] removed'. Nothing is returned.

def delete_course(course_number):
    #### your code goes here
    del course_enrollment[course_number]
    print('Course', course_number, 'removed')
    return
    
# Step 4: complete the function add_students(course_number, new_students) 
#         which will increase the number of students in the specified course by
#         new_students, and return the new total number of students in 
#         the course

def add_students(course_number, new_students):
    #### your code goes here
    course_enrollment[course_number] += new_students
    return course_enrollment[course_number]
    
# Step 5: complete the function num_students(course_number) which returns the
#         returns the number of students in the course

def num_students(course_number):
    #### your code goes here
    return course_enrollment[course_number]

# Below is the test function. You do not need to change it, except to uncomment 
# the tests as you complete the coding for each step.
def tests():
    course1 = 'ACIT1234'
    course2 = 'ACIT3456'
    course3 = 'MATH0001'
    
    ### Uncomment the next three lines after your have coded Step 1
    print(course1+':', course_enrollment[course1])
    print(course2+':', course_enrollment[course2])
    print(course3+':', course_enrollment[course3])
    
    ### uncomment the next two lines after you have coded Step 2
    course4 = add_course('COMM1991')
    course5 = add_course('COMP7777')
    
    ### uncomment the next two lines after you have coded Step 3
    delete_course(course2)
    delete_course(course4)
    
    ### uncomment the next four lines after you have coded Step 4
    c1_count = add_students(course1, 1)
    print('Course', course1, 'enrollment:', c1_count)
    c5_count = add_students(course5, 2)
    print('Course', course5, 'enrollment:', c5_count)

    ### uncomment the next two lines after you have coded Step 4    
    c3_count = num_students(course3)
    print('Course', course3, 'enrollment:', c3_count)
    return
    
# The next line is the start. It just calls the tests() function.
# This is the first thing that gets executed.
tests()