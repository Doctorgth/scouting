from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from methods import catch_session
from config import database
from db_api import get_api


app=0

def main():


    engine = create_engine(database.url)

    # Создаем сессию
    Session = sessionmaker(bind=engine)
    session = Session()
    catch_session(session)
    try:
        import uvicorn
        global app
        app=get_api()
        return app
        uvicorn.run(app, host="127.0.0.1", port=5000)

    finally:
        # Закрываем сессию
        session.close()
        # Освобождаем соединение из пула соединений
        engine.dispose()


app=main()
