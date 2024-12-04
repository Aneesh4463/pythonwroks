
# 3. Given a dictionary where the keys are student names and the values are their scores, write a program to calculate the average score.


students_details={"ram":50,"hari":30,"raj":10}

num=0

count=0

for v in students_details.values():
        
    num+=v

    count+=1

result=num/count

print(result)



    