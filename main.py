import cv2
from PIL import Image

image_path = "cat.jpeg"

cat_face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')

image = cv2.imread(image_path)

cat_face = cat_face_cascade.detectMultiScale(image)
print(cat_face)

cat = Image.open(image_path)
glasses = Image.open("glasses.png")

cat = cat.convert("RGBA")
glasses = glasses.convert("RGBA")

for(x, y, w, h) in cat_face:
    glasses = glasses.resize((w, int(h/3)))
    cat.paste(glasses, (x, int(y+h/4)), glasses)
    cat.save("Cat_with_glasses.png")
    cat_with_glasses = cv2.imread("Cat_with_glasses.png")
    cv2.imshow("Cat with glasses", cat_with_glasses)

# for (x, y, w, h) in cat_face:
#     cv2.rectangle(image, (x,y),(x+w, y+h), (0, 0, 255), 3)

cv2.imshow("Cat", image)
cv2.waitKey()
