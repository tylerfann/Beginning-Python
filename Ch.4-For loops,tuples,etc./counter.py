# Ch.4: Challenge 1
# Counter progrom
# user can enter a start/end point and program will count that range

start = int(input("Enter a starting point: "))
end = int(input("Enter an ending point: "))
count = int(input("Enter an amount which to count by: "))

end += count

for num in range(start, end, count):
    print(num, end=" ")
