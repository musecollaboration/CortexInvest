# # main.py
# from fastapi import FastAPI
# from src.cortexinvest.backend.di.container import get_container
# from src.cortexinvest.backend.presentation.api.routes import users, auth
# from src.cortexinvest.ai.application.services import prediction_router


# def create_app() -> FastAPI:
#     app = FastAPI(title="CortexInvest")

#     # DI
#     container = get_container()

#     # Backend routes
#     app.include_router(users.router, prefix="/api/v1/users", tags=["Users"])
#     app.include_router(auth.router, prefix="/api/v1/auth", tags=["Auth"])

#     # AI routes
#     app.include_router(prediction_router, prefix="/api/v1/ai", tags=["AI"])

#     return app


# app = create_app()

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)
