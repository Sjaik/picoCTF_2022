import numpy as np

numberArray = [128, 63, 131, 198, 262, 110, 309, 73, 276, 285, 316, 161, 151, 73, 219, 150, 145, 217, 103, 226, 41, 255]
decodeArray = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8","9", "_"]
modArray = [0]*len(numberArray)
idx = 0
decodeString=""

for i in numberArray:
	modArray[idx] = i % 37
	idx += 1

print(numberArray)
print(decodeArray)
print(modArray)

for i in modArray:
	decodeString = decodeString + decodeArray[i]

print("picoCTF{"+decodeString+"}")

