"""
This program generates the Warhol effect based on the original image.
"""

from simpleimage import SimpleImage
import _tkinter

N_ROWS = 2
N_COLS = 3
PATCH_SIZE = 222
WIDTH = N_COLS * PATCH_SIZE
HEIGHT = N_ROWS * PATCH_SIZE
PATCH_NAME = 'images/simba-sq.jpg'

def main():

    final_image = SimpleImage.blank(WIDTH, HEIGHT)
    for y in range(N_ROWS):
        for x in range(N_COLS):
            patch = make_recolored_patch(1.5, 1*y, 1.5*x)
            final_image = add_to_final_image(patch, final_image, x, y)

    final_image.show()

def make_recolored_patch(red_scale, green_scale, blue_scale):
    '''
    Implement this function to make a patch for the Warhol Filter. It
    loads the patch image and recolors it.
    :param red_scale: A number to multiply each pixels' red component by
    :param green_scale: A number to multiply each pixels' green component by
    :param blue_scale: A number to multiply each pixels' blue component by
    :return: the newly generated patch
    '''
    patch = SimpleImage(PATCH_NAME)
    for pixel in patch:
        pixel.red *= red_scale
        pixel.green *= green_scale
        pixel.blue *= blue_scale
    return patch

def add_to_final_image(image, final_image, x, y):

    for j in range(image.height):
        for i in range(image.width):
            pixel = image.get_pixel(i, j)
            final_image.set_pixel(i+(x)*PATCH_SIZE, j+(y)*PATCH_SIZE, pixel)

    return final_image


if __name__ == '__main__':
    main()
