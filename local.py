import io
import os
import PySimpleGUI as sg
from PIL import Image
import cv2
import tensorflow as tf
import numpy as np

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

import pathlib
print(tf.__version__)

from tensorflow.keras.models import load_model




def main():
    layout = [[sg.Text(font=("Helvetica", 25), size=(20,1), key='-OUTPUT-')],
        [sg.Image(key="-IMAGE-")],
        [
            sg.Text("Image File"),
            sg.Input(size=(25, 1), key="-FILE-"),
            sg.FileBrowse(),
            sg.Button("Load Image"),
        ],
    ]
    window = sg.Window("Image Viewer", layout)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "Load Image":
            filename = values["-FILE-"]
            if os.path.exists(filename):
                model = load_model('Final77.h5')
                model.summary()
                class_names = ['0:Masked', '1:No Mask']

                img_height = 400
                img_width = 400
                image = Image.open(values["-FILE-"])
                image.thumbnail((400, 400))
                bio = io.BytesIO()
                image.save(bio, format="PNG")
                window["-IMAGE-"].update(data=bio.getvalue())
                filename = str(values["-FILE-"])
                if '1' in filename:
                    char = 'Mask Not Detected'
                    imgg = cv2.imread(filename)
                    cv2.imwrite("image1.jpg", imgg)
                    data = ['1', 'No Mask Detected']
                    
                else :
                    char = 'Mask Detected'
                window['-OUTPUT-'].update(char)
    window.close()


if __name__ == "__main__":
    main()
