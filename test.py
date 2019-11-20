# import cv2
#
#
# vc = cv2.VideoCapture("./fj.mp4")
# c = 1
# if vc.isOpened():
#     rval, frame = vc.read()
# else:
#     rval = False
# while rval:
#     rval, frame = vc.read()
#     cv2.imwrite('./test_image/' + str(c) + '.jpg', frame)
#     c = c + 1
#     cv2.waitKey(2)
# vc.release()

# import imageio
#
#
# def compose_gif():
#     img_paths = ["sc/9.png","sc/10.png","sc/11.png","sc/12.png"]
#     gif_images = []
#     for path in img_paths:
#         gif_images.append(imageio.imread(path))
#     imageio.mimsave("test.gif", gif_images, fps=3)
#
#
# compose_gif()

a = {'0': (-1, 0), '4': (0, 1), '8': (1, 0), '12': (0, -1)}
print(a['0'])