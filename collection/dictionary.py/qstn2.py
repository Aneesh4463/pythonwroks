arr=[10,20,30,40,2,3]   # out even_number= square & odd _numbre =cubes

even_numbers={ num:num**2 for num in arr  if num%2==0  }

odd_numbers={ num:num**3  for num in arr  if num%2!=0  }

print("odd pairs =>",odd_numbers)

print("even pairs =>",even_numbers)


# frequency of numbers   =>  {10:2}

arr=[10,20,30,40,2,3,7,8,9,10,30]

frequency_count={ num:arr.count(num)  for num in arr }

print(frequency_count)

