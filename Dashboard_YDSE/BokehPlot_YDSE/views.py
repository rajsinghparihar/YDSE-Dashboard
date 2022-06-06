from django.shortcuts import render
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import CrosshairTool
import cv2
import numpy as np
import urllib.request

# Create your views here.


def plot(request):
    YDSE = cv2.imread("images\pattern.jpg", 0)
    YDSE = np.flipud(YDSE)
    y_range = YDSE.shape[0]
    x_range = YDSE.shape[1]
    TOOLTIPS = [
        ('name', "$name"),
        ("x", "$x"),
        ("y", "$y"),
    ]
    plot = figure(frame_height=y_range, frame_width=x_range, x_range=(0, x_range), y_range=(0, y_range),
                  tools='hover,wheel_zoom', tooltips=TOOLTIPS)
    plot.add_tools(CrosshairTool(line_color='green', line_width=2))

    data = dict(image=[YDSE],
                pattern=['YDSE'],
                x=[0],
                y=[0],
                dw=[x_range],
                dh=[y_range])

    plot.image(source=data, image='image', x='x', y='y',
               dw='dw', dh='dh', name="YDSE Pattern", palette='Greys9')
    script, div = components(plot)
    # form control
    config_value = None
    isConnected = urllib.request.urlopen(
        "http://blynk-cloud.com/O-6QCcrh1pgsykl0Qo-bsYTYjvvsn5I0/isHardwareConnected").read().decode('utf-8')
    if isConnected == 'true':
        isConnected = True
    else:
        isConnected = False

    if request.method == "POST":
        config_value = request.POST.get('val')
        urllib.request.urlopen(
            f"http://blynk-cloud.com/O-6QCcrh1pgsykl0Qo-bsYTYjvvsn5I0/update/v3?value={min(abs(int(config_value)),2)}").read()

    return render(request, 'plot.html', {'isConnected': isConnected, 'div': div, 'script': script})


def home(request):
    YDSE = cv2.imread("images\pattern.jpg", 0)
    YDSE = np.flipud(YDSE)
    y_range = YDSE.shape[0]
    x_range = YDSE.shape[1]
    TOOLTIPS = [
        ('name', "$name"),
        ("x", "$x"),
        ("y", "$y"),
    ]
    plot = figure(frame_height=y_range, frame_width=x_range, x_range=(0, x_range), y_range=(0, y_range),
                  tools='hover,wheel_zoom', tooltips=TOOLTIPS)
    plot.add_tools(CrosshairTool(line_color='green', line_width=2))

    data = dict(image=[YDSE],
                pattern=['YDSE'],
                x=[0],
                y=[0],
                dw=[x_range],
                dh=[y_range])

    plot.image(source=data, image='image', x='x', y='y',
               dw='dw', dh='dh', name="YDSE Pattern", palette='Greys9')
    script, div = components(plot)

    return render(request, 'base.html', {'script': script, 'div': div})
