#!/usr/bin/env python3.6
import png

def rtnf(value):
	return round(value/5) * 5

valuemap = {0:65,5:66,10:67,15:68,20:69,25:70,30:71,35:72,40:73,45:74,50:75,55:76,60:77,65:78,70:79,75:80,80:81,85:82,90:83,95:84,100:85,105:86,110:87,115:88,120:89,125:90,130:97,135:98,140:99,145:100,150:101,155:102,160:103,165:104,170:105,175:106,180:107,185:108,190:109,195:110,200:111,205:112,210:113,215:114,220:115,225:116,230:117,235:118,240:119,245:120,250:121,255:122}

input_name = "pdx"
file_name = "{}.png".format(input_name)

r = png.Reader(filename=file_name)
img = r.read()

with open("{}.txt".format(input_name), mode='w') as file:

	for row in img[2]:
		file.write(''.join(	[chr(valuemap[rtnf(x)]) for x in row]	))
