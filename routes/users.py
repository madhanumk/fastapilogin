from fastapi import APIRouter
from config.db import conn 
from models.index import users
from schemas.users import User
user  = APIRouter()
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


# Helper function to convert Row to dictionary
def row_to_dict(row):
    return {key: row[key] for key in row.keys()}


@user.get("/")
async def read_data():
    result = conn.execute(users.select())
    
    # Convert rows to dictionaries
    books = [dict(row) for row in result.mappings()]
    
    # Encode the data for the JSON response
    response_data = jsonable_encoder({"book": books})
    
    # Return as a JSON response
    return JSONResponse(
        status_code=200,
        content={"status_code": 200, "result": response_data}
    )


@user.get("/{id}")
async def read_data(id:int):
    return conn.execute(users.select().where(users.c.id == id )).fetchall()


@user.post("/")
async def write_data(user: User):
    conn.execute(users.insert().values(
        id = user.id,
        name = user.name,
        email = user.email,
        password = user.password
    ))
    conn.commit()

    # Fetch all rows from the table
    result = conn.execute(users.select())
    return [dict(row) for row in result.mappings()]


@user.put("/{id}")
async def update_data(id:int, user: User):
    conn.execute(users.update().values(
        name = user.name,
        email = user.email,
        password = user.password
    ).where(users.c.id == id))


    return conn.execute(users.select()).fetchall()


@user.delete("/{id}")
async def delete_data(id:int):
    conn.execute(users.delete().where(users.c.id == id))

    return conn.execute(users.select()).fetchall()
