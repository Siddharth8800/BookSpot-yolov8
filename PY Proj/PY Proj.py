import pynecone as pc
from ultralytics import YOLO
from ultralytics.yolo.v8.detect.predict import DetectionPredictor
from tinydb import TinyDB, Query
import pandas as pd
from bookDetection import BookDetection
import csv

# ----- settings --------
db = TinyDB("books.json")
# User = Query()
csv_db = pd.read_csv("books.csv")
ans_db = pd.read_csv("results.csv")
detector = BookDetection(capture_index=0)
# -------------------------


# ------------ database -----------
class Books(pc.Model, table = True):
    Book_ID: int
    Name: str
    Author: str
    Page_Count: int
    Date_Published: str
# ---------------------------------




class QueryBooks(pc.State):
    ID: int
    name: str
    users: list[Books]

    def get_users(self):
        with pc.session() as session:
            self.users = (
                session.query(Books)
                .filter(Books.Book_ID.contains(self.ID))
                .all()
            )


class State(pc.State):
    show: bool = True

    def change(self):
        self.show = not (self.show)

    def realTime(self):
        detector()


        
# @pc.route(route=" ", title="BookSpot")
def index():
    return pc.vstack(
        pc.hstack(
            pc.heading(
            "BookSpot",
            background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
            background_clip="text",
            font_weight="bold",
            font_size="200px",
            ),
            pc.button(
            pc.icon(tag="moon"),
            on_click=pc.toggle_color_mode,
            ),
        ),
        
        pc.hstack(
           pc.center(
               pc.box(
                pc.button(
                "Training Data",
                border_radius="1em",
                box_shadow="rgba(151, 65, 252, 0.8) 0 15px 30px -10px",
                background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
                box_sizing="border-box",
                color="white",
                on_click = State.change,
                _hover={
                    "opacity": 0.85,
                  },
                ),
                padding = "5em"
               ),
            
                pc.box(
                pc.button(
                "Database",
                border_radius="1em",
                box_shadow="rgba(151, 65, 252, 0.8) 0 15px 30px -10px",
                background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
                box_sizing="border-box",
                color="white",
                on_click = State.change,
                _hover={
                    "opacity": 0.85,
                  },
                ),
                padding = "5em"
               ),
            
               pc.box(
                pc.button(
                "Test Model",
                border_radius="1em",
                box_shadow="rgba(151, 65, 252, 0.8) 0 15px 30px -10px",
                background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
                box_sizing="border-box",
                color="white",
                on_click = State.realTime,
                _hover={
                    "opacity": 0.85,
                  },
                ),
                padding = "5em"
               ),
           ),
        ),

       pc.cond(
        State.show,
        pc.box(
           pc.heading(
            "Training Results",
            background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
            background_clip="text",
            font_weight="bold",
            font_size="80px",
            align = "left"
            ),
            # pc.data_table(
            # data=csv_db[["ID", "Name", "Author", "Page_Count", "Date_Published"]],
            # pagination=True,
            # search=True,
            # sort=True,
            # resizable=True,
            # ),
            pc.hstack(
               pc.center(
                   pc.box(
                    pc.image(
                    src="/val_batch1_labels.jpg",
                    width="500px",
                    height="auto",
                    ),
                    padding = "0.5em"
                   ),
                   pc.box(
                    pc.image(
                    src="/val_batch1_pred.jpg",
                    width="500px",
                    height="auto",
                    ),
                    padding = "0.5em"
                   ),
                   pc.box(
                    pc.image(
                    src="/val_batch2_labels.jpg",
                    width="500px",
                    height="auto",
                    ),
                    padding = "0.5em"
                   ),
                   pc.box(
                    pc.image(
                    src="/val_batch2_pred.jpg",
                    width="500px",
                    height="auto",
                    ),
                    padding = "0.5em"
                   ),
               ),
            ),
            width = "1000px"
        ),
        pc.box(
            pc.heading(
            "Database",
            background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
            background_clip="text",
            font_weight="bold",
            font_size="80px",
            ),
            pc.data_table(
            data=csv_db[["ID", "Name", "Author", "Page_Count", "Date_Published"]],
            pagination=True,
            search=True,
            sort=True,
            resizable=True,
            ),
            width = "1000px"
        ),
       ),
    )


app = pc.App(state=State)
app.add_page(index)

app.compile()