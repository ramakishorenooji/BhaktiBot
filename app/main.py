from fastapi import FastAPI
from app.routes import festival_routes
from app.scheduler import scheduler  # Ensuring scheduler starts

app = FastAPI()

# Include API routes
app.include_router(festival_routes.router)

@app.get("/")
def home():
    return {"message": "Hindu Festival Wisher API"}
