import flet as ft
from ultralytics import YOLO
from ultralytics.yolo.v8.detect.predict import DetectionPredictor

def main(page: ft.Page):
    page.title = "Elevated button with 'click' event"

    def button_clicked(e):
        model = YOLO("1050ti_BookSpot.pt")
        results = model.predict(source='0', show=True)
        page.update()

    b = ft.ElevatedButton("Button with 'click' event", on_click=button_clicked, data=0)
    t = ft.Text()

    page.add(b, t)

ft.app(target=main)