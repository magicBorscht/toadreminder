from __future__ import annotations

from pydantic import BaseModel

from typing import Type

from aiosqlite import Row


class GifterDataSchema(BaseModel):
    gift_manager: int
    gift_receiver: int
    gift_manager_name: str = None
    gift_receiver_name: str = None


class GifterSchema(GifterDataSchema):
    id: int

    @classmethod
    def from_list(cls: Type[GifterSchema], toad: Row) -> GifterSchema:
        return cls(
                id=toad[0],
                gift_manager=toad[1],
                gift_receiver=toad[2],
            )
