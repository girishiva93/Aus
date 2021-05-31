from io import BytesIO
from PIL import Image
from django.core.files import File

def compressImage(image):
    img = Image.open(image).convert("RGB")
    im_io = BytesIO()

    if image.name.split('.')[1] == 'jpeg' or image.name.split('.')[1] == 'jpg':
        img.save(im_io , format='jpeg', optimize=True, quality=50)
        new_image = File(im_io, name="%s.jpeg" %image.name.split('.')[0],)
    else:
        img.save(im_io , format='png', optimize=True, quality=50)
        new_image = File(im_io, name="%s.png" %image.name.split('.')[0],)

    return new_image