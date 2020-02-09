#!/usr/bin/env python3.6
# This program will take a txt file and convert it to an image. 
# The process works by taking 3 letters at a time, mapping them to values between 0 and 255, and then using
# those values to create an image
# A reverse process could be implemented to take an image and turn it back into text
# spaces and other non alpha characters are eliminated, so to read it will take some effort. 

import png
def get_width_height(factors):
	# if len(factors) % 2 == 1:
	# 	same = factors[int(len(factors)/2)]
	# 	return [same, same]
	
	height = int(len(factors) / 2)
	width = height - 1

	return factors[width], factors[height]

# factor square.py
input_name = "pdx"
with open("{}.txt".format(input_name), mode='r') as file:
	lines = file.read()

letters = ''.join(e for e in lines if e.isalpha())

valuemap = {65:0,66:5,67:10,68:15,69:20,70:25,71:30,72:35,73:40,74:45,75:50,76:55,77:60,78:65,79:70,80:75,81:80,82:85,83:90,84:95,85:100,86:105,87:110,88:115,89:120,90:125,97:130,98:135,99:140,100:145,101:150,102:155,103:160,104:165,105:170,106:175,107:180,108:185,109:190,110:195,111:200,112:205,113:210,114:215,115:220,116:225,117:230,118:235,119:240,120:245,121:250,122:255}

# print( valuemap[65], valuemap[100], valuemap[101]  )

ord_values = [valuemap[ord(letter)] for letter in letters]
# ord_values = set(ord_values)
# print(max(ord_values), min(ord_values))
print(len(ord_values))
n = int(len(ord_values)/3)


factors = [i for i in range(1, n+1) if n % i == 0]
width, height = get_width_height(factors)

print(width, height)
width = 341
height = 1023

# for i in range(int(len(ord_values)/3)):
# 	print(i+1, ord_values[i*3:i*3+3])
# 	i3 = i*3
# 	ord_values[pos], ord_values [pos+1] , ord_values[pos+2]


img = []
# # width *= 3
# for y in range(height): # 12... 0, 1, 2, 
# 	row = ()
# 	for x in range(width): # 9... 0, 1, 2
# 		pos = y * width + x
# 		row = row + (ord_values[pos], ord_values [pos+1] , ord_values[pos+2])
# 		# row = row + tuple(ord_values[pos])
# 		# + (x, max(0, 255 - x - y), y)
# 	img.append(row)

for y in range(height):
	row = ()
	b = width * 3 
	row = row + tuple(ord_values[y * b : y * b + b])
	img.append(row)


with open("{}2.png".format(input_name), 'wb') as f:
    w = png.Writer(width, height, greyscale=False)
    w.write(f, img)

