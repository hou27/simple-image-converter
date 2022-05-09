# image_view_converter

import shutil
import PySimpleGUI as sg 
import PIL.Image as Image
import io # python에서 input output 관리하는 라이브러리
import tempfile # 메모리 상에 저장되는 임시 파일

# converters
from converter.bw import bw, bw_dithering
from converter.grayscale import grayscale
from converter.four_color import four_color
from converter.sepia import create_sepia as sepia

# filters
from filter.blur_image import blur
from filter.contour_image import contour
from filter.detail_image import detail
from filter.edge_enhance_image import edge_enhance
from filter.emboss_image import emboss
from filter.find_edges_image import find_edges
from filter.gaussian_blur_image import gaussian_blur
from filter.sharpen_image import sharpen
from filter.smooth_image import smooth

tmp_file = tempfile.NamedTemporaryFile(suffix=".png").name

file_types = [("JPEG (*jpg)","*.jpg"), ("PNG (*png)","*.png")]

effects = {
    "Grayscale": grayscale,
    "Black and White": bw,
    "Bw_dithering": bw_dithering,
    "Four_color": four_color,
    "Sepia": sepia,
}

effect_name = list(effects.keys())

filters = {
    "Blur": blur,
    "Contour": contour,
    "Detail": detail,
    "Edge Enhance": edge_enhance,
    "Emboss": emboss,
    "Find Edges": find_edges,
    "Gaussian Blur": gaussian_blur,
    "Sharpen": sharpen,
    "Smooth": smooth,
}

filter_name = list(filters.keys())

layout = [
    [sg.Image(key="IMAGE", size=(640, 480))],
    [sg.Text("이미지 선택"), sg.Input(size=(30, 1), key="FILENAME"), sg.FileBrowse(file_types=file_types), sg.Button("Load")],
    [sg.Text("적용할 효과"), sg.Combo( effect_name, default_value="Black and White", key="EFFECT", enable_events= True, ), sg.Button("효과 적용하기")],
    [sg.Text("적용할 필터"), sg.Combo( filter_name, default_value="Blur", key="FILTER", enable_events= True, ), sg.Button("필터 적용하기")],
    [sg.Button("Save"), sg.Button("Exit")]
]

def image_viewer():
    print("Image Viewer Started")

    window = sg.Window("Image Viewer", layout, size=(640, 700))

    while True:
        event, value = window.read() # Read the window events
        print(event, " ", value)
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        elif event == "Load" and value["FILENAME"] != "":
            print(value["FILENAME"])
            image = Image.open(value["FILENAME"])
            # image.show()
            image.thumbnail((640, 480))
            bio = io.BytesIO()
            image.save(bio, "PNG")
            window["IMAGE"].update(data=bio.getvalue(), size = (640, 480))
        elif event == "효과 적용하기" or event == "EFFECT" and value["FILENAME"] != "":
            print(value["EFFECT"])
            effects[value["EFFECT"]](value["FILENAME"], tmp_file)
            image = Image.open(tmp_file)
            image.thumbnail((640, 480))
            bio = io.BytesIO()
            image.save(bio, "PNG")
            window["IMAGE"].update(data=bio.getvalue(), size = (640, 480))
        elif event == "필터 적용하기" or event == "FILTER" and value["FILENAME"] != "":
            print(value["FILTER"])
            filters[value["FILTER"]](value["FILENAME"], tmp_file)
            image = Image.open(tmp_file)
            image.thumbnail((640, 480))
            bio = io.BytesIO()
            image.save(bio, "PNG")
            window["IMAGE"].update(data=bio.getvalue(), size = (640, 480))
        elif event == "Save" and value["FILENAME"]:
            save_filename = sg.popup_get_file("Save Image", file_types=file_types, save_as=True, no_window=True)

            if save_filename:
                try:
                    shutil.copy(tmp_file, save_filename)
                    sg.popup("변환된 이미지가 성공적으로 저장되었습니다.")
                except Exception as e:
                    sg.popup("저장에 실패했습니다.\n" + str(e))

    window.close()

