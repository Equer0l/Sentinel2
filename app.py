from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import PlainTextResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import shutil
from pathlib import Path
from attributeCalculator import get_width, get_heigth, get_num_bands, get_crs, get_bounding_box, convertToPng

app = FastAPI()

app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=PlainTextResponse)
def read_root():
    return "Welcome to the Sentinel 2 API \nUse /attributes to get the image attributes \nUse /thumbnail"


@app.get("/attributes")
def read_attributes(request: Request):
    return templates.TemplateResponse("imageUpload.html", {"request": request, "function" : "attributes"})

@app.get("/thumbnail")
def read_thumbnail(request: Request):
    return templates.TemplateResponse("imageUpload.html", {"request": request, "function" : "thumbnail"})

@app.post("/uploadfileAttribute/")
async def upload(request: Request, file: UploadFile = File(...)):
    upload_folder = Path("uploads")
    upload_folder.mkdir(exist_ok=True)
    file_path = upload_folder / file.filename

    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    width = get_width(file_path)
    height = get_heigth(file_path)
    num_bands = get_num_bands(file_path)
    crs = get_crs(file_path)
    bounding_box = get_bounding_box(file_path)

    return templates.TemplateResponse("attributeresults.html", {"request": request, 
                                                                "width": width, 
                                                                "height" : height, 
                                                                "num_bands": num_bands, 
                                                                "crs": crs, 
                                                                "bounding_box": bounding_box})
    
    
@app.post("/uploadfileThumbnail/")
async def upload(request: Request, file: UploadFile = File(...)):
    upload_folder = Path("uploads")
    upload_folder.mkdir(exist_ok=True)
    file_path = upload_folder / file.filename

    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    convertToPng(file_path)
    path = Path.cwd() / "output_thumbnail.png"
    return templates.TemplateResponse("imagepng.html", {"request": request, "path" : path})