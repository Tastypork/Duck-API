from fastapi import FastAPI
from fastapi.responses import FileResponse
import os, random

app = FastAPI()

# Path to your duck images
DUCK_IMAGES_PATH = "./Ducks"

@app.get("/")
def read_root():
    return {"msg": "Duck API is alive!"}

@app.get("/duck")
def get_duck_root():
    return get_duck("root")

@app.get("/duck/{unique}")
def get_duck(unique: str):
    # Get all image files in the directory
    files = [f for f in os.listdir(DUCK_IMAGES_PATH) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    
    if not files:
        return {"error": "No duck images found."}
    
    # Pick a random duck image
    duck_file = random.choice(files)
    file_path = os.path.join(DUCK_IMAGES_PATH, duck_file)
    
    return FileResponse(
        file_path,
        headers={"Cache-Control": "no-store, no-cache, must-revalidate, max-age=0"})
