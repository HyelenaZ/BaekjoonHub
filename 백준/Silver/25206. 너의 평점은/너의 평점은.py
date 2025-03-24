import sys
input = sys.stdin.readline

grade_info = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0,
    'P': None  
}

def calculate_grade_average():
    total_grade_points = 0 
    total_credits = 0      

    for _ in range(20):
        subject, credit, grade = input().split()
        credit = float(credit)  
        if grade != 'P':  
            grade_point = grade_info[grade]
            total_grade_points += credit * grade_point
            total_credits += credit
    
    gpa = total_grade_points / total_credits  
    print(f"{gpa:.6f}")

calculate_grade_average()
