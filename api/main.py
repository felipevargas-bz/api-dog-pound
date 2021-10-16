from logging import debug
from internal.admin import app, SessionLocal, engine, Base
import uvicorn
from routers.routes import router


if __name__ == "__main__":

    Base.metadata.create_all(bind=engine)

    app.include_router(router)

    

    uvicorn.run(app, host="0.0.0.0", port=8000, debug=True)
