from internal.admin import app, engine, Base
import uvicorn
from routers.dog_routes import router as dog_router
from routers.user_routes import router as user_router


if __name__ == "__main__":

    while 1:
        try:
            Base.metadata.create_all(bind=engine)

            app.include_router(dog_router)
            app.include_router(user_router)

            uvicorn.run(app, host="0.0.0.0", port=8000)
        except Exception as e:
            print("-- Error {} -- Retrying to start!".format(e))
            continue
        break
