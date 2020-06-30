from PIL import Image, ImageDraw


def correct_img(path: str, result_name: str):
   img = Image.open(path)
   draw = ImageDraw.Draw(img)
   width = img.size[0]
   height = img.size[1]
   pix = img.load()

   # Изменение цвета
   for x in range(width):
      for y in range(height):
         r = pix[x, y][0]
         g = pix[x, y][1]
         b = pix[x, y][2]
         draw.point((x, y), (r-1, g-1, b-1))

   # Обрезка
   area = (width - 1, height - 1, width - 2, height - 2)
   cropped_img = img.crop(area)

   img.save()

def correct_size(path: str):
   img = Image.open(path)
   width = img.size[0]
   height = img.size[1]



   cr