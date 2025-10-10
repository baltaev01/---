# import cv2
#
# img = cv2.imread('assets/logo.jpg', 1)
# img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
# img = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)
#
# cv2.imwrite('new_img.jpg', img)
#
# cv2.imshow('Image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
# import cv2
# import random
#
# img = cv2.imread('assets/logo.jpg', -1)
#
# # Change first 100 rows to random pixels
# for i in range(100):
# 	for j in range(img.shape[1]):
# 		img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
#
# # Copy part of image
# tag = img[500:700, 600:900]
# img[100:300, 650:950] = tag
#
# cv2.imshow('Image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
# import numpy as np
# import cv2
#
# cap = cv2.VideoCapture(0)
#
# while True:
#     ret, frame = cap.read()
#     width = int(cap.get(3))
#     height = int(cap.get(4))
#
#     image = np.zeros(frame.shape, np.uint8)
#     smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
#     image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180)
#     image[height//2:, :width//2] = smaller_frame
#     image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180)
#     image[height//2:, width//2:] = smaller_frame
#
#     cv2.imshow('frame', image)
#
#     if cv2.waitKey(1) == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()
#
# import numpy as np
# import cv2
#
# cap = cv2.VideoCapture(0)
#
# while True:
#     ret, frame = cap.read()
#     width = int(cap.get(3))
#     height = int(cap.get(4))
#
#     img = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), 10)
#     img = cv2.line(img, (0, height), (width, 0), (0, 255, 0), 5)
#     img = cv2.rectangle(img, (100, 100), (200, 200), (128, 128, 128), 5)
#     img = cv2.circle(img, (300, 300), 60, (0, 0, 255), -1)
#     font = cv2.FONT_HERSHEY_SIMPLEX
#     img = cv2.putText(img, 'Tim is Great!', (10, height - 10), font, 2, (0, 0, 0), 5, cv2.LINE_AA)
#
#     cv2.imshow('frame', img)
#
#     if cv2.waitKey(1) == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()
#
# import numpy as np
# import cv2
#
# img = cv2.imread('assets/chessboard.png')
# img = cv2.resize(img, (0, 0), fx=0.75, fy=0.75)
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
# corners = np.int0(corners)
#
# for corner in corners:
# 	x, y = corner.ravel()
# 	cv2.circle(img, (x, y), 5, (255, 0, 0), -1)
#
# for i in range(len(corners)):
# 	for j in range(i + 1, len(corners)):
# 		corner1 = tuple(corners[i][0])
# 		corner2 = tuple(corners[j][0])
# 		color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))
# 		cv2.line(img, corner1, corner2, color, 1)
#
# cv2.imshow('Frame', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
# import numpy as np
# import cv2
#
# img = cv2.resize(cv2.imread('assets/soccer_practice.jpg', 0), (0, 0), fx=0.8, fy=0.8)
# template = cv2.resize(cv2.imread('assets/shoe.PNG', 0), (0, 0), fx=0.8, fy=0.8)
# h, w = template.shape
#
# methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
#             cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]
#
# for method in methods:
#     img2 = img.copy()
#
#     result = cv2.matchTemplate(img2, template, method)
#     min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
#     if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
#         location = min_loc
#     else:
#         location = max_loc
#
#     bottom_right = (location[0] + w, location[1] + h)
#     cv2.rectangle(img2, location, bottom_right, 255, 5)
#     cv2.imshow('Match', img2)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
#
#     import numpy as np
#     import cv2
#
#     cap = cv2.VideoCapture(0)
#     face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#     eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
#
#     while True:
#         ret, frame = cap.read()
#
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         faces = face_cascade.detectMultiScale(gray, 1.3, 5)
#         for (x, y, w, h) in faces:
#             cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)
#             roi_gray = gray[y:y + w, x:x + w]
#             roi_color = frame[y:y + h, x:x + w]
#             eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
#             for (ex, ey, ew, eh) in eyes:
#                 cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 5)
#
#         cv2.imshow('frame', frame)
#
#         if cv2.waitKey(1) == ord('q'):
#             break
#
#     cap.release()
#     cv2.destroyAllWindows()
#
#
# import numpy as np
# import cv2
#
# img = cv2.resize(cv2.imread('assets/soccer_practice.jpg', 0), (0, 0), fx=0.8, fy=0.8)
# template = cv2.resize(cv2.imread('assets/shoe.PNG', 0), (0, 0), fx=0.8, fy=0.8)
# h, w = template.shape
#
# methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
#            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]
#
# for method in methods:
#     img2 = img.copy()
#
#     result = cv2.matchTemplate(img2, template, method)
#     min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
#     if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
#         location = min_loc
#     else:
#         location = max_loc
#
#     bottom_right = (location[0] + w, location[1] + h)
#     cv2.rectangle(img2, location, bottom_right, 255, 5)
#     cv2.imshow('Match', img2)
#     cv2.waitKey(0)
#
# cv2.destroyAllWindows()
#
# import cv2
#
# # Rasmni o‘qish (rasm web.py bilan bir papkada)
# img = cv2.imread('kali linux 4.jpg', 1)
#
# # Agar fayl topilmasa xabar chiqadi
# if img is None:
#     print("⚠️ Xato: 'kali linux 4.jpg' topilmadi. Fayl nomi yoki joylashuvni tekshir!")
# else:
#     # Rasmni 2 baravar kichraytirish
#     img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
#
#     # Rasmni 90° o‘ngga aylantirish
#     img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
#
#     # Yangi rasmni saqlash
#     cv2.imwrite('new_img.jpg', img)
#
#     # Rasmni oynada ko‘rsatish
#     cv2.imshow('Aylantirilgan rasm', img)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
#
# import cv2
# import numpy as np
# import os
#
# # Fayl nomlari
# main_img = '14.jpeg'
# template_img = 'shoe.png'
#
# # Asosiy rasmni o‘qish
# img = cv2.imread(main_img, 0)
# if img is None:
#     print(f"❌ Asosiy rasm topilmadi: {main_img}")
#     exit()
#
# # Agar shoe.png mavjud bo‘lmasa — avtomatik shablon yasaymiz
# if not os.path.exists(template_img):
#     print(f"⚠️ Shablon topilmadi, yangi shablon yaratilmoqda: {template_img}")
#     # Rasmning kichik qismini (markazidan) kesib olamiz
#     h, w = img.shape
#     y, x = h // 4, w // 4
#     template = img[y:y + 100, x:x + 100]
#     cv2.imwrite(template_img, template)
# else:
#     template = cv2.imread(template_img, 0)
#
# # Shablon o‘lchamini olish
# h, w = template.shape
#
# # Moslashtirish usullari
# methods = [
#     cv2.TM_CCOEFF,
#     cv2.TM_CCOEFF_NORMED,
#     cv2.TM_CCORR,
#     cv2.TM_CCORR_NORMED,
#     cv2.TM_SQDIFF,
#     cv2.TM_SQDIFF_NORMED
# ]
#
# # Har bir metod bo‘yicha natijani chiqarish
# for method in methods:
#     img2 = img.copy()
#     result = cv2.matchTemplate(img2, template, method)
#     min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
#
#     # Metodga qarab joyni tanlaymiz
#     if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
#         location = min_loc
#     else:
#         location = max_loc
#
#     bottom_right = (location[0] + w, location[1] + h)
#     cv2.rectangle(img2, location, bottom_right, 255, 3)
#
#     # Natijani ko‘rsatish
#     cv2.imshow(str(method), img2)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

import cv2

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

print("""
---------------------------------------------
✅ Ishga tayyor:
   - 'S' bos — Yuzni aniqlashni boshlaydi
   - 'Q' bos — Dasturdan chiqadi
---------------------------------------------
""")

detect_enabled = False  # Dastlab aniqlash o‘chiq

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Kamera topilmadi yoki ulanmagan.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Yuzni aniqlash uchun oq-qora rasm kerak
    key = cv2.waitKey(1) & 0xFF

    if key == ord('s'):
        detect_enabled = True
        print("🟢 Aniqlash faollashdi (yuz kuzatuv rejimi)")

    if key == ord('q'):
        print("👋 Chiqilmoqda...")
        break

    if detect_enabled:
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(80, 80)
        )

        if len(faces) > 0:
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
                cv2.putText(frame, "✅ Odam topildi", (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        else:
            cv2.putText(frame, "❌ Obyekt yo'q", (30, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
    cv2.imshow("Yuzni aniqlash", frame)

cap.release()
cv2.destroyAllWindows()
