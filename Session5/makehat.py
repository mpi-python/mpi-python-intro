from PIL import Image

im = Image.open('hat.png')
im = im.resize((400, 400), Image.BICUBIC)

for deg in range(1,361):
        rot_img = im.rotate(deg)
        image_file = ('hat' + str(deg) + '.png')
        rot_img.save('hat' + str(deg) + '.png')
        print(f'wrote image {image_file} to file')