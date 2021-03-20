from fastapi import FastAPI,Request
from fastapi.encoders import jsonable_encoder
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import tensorflow as tf
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
one_step_reloaded = tf.saved_model.load('one_step')
templates = Jinja2Templates(directory="templates")
def get_results(s):
    states = None
    next_char = tf.constant([s])
    result = [next_char]

    for n in range(100):
        next_char, states = one_step_reloaded.generate_one_step(next_char, states=states)
        result.append(next_char)
    print(tf.strings.join(result)[0].numpy().decode("utf-8"))
    return tf.strings.join(result)[0].numpy().decode("utf-8")
@app.get("/") 
def read_root(request:Request):
    return templates.TemplateResponse("index.html",{"request":request})
@app.get("/sentence/{item}")
def read_item(item: str):
    x = get_results(item)
    return {"para":x}
