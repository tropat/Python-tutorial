lucky_numbers = [2, 4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", 2, False]

print(friends[0])
print(friends[-1])
print(friends[1:])

friends[1] = "Mike"

print(friends[1:3])

friends.extend(lucky_numbers)
print(friends)

friends.append("Creed")
print(friends)

friends.insert(1, "Kelly")
print(friends)

friends.remove("Jim")
print(friends)

friends.pop()
print(friends)

print(friends.index("Kelly"))
print(friends.count(2))
print(friends.count("Kevin"))

lucky_numbers.sort()
print(lucky_numbers)

lucky_numbers.reverse()
print(lucky_numbers)

friends2 = friends.copy()
print(friends2)

friends.clear()
print(friends)

#-----------------------------
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
print(number_grid[2][1])

for row in number_grid:
    print(row)

for row in number_grid:
    for col in row:
        print(col)