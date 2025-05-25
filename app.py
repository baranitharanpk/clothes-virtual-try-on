from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse

app = FastAPI()

@app.post("/try-on/")
async def try_on(user_img: UploadFile = File(...), cloth_img: UploadFile = File(...)):
    # Save files temporarily
    with open("user.png", "wb") as f:
        f.write(await user_img.read())
    with open("cloth.png", "wb") as f:
        f.write(await cloth_img.read())

    # Call your model pipeline (like run.py or cloth-mask.py)
    result_path = "result.png"  # after model processing

    # TODO: Replace this with your actual processing logic
    # You probably need to call your functions from `remove_bg.py`, `run.py`, etc.

    return FileResponse(result_path, media_type="image/png")
