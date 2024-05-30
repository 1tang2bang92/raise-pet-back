import json
import os
import gspread

from fastapi import FastAPI

from src.api import router


FILE_PATH = r'./cache/info.json'

if not os.path.exists(FILE_PATH):
    gc = gspread.service_account()
    sh = gc.open('breed_info')
    wks = sh.worksheet('info')
    data = wks.get_all_records()
    
    with open(FILE_PATH, 'w') as f:
        json.dump(data, f, indent=2)

app = FastAPI()
app.include_router(router.router)