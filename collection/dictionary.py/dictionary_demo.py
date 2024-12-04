
# create a dictionary product with keys id, title, price, brand

# dictionary syntax :>  key:values pairs

product={"id":42315,"title":"i20 sportz","price":1300000,"brand":"hyundai"}

print(product["title"])

# product price update as 1400000

product["price"]=1400000

print(product)

#update brand as bmw

product["brand"]="BMW"

print(product)

# add new key "use by date"

product["use_by_date"]="20_12_2035"

print(product)

# chk key exist or not

if "brand" in product:

    print("exist")

else:

    print("not")



#qstn: add offer as 10 if offer exist else add offer as 20

if "offer" in product:

    product["offer"]=10

else:

    product["offer"]=20

print(product)

