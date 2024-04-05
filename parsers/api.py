from parsers import techcrunch_parser
from fastapi import FastAPI, Form

app = FastAPI()
site_list=["techcrunch"]

@app.post("/get_news")# возвращает новостную ленту с сайта, если для неё есть парсер
async def get_news(site: str = Form(...)):
    if site in site_list:
        if site==site_list[0]:
            try:
                x=techcrunch_parser()
                result=x.search_latest_news()
                return result
            except Exception as e:
                return {"code":-2,"Exeption":e}
    else:
        return -1

@app.post("/get_new")# возвращает текст новости, применяет специальный парсер для сайта, если такой парсер существует
async def get_new(site: str = Form(...),url: str = Form(...)):
    if site in site_list:
        if site==site_list[0]:
            try:
                x=techcrunch_parser()
                result=x.download_text(url)
                return result
            except Exception as e:
                return {"code": -2, "Exeption": e}
    else:
        return -1


@app.post("/search")# возвращает текст новости, применяет специальный парсер для сайта, если такой парсер существует
async def search(site: str = Form(...),query: str = Form(...)):
    if site in site_list:
        if site==site_list[0]:
            try:
                x=techcrunch_parser()
                result=x.search_startup(query)
                return result
            except Exception as e:
                return {"code":-2,"Exeption":e}
    else:
        return -1



def get_api():
    global app
    return app
