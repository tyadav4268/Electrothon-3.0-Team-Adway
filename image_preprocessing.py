import os
import cv2

imgpath = 'data/signs/test/1/1_0_1527.jpeg'
img = cv2.imread(imgpath)

labels = [str(i) for i in range(1, 11)]
labels.extend([chr(i) for i in range(65, 91)])

for i in ['test', 'train', 'valid']:
    for j in labels:
        images = os.listdir(f'data/signs/{i}/{j}')
        for image in images:
            img = cv2.imread(f'data/signs/{i}/{j}/{image}')
            img_resized = cv2.resize(img, (224, 224))
            final_image = cv2.Canny(img, 100, 100)
            cv2.imwrite(f'data/signs/{i}/{j}/{image}', final_image)
