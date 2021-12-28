from models import Tests
from schemas import CreateTestPayload, TestDetail
from app import app


@app.post("/tests/", tags=["Tests"])
async def create_user(payload: CreateTestPayload):
    test_id = await Tests.create(**payload.dict())
    return {"test_id": test_id}


@app.get("/tests/{test_id}", tags=["Tests"])
async def get_user(test_id: int):
    test = await Tests.get(test_id)
    return TestDetail(**test).dict()
