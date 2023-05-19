rows, columns = [int(x) for x in input().split()]

start_end = ord("a")    # 97

for row in range(start_end, start_end + rows):
    for column in range(start_end, start_end + columns):
        print(f"{chr(row)}{chr((row + column) - start_end)}{chr(row)}", end=" ")
    print()
    
# Variant 2
# rows, cols = [int(x) for x in input().split()]
# 
# start = ord("a")
# 
# for row in range(start, start + rows):
#     for col in range(start, start + cols):
#         print(f"{chr(row)}{chr(col + abs(97 - row))}{chr(row)}", end=" ")
#     print()
