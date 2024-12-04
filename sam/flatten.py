
arr=[ [10,20],
      [20,30],
      [30,40],
      [40,50]
]

result=[ num for ls in arr for num in ls ]

print(result)

#greater than 20

result=[num for ls in arr for num in ls if num>20]

print(result)