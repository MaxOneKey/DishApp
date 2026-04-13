import os
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

# 1. Визначаємо, де лежить цей файл (web_app.py)
base_dir = os.path.dirname(os.path.abspath(__file__))

# 2. Склеюємо шлях до папки templates
templates_dir = os.path.join(base_dir, "templates")

# 3. Перевіряємо для себе, чи правильний шлях (виведеться в консоль при старті)
print(f"Шукаю шаблони тут: {templates_dir}")

# 4. Підключаємо шаблони за повним шляхом
templates = Jinja2Templates(directory=templates_dir)

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})