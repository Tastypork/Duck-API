from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import os, random
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI()

HTML_DIR = Path("./html")  # this is the symlink

# Serve the actual HTML files
app.mount("/ducks/html", StaticFiles(directory=HTML_DIR), name="ducks_html")

@app.get("/user/{user_id}")
async def redirect_user(user_id: str):
    file_path = HTML_DIR / f"{user_id}.html"
    if file_path.exists():
        return RedirectResponse(url=f"/ducks/html/{user_id}.html")
    return {"error": "No ducks found for this user"}

DUCK_IMAGES_PATH = "./Ducks"

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
