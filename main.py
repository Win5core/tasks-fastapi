from fastapi import FastAPI

from routes import router


# from fastapi.responses import HTMLResponse
# from fastapi.staticfiles import StaticFiles
# from fastapi.templating import Jinja2Templates


app = FastAPI()
app.include_router(router=router)
