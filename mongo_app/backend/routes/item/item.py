import logging
from bson.objectid import ObjectId
from fastapi import APIRouter, Depends, HTTPException
from starlette.status import HTTP_201_CREATED
from config.config import DB, CONF
from model.item import GamingItem

__all__ = ["item_router"]

item_router = APIRouter()


def validate_object_id(id_: str):
    try:
        _id = ObjectId(id_)
    except Exception:
        if CONF["fastapi"].get("debug", False):
            logging.warning("Invalid Object ID")
        raise HTTPException(status_code=400)
    return _id


async def _get_game_or_404(id_: str):
    _id = validate_object_id(id_)
    game_item = await DB.game.find_one({"_id": _id})
    if game_item:
        return fix_game_id(game_item)
    else:
        raise HTTPException(status_code=404, detail="Game not found")


def fix_game_id(game):
    if game.get("_id", False):
        game["id_"] = str(game["_id"])
        return game
    else:
        raise ValueError(f"No `_id` found! Unable to fix game ID for game: {game}")


@item_router.post("/", response_model=GamingItem, status_code=HTTP_201_CREATED)
async def add_gaming_item(game_item: GamingItem):
    game_op = await DB.game.insert_one(game_item.dict())
    if game_op.inserted_id:
        game = await _get_game_or_404(game_op.inserted_id)
        game["id_"] = str(game["_id"])
        return game
