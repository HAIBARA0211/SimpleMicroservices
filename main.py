from fastapi import FastAPI
from resources.people import router as people_router
from resources.addresses import router as addresses_router

app = FastAPI()
app.include_router(people_router)
app.include_router(addresses_router)
