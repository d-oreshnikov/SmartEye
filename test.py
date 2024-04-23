import cv2

# Загрузка изображения с 4 каналами
image_with_4_channels = cv2.imread('photo/man.png', cv2.IMREAD_UNCHANGED)

# Конвертация изображения в RGB (3 канала)
rgb_image = cv2.cvtColor(image_with_4_channels, cv2.IMREAD_COLOR)

# Сохранение трехканального изображения
cv2.imwrite('image_with_3_channels.jpg', rgb_image)