height = 12
width = 9
for y in range(height): # 12... 0, 1, 2, 
	for x in range(0, width*3, 3): # 9... 0, 1, 2
		pos = y * width + x
		# row = row + (ord_values[pos], ord_values [pos+1] , ord_values[pos+2])
		print(pos, pos + 1, pos + 2)