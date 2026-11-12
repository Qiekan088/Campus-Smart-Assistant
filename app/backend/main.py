from uuid import uuid4
from fastapi import FastAPI, Response
app = FastAPI(title="Campus QA development environment")
@app.get("/api/v1/health")
def health(response: Response):
    request_id = str(uuid4())
    response.headers["X-Request-ID"] = request_id
    return {"data": {"status": "ok", "service": "campus-qa", "capabilities": ["environment_only"]}, "meta": {"request_id": request_id, "contract_version": "V0-contract-0.2", "mode": "mock"}}
