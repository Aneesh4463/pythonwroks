cars=[
    {"id":1,"name":"fronx","price":1200000,"brand":"nexa","colors":["red","blue","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":2,"name":"baleno","price":1100000,"brand":"nexa","colors":["grey","blue","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":3,"name":"3xo","price":900000,"brand":"mahindra","colors":["red","white","black"],"transmissions":["amt","cvt"]},
    {"id":4,"name":"punch","price":700000,"brand":"tata","colors":["red","blue","white","green"],"transmissions":["manuel","cvt"]},
    {"id":5,"name":"nexon","price":1400000,"brand":"tata","colors":["red","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":6,"name":"kiger","price":1000000,"brand":"renault","colors":["blue","white"],"transmissions":["manuel","cvt","dct"]},
    {"id":7,"name":"taigun","price":2300000,"brand":"volkswagon","colors":["red","blue","white"],"transmissions":["manuel","cvt","torque"]},
]

# print count of vehicles

print(f"total number of vehicles => {len(cars)}")


# print available colours of baleno

baleno_colors=[b.get("colors") for b in cars if b.get("name")=="baleno" ]

print(baleno_colors[0])


# print all brands

brands=[c.get("brand") for c in cars ]

print(set(brands))

# print car names available in amt transmission

amt_transmission_car=[d.get("name") for d in cars  if "amt" in d.get("transmissions") ]

print(amt_transmission_car)


# cars avilable in blue colors

blue_colors_cars=[b.get("name") for b in cars if "blue" in b.get("colors")]

print(blue_colors_cars)

# print all transmission type

transmission_type={ t    for c in cars  for t in c.get("transmissions") }

print(transmission_type)

# print all colors

colors_car={  d     for c in cars for d in c.get("colors")}

print(colors_car)

# costly car 

costly_car=[p.get("price")  for p in cars]

price=max(costly_car)

costly_car_name=[ c.get("name") for c in cars if c.get("price")==price]

print(f"costly_car_name=> {costly_car_name}")




# car with minimum cost 

costly_car=[p.get("price")for p in cars]

price=min(costly_car)

cheap_car_name=[ c.get("name") for c in cars if c.get("price")==price]

print(f"cheap_cost_carname=> {cheap_car_name}")



#  sort car price

car_price={c.get("name"):c.get("price") for c in cars}

print(car_price)

# most popular color  => {"blue":4,"red:2"....}

# most_color=[d for c in cars for d in c.get("colors")]

# colours=[]

# for c in cars:
#     count=0

#     for d in c.get("colors"):

#         if colours!=d:

#             colours=d
        
#         else:

#             colours+=1
#     count+=1
#     print(colours)


