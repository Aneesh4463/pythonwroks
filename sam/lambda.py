box=[
    {"color":"green","size":2},
    {"color":"green","size":7},
    {"color":"blue","size":1},
    {"color":"blue","size":5},
    {"color":"yellow","size":3},
    {"color":"yellow","size":8}
]

#count

print(len(box))

# print size and colors

for b in box:

    print(b.get("size"))

for b in box:
    
    print(b.get("color"))


# use list comperhension... print all colors

colurs=[b.get("color") for b in box]

print(colurs)

