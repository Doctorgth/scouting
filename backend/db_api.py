from methods import add_record, get_record, delete_record, update_record
from fastapi import FastAPI, Form

app = FastAPI()


@app.post("/add_record")
async def add_record1(table_name: str = Form(...), data=Form(...)):
    result = add_record(table_name, data)
    return result


@app.post("/remove_record")
async def remove_record(table_name: str = Form(...), column=Form(...), value=Form(...)):
    result = delete_record(table_name, column, value)
    return result


@app.post("/get_record")
async def get_record1(table_name: str = Form(...), column=Form(...), value=Form(...)):

    result = get_record(table_name, column, value)
    print("GETTET RESULT")

    return result


@app.post("/update_record")
async def update_record1(table_name: str = Form(...), field_name=Form(...), new_value=Form(...), condition_field=Form(...),
                      condition_value=Form(...)):
    result = update_record(table_name, field_name, new_value, condition_field, condition_value)
    return result


def get_api():
    global app
    return app
