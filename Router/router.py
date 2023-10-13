from fastapi import FastAPI

from modules import post, ping, google_login


app = FastAPI()


@app.on_event("startup")
async def startup():
    print("==========DB Connect==========")


@app.on_event("shutdown")
async def shutdown():
    # db disconnect
    print("==========DB Disconnect==========")


app.include_router(post.router)
app.include_router(ping.router)
app.include_router(google_login.router)
