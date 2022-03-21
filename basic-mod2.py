numberArray = [350, 372, 192, 354, 139, 337, 67, 311, 392, 338, 241, 414, 180, 277, 379, 294, 128, 117, 250, 404, 336, 350, 386]
decodeArray = ["", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8","9", "_"]
modArray = [0]*len(numberArray)
idx = 0
decodeString=""

for i in numberArray:
	modArray[idx] = pow(i, -1, 41)
	idx += 1

print(numberArray)
print(decodeArray)
print(modArray)

for i in modArray:
        decodeString = decodeString + decodeArray[i]

print("picoCTF{"+decodeString+"}")
