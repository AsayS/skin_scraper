import webbrowser
import win32clipboard
import keyboard
import time

all_found = []

# Create dict from txt file
d = {}
with open(r"buffids.txt", "r", encoding="utf8") as f:
    lines = f.readlines()
for line in lines:
    key, value = line.split(";")
    d[value] = key

def open_browser(link):
    webbrowser.open_new_tab("https://buff.163.com/goods/" + link)

# def get_id():
#     win32clipboard.OpenClipboard()
#     search = win32clipboard.GetClipboardData()
#     win32clipboard.CloseClipboard()
#     for key, value in d.items():
#             if search in key:
#                 all_found.append(value)
#     return all_found

# def item_name(id):
#     for key, value in d.items():
#         if str(id) in value:
#             return key



while not keyboard.is_pressed("f12"):
    time.sleep(0.05)
    if keyboard.is_pressed("f10"):
        win32clipboard.OpenClipboard()
        search = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        time.sleep(0.01)
        split_clip = search.split(" ")
        # print(split_clip)
        item_search = '%20'.join(split_clip)
        # print(item_search)
        link = "https://buff.163.com/market/csgo#tab=selling&page_num=1&search=" + item_search
        webbrowser.open_new_tab(link)
    if keyboard.is_pressed("f9"):
        win32clipboard.OpenClipboard()
        search = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        all_found.clear()
    
        # Search for buff value fomr skin name
        for key, value in d.items():
            if search in key:
                all_found.append(value)
                time.sleep(0.01)
                webbrowser.open_new_tab("https://buff.163.com/goods/" + all_found[0])
                break