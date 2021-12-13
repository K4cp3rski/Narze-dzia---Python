import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy.ndimage import gaussian_filter
import argparse
import textwrap

parser = argparse.ArgumentParser(prog="pd6.12.py",
                                 formatter_class=argparse.RawDescriptionHelpFormatter,
                                 description="Image Blurring program",
                                 epilog="Thanks for using our program!")
parser.add_argument("-x", help="x axis of gaussian blur", nargs="?", type=float, default=2)
parser.add_argument("-y", help="y axis of gaussian blur", nargs="?", type=float, default=2)
parser.add_argument("-xy", help="xy axis of gaussian blur", nargs="?", type=float, default=2)
parser.add_argument("inputfile", help="The file to be blurred", nargs="+")

args = parser.parse_args()

filename = args.inputfile[0]

plt.figure()
img = mpimg.imread("{}".format(filename))

if args.x == args.y == 2:
    img = gaussian_filter(img, sigma=args.xy)
else:
    img = gaussian_filter(img, sigma=(args.x, args.y))


plt.imshow(img)
plt.show()


