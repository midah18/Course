import random

def create_outline():
    course_topics = ["Introduction to Python", 
    "Tools of the Trade", 
    "How to make decisions", 
    "How to repeat code", 
    "How to structure data", 
    "Functions", 
    "Modules"]

    course_topics.sort()
    point = '*' 

    print("Course Topics:")
    course_topics_1 = ["Introduction to Python", 
    "Tools of the Trade", 
    "How to make decisions", 
    "How to repeat code", 
    "How to structure data", 
    "Functions", 
    "Modules"]

    for i in course_topics:
        print(point,i)
    list_problems = ("Problem 1", "Problem 2", "Problem 3")
    new_list = ', '.join(list_problems)
    
    #YOU'RE WELCOME - Mr eyebrow
    print("Problems:")
    for i in course_topics_1:
        print(point,i + ' : ' + new_list)
    print("Student Progress: ")
    student_name = ["Nyari", "Adam", "Tom"]
    student_status = ["GRADED", "STARTED", "COMPLETED"]
    
    print("1. Nyari - Introduction to Python - Problem 2 [STARTED]")
    print("2. Adam - How to make decisions - Problem 1 [GRADED]")
    print("3. Tom - How to make decisions - Problem 1 [COMPLETED]")


if __name__ == "__main__":
    create_outline()
