from torchvision import transforms
def random_rotation(image):
    RR = transforms.Compose([
        transforms.CenterCrop(600),
        transforms.Grayscale(num_output_channels=3),
        transforms.RandomRotation(degrees=(0, 180)),
    ])
    rr_image = RR(image)
    return rr_image
img = Image.open(os.path.join(r'C:\Users\DD\Desktop\加油\数据增强\test', str(i+1) + '.jpg'))
plt.figure(figsize=(8,8))

