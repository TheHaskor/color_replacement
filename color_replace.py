from PIL import Image
import numpy


def get_image(image_path):
  """Get a numpy array of an image so that one can access values[x][y]."""
  image = Image.open(image_path, 'r')
  width, height = image.size
  pixel_values = list(image.getdata())
  if image.mode == 'RGB':
    channels = 3
  elif image.mode == 'L':
    channels = 1
  else:
    print("Unknown mode: %s" % image.mode)
    return None
  pixel_values = numpy.array(pixel_values).reshape((width, height, channels))
  return pixel_values


def similar_color(c1, c2, threshold=40):
  for index, i in enumerate(c1):
    if c1[index] > c2[index] + threshold or c1[index] < c2[index] - threshold:
      return False
  return True


def change_img(arr, from_rgb=[237, 28, 36], to_rgb=[3, 78, 252]):
  for index1, p in enumerate(arr):
    for index2, i in enumerate(p):
      if similar_color(list(i), from_rgb):
        arr[index1][index2] = numpy.array(to_rgb)


def plot_img(array):
    array = numpy.array(array, dtype=numpy.uint8)
    img = Image.fromarray(array)
    img.save('new.png')



if __name__ == '__main__':
  img_loc = r"C:\Users\User\Desktop\dtl\tree-576848_1280.png"
  arr = get_image(img_loc)
  change_img(arr)
  plot_img(arr)
