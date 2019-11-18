import cv2


# vc = cv2.VideoCapture("./sc.mp4")
# c = 1
# if vc.isOpened():
#     rval, frame = vc.read()
# else:
#     rval = False
# while rval:
#     rval, frame = vc.read()
#     cv2.imwrite('./test_image/' + str(c) + '.jpg', frame)
#     c = c + 1
#     cv2.waitKey(1)
# vc.release()

import imageio


def compose_gif():
    img_paths = ["sc/1.png","sc/2.png","sc/3.png","sc/4.png"]
    gif_images = []
    for path in img_paths:
        gif_images.append(imageio.imread(path))
    imageio.mimsave("test.gif", gif_images, fps=3)


compose_gif()