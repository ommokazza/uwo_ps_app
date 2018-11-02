import os

from PIL import Image

from uwo_ps_utils import common
from uwo_ps_utils import cropper


STATUS_WELCOME = "Welcome"
STATUS_FLOODED = "Flooded"
STATUS_PLUMMET = "Plummet"


TH = 200    #Threshhold
def __clear_bg(c):
    return int(c / TH) * 255
def __get_bytes(im):
    return im.point(__clear_bg).tobytes()

MK_BYTES = __get_bytes(Image.open("resources/chat_imgs/marketkeeper.png"))
MA_BYTES = __get_bytes(Image.open("resources/chat_imgs/marketappentice.png"))
FD_BYTES = __get_bytes(Image.open("resources/chat_imgs/flooded.png"))
PM_BYTES = __get_bytes(Image.open("resources/chat_imgs/plummet.png"))
WELCOMES = [
    __get_bytes(Image.open("resources/chat_imgs/welcome1.png")),
    __get_bytes(Image.open("resources/chat_imgs/welcome2.png")),
    __get_bytes(Image.open("resources/chat_imgs/welcome3.png"))
]

def __init_categories_bytes():
    categories = {}
    for f in common.get_image_paths("resources/chat_imgs", ".png"):
        basename = os.path.basename(f)
        if not basename.startswith("Class_"):
            continue
        name = basename.replace("Class_", "").replace(".png", "")
        categories[name] = __get_bytes(Image.open(f))

    return categories

CATEGORIES = __init_categories_bytes()

def get_status(im):
    for chat in cropper.get_chats(im):
        msg = cropper.get_msg(chat)
        if msg:
            status = __get_status(msg)
            if status == None:
                continue
            category = __get_category(msg)
            return (status, category)

    return None

def __get_status(msg):
    t1_bytes = __get_bytes(cropper.get_first_token_from_msg(msg))
    for welcome_bytes in WELCOMES:
        if t1_bytes == welcome_bytes:
            return STATUS_WELCOME

    if t1_bytes == FD_BYTES:
        return STATUS_FLOODED

    if t1_bytes == PM_BYTES:
        return STATUS_PLUMMET

    return None

def __get_category(msg):
    t1_bytes = __get_bytes(cropper.get_first_token_from_msg(msg))
    if t1_bytes == FD_BYTES:
        c_bytes = __get_bytes(cropper.get_flooded_second_token_from_msg(msg))
    elif t1_bytes == PM_BYTES:
        c_bytes = __get_bytes(cropper.get_plummet_second_token_from_msg(msg))
    else:
        return None

    for category in CATEGORIES.keys():
        if c_bytes == CATEGORIES[category]:
            return category

    return None
