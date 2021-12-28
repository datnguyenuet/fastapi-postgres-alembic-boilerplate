from sqlalchemy.sql import func
from db import db, metadata, sqlalchemy

from fastapi import HTTPException
from starlette.status import HTTP_404_NOT_FOUND


tests = sqlalchemy.Table(
    "tests",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String, nullable=False),
    sqlalchemy.Column(
        "created_at", sqlalchemy.DateTime(timezone=True), server_default=func.now()
    ),
    sqlalchemy.Column(
        "updated_at", sqlalchemy.DateTime(timezone=True), onupdate=func.now()
    ),
)


class Tests:
    @classmethod
    async def get(cls, id):
        query = tests.select().where(tests.c.id == id)
        test = await db.fetch_one(query)
        if not test:
            raise HTTPException(HTTP_404_NOT_FOUND)
        return test

    @classmethod
    async def create(cls, **test):
        query = tests.insert().values(**test)
        test_id = await db.execute(query)
        return test_id
