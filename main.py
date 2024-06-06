import cv2
import numpy as np



name_image = 'vetru_chel.png'
# Загрузка изображения
image = cv2.imread(name_image)

# Нахождение ширины и высоты изображения
height, width, _ = image.shape

# Вычисление координат точек, соответствующих золотому сечению
phi = 1.618  # Значение золотого сечения

# Вертикальные линии
x1 = int(width / phi)
y1 = 0
x2 = int(width - x1)
y2 = height
cv2.line(image, (x1, y1), (x1, y2), (0, 0, 255), 3)
cv2.line(image, (x2, y1), (x2, y2), (0, 0, 255), 3)

# Горизонтальные линии
y3 = int(height / phi)
x3 = 0
y4 = int(height - y3)
x4 = width
cv2.line(image, (x3, y3), (x4, y3), (0, 0, 255), 3)
cv2.line(image, (x3, y4), (x4, y4), (0, 0, 255), 3)

center_x = image.shape[1] // 2
center_y = image.shape[0] // 2

# Нарисуем оцентрованную горизонтальную линию (красного цвета) на изображении
cv2.line(image, (0, center_y), (image.shape[1], center_y), (255, 0, 0), 3)  # Начальная точка (0, center_y), конечная точка (ширина изображения, center_y), цвет (красный), толщина линии 3

# Нарисуем оцентрованную вертикальную линию (зеленого цвета) на изображении
cv2.line(image, (center_x, 0), (center_x, image.shape[0]), (255, 0, 0), 3)  # Начальная точка (center_x, 0), конечная точка (center_x, высота изображения), цвет (зеленый), толщина линии 3


# Отображение изображения с нарисованными линиями золотого сечения
cv2.imshow(name_image, image)
cv2.waitKey(0)
cv2.destroyAllWindows()