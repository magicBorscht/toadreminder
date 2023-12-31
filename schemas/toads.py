from __future__ import annotations

from pydantic import BaseModel


class ToadDataSchema(BaseModel):
    name: str
    name_gen: str
    tg_handler: str
    birthday: str
    name_dat: str
    manager_notified: bool


class ToadSchema(ToadDataSchema):
    id: int

    @classmethod
    def from_list(cls, toad):
        return cls(
                id=toad[0],
                name=toad[1],
                name_gen=toad[2],
                tg_handler=toad[3],
                birthday=toad[4],
                name_dat=toad[5],
                manager_notified=bool(toad[6])
            )
