from os import listdir
from PIL import Image, ImageFilter, ImageEnhance

# blur = True
blur = False

sharp = True
# sharp = False

# median = True
median = False

sharp_times = 9
gauss_rad = 3
median_size = 5

img_names = [f for f in listdir('./input')]

# for img_name in img_names:
#     try:
#         img = Image.open('./input.full/' + img_name)
#         if img.size != (1920, 1080):
#             print(img_name)
#             continue
#         # print(img.size)
#
#     except IOError:
#         pass

print("sharp: " + str(sharp))
print("sharp times: " + str(sharp_times))
print("blur: " + str(blur))
print("blur rad: " + str(gauss_rad))
print("median: " + str(median))
print("median size: " + str(median_size))

for img_name in img_names:
    try:
        test_img = Image.open('./input/' + img_name)

        width, height = test_img.size
        delta = 4

        delta_add = 0

        while (width > 20 and height > 20):
            old_width = width
            width = width - delta*2
            old_height = height
            height = height - delta*2

            delta_add += delta*2
            # delta_add += delta

            sub_img = test_img.crop((delta_add, delta_add, width, height)).rotate(180)
            test_img.paste(sub_img, (delta_add, delta_add))

        test_img = test_img.convert(mode='RGBA')

        test_img2 = test_img
        if blur:
            test_img2 = test_img.filter(ImageFilter.GaussianBlur(radius=gauss_rad))

        test_img3 = test_img2
        if median:
            test_img3 = test_img2.filter(ImageFilter.MedianFilter(size=median_size))

        test_img4 = test_img3

        if sharp:
            test_img4 = test_img3.filter(ImageFilter.MinFilter(size=sharp_times))


        test_img4.save('altered/altered_' + img_name.split('.')[0] + '.png')
    except:
        pass
