from fastapi import FastAPI
from fastapi.responses import FileResponse
import os, random, uuid

app = FastAPI()

DUCK_IMAGES_PATH = "./Ducks"

# mapping of unique_id -> file
duck_map = {}

@app.get("/")
def read_root():
    return {"msg": "Duck API is alive!"}

@app.get("/duck")
def get_duck_root():
    """Create a new unique ID and let get_duck handle it."""
    unique_id = str(uuid.uuid4())
    return get_duck(unique_id)

@app.get("/duck/{unique}")
def get_duck(unique: str):
    """Return the same duck for the same unique id, or create one if it doesn’t exist yet."""
    if unique not in duck_map:
        files = [f for f in os.listdir(DUCK_IMAGES_PATH) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
        if not files:
            return {"error": "No duck images found."}
        duck_map[unique] = random.choice(files)

    duck_file = duck_map[unique]
    file_path = os.path.join(DUCK_IMAGES_PATH, duck_file)

    return FileResponse(
        file_path,
        headers={"Cache-Control": "no-store, no-cache, must-revalidate, max-age=0"}
    )
