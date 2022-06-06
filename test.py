from bokeh.plotting import figure, show, output_file
from bokeh.models import CrosshairTool, HoverTool
import cv2
import numpy as np


output_file('image.html')
img = cv2.imread("../images/car.jpg", 0)
img = np.flipud(img)
y_range = img.shape[0]
x_range = img.shape[1]
TOOLTIPS = [
    ('name', "$name"),
    ('index', "$index"),
    ('pattern', '@pattern'),
    ("x", "$x"),
    ("y", "$y"),
    ("value", "@image"),
]
p = figure(frame_height=y_range, frame_width=x_range, x_range=(0, x_range), y_range=(0, y_range),
           tools='hover,wheel_zoom', tooltips=TOOLTIPS)

data = dict(image=[img],
            pattern=['img'],
            x=[0],
            y=[0],
            dw=[x_range],
            dh=[y_range])


p.image(source=data, image='image', x='x', y='y',
        dw='dw', dh='dh', name="Image Glyph", palette='Greys9')
show(p)
