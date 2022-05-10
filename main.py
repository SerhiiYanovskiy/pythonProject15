import numpy as np
import cv2
import os
path = ("/home/serhii/PycharmProjects/pythonProject15/input_image")
list_image = os.listdir(path)
for elem in list_image:
	image = cv2.imread(f"{path}/{elem}")
	blur = cv2.GaussianBlur(image, (21, 21), 0)
	hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
	cv2.imwrite("res.jpg", hsv)
	lower = [18, 50, 50]
	upper = [35, 255, 255]
	lower = np.array(lower, dtype="uint8")
	upper = np.array(upper, dtype="uint8")
	mask = cv2.inRange(hsv, lower, upper)
	no_red = cv2.countNonZero(mask)
	if int(no_red) > 2000:
		print(f'{elem} is  Fire detected')
	else:
		print((f'{elem} is not Fire detected'))

if cv2.waitKey(1) & 0xFF == ord('q'):
	pass
