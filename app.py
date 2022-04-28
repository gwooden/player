from typing import List,Optional
from fastapi import FastAPI
from db.config import engine, Base, async_session
from db.dals.player_dal import PlayerDAL
from db.models.player import Player

app = FastAPI()

@app.post("/players")
async def create_player(firstName: str, lastName: str, number: int):
    async with async_session() as session:
        async with session.begin():
            player_dal = PlayerDAL(session)
            return await player_dal.create_player(firstName, lastName, number)

@app.get("/players")
async def get_all_players() -> List[Player]:
    async with async_session() as session:
        async with session.begin():
            player_dal = PlayerDAL(session)
            return await player_dal.get_all_players()

@app.put("/players/{player_id}")
async def update_player(player_id: int, firstName: Optional[str] = None, lastName: Optional[str] = None, number: Optional[int] = None):
    async with async_session() as session:
        async with session.begin():
            player_dal = PlayerDAL(session)
            return await player_dal.update_player(player_id, firstName, lastName, number)