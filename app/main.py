from fastapi import FastAPI
import uvicorn
from app.api.user import router as user_route


app = FastAPI()

@app.get("/")
def home():
    return {"message": "Server is running for Donation OpenHand"}


# include router
app.include_router(user_route,prefix="/user")

if __name__ == "__main__":

    uvicorn.run(app,port=8000,reload=True)
