import cv2

vidcap = cv2.VideoCapture('这里输入视频地址')
success,image = vidcap.read()
fps = int(vidcap.get(cv2.CAP_PROP_FPS))
count = 0
while success:
    if count % fps == 0:
        cv2.imwrite("这里输入存储图片的地址/%d.jpg" % int(count / fps), image)
    print('Process %dth seconds: ' % int(count / fps), success)
    success,image = vidcap.read()
    count += 1
