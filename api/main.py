from internal.admin import app, engine, Base
import uvicorn
from routers.dog_routes import router


if __name__ == "__main__":

    Base.metadata.create_all(bind=engine)

    app.include_router(router)

    uvicorn.run(app, host="0.0.0.0", port=8000, debug=True)
