import cv2

img = cv2.imread('solar-system.jpg')

cv2.putText(img,
            "Sun",
            (20, 300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )

cv2.putText(img,
            "Mercury",
            (100, 250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )

cv2.putText(img,
            "Venus",
            (190, 170),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )

cv2.putText(img,
            "Earth",
            (285, 270),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )

cv2.putText(img,
            "Mars",
            (380, 170),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )
cv2.putText(img,
            "Jupiter",
            (530, 50),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )

cv2.putText(img,
            "Saturn",
            (750, 320),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )

cv2.putText(img,
            "Uranus",
            (960, 130),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )

cv2.putText(img,
            "Neptune",
            (1100, 290),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )

cv2.imshow("output", img)
cv2.waitKey(0)