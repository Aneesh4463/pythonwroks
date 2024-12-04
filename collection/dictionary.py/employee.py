# create dictionary employee with keys id, name, salary, department, experience

employee={"eid":"LCMA07",
          "name":"ronaldo",
          "salary":35000,
          "department":"hr","experience":3}

print(employee["salary"])


#add contact as 3453324


employee["contact"]=453324

print(employee)


# if experience > 5 update employee salary as currentsalary+10000
# else currentsalary+5000


if employee["experience"]>5:

    employee["salary"]+=10000

else:

    employee["salary"]+=5000

print(employee)


#add role as SDE id exp>5 else add role as JDE


if employee["experience"]>5:

    employee["role"]="SDE"

else:

    employee["role"]="JDE"

print(employee)




