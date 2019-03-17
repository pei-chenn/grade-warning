def get_grades_data():
    gradesdata=[]
    passed_percent=0

    a=0
    for grade1 in infile1:
        gradesdata.append([0.0,0.0,0])
        gradesdata[a][0]=float(grade1.strip("\n"))
        a+=1

    b=0
    for grade2 in infile2:
        gradesdata[b][1]=float(grade2.strip("\n"))
        b+=1

    c=0
    pass_count=0
    pass_grade_total=0
    fail_grade_total=0
    for line in infile3:
        if line.strip("\n")=="Pass":
            gradesdata[c][2]=1
            pass_grade_total=pass_grade_total+gradesdata[c][0]+gradesdata[c][1]
            pass_count+=1
        else:
            gradesdata[c][2]=0
            fail_grade_total=fail_grade_total+gradesdata[c][0]+gradesdata[c][1]
        c+=1

    passed_percent=pass_count/c

    first_point=pass_grade_total/pass_count
    third_point=fail_grade_total/(c-pass_count)
    second_point=(first_point*passed_percent)+(third_point*(1-passed_percent))
    

    return first_point, second_point, third_point

def predict_result(user_total_grade, first_point, second_point, third_point):
    if user_total_grade>=first_point:
        return "Great job! Keep up the good work!"
    elif user_total_grade<=third_point:
        return "Dropping this class might be a good decision."
    elif user_total_grade>second_point and user_total_grade<first_point:
        return "Your grades are a little danger. Make sure to work hard on the final."
    else:
        return "You really need a high grade on the final in order to pass this class."

infile1=open("midterm1.txt","r")
infile2=open("midterm2.txt","r")
infile3=open("result.txt","r")

midterm1_grade=float(input("Enter your midterm1 grade:"))
midterm2_grade=float(input("Enter your midterm2 grade:"))
user_total_grade=midterm1_grade+midterm2_grade

first_point, second_point, third_point=get_grades_data()
print(predict_result(user_total_grade, first_point, second_point, third_point))

infile1.close()
infile2.close()
infile3.close()
