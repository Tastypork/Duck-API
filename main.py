from fastapi import FastAPI
import os, random

app = FastAPI()

DUCK_IMAGES_PATH = "./Ducks"

# Serve static files
from fastapi.staticfiles import StaticFiles
app.mount("/static/ducks", StaticFiles(directory="Ducks"), name="ducks")

@app.get("/")
def read_root():
    return {"msg": "Duck API is alive!"}

@app.get("/duck")
def get_duck():
    """Return a random duck image URL"""
    files = [f for f in os.listdir(DUCK_IMAGES_PATH) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    if not files:
        return {"error": "No duck images found."}

    duck_file = random.choice(files)
    return {
        "url": f"https://duck.jocal.dev/static/ducks/{duck_file}"
    }
