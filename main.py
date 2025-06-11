from fastapi import FastAPI
from router import rcomputer, rproduct, rcars, rstudents
app=FastAPI()
app.include_router(rcars.router)
app.include_router(rcomputer.router)
app.include_router(rproduct.router)
app.include_router(rstudents.router)











