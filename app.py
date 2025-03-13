from litestar import Litestar, get

@get("/names")
async def get_names() -> dict:
    
    return {"name": "Nasir Ahmed"}

app = Litestar([get_names])