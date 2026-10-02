from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="First API", version="0.1.0")


class EchoRequest(BaseModel):
    mensaje: str = Field(min_length=1, max_length=200)
    veces: int = Field(ge=1, le=10, default=1)


class EchoResponse(BaseModel):
    resultado: str
    longitud: int


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/echo", response_model=EchoResponse)
def echo(payload: EchoRequest) -> EchoResponse:
    texto = " ".join([payload.mensaje] * payload.veces)
    return EchoResponse(resultado=texto, longitud=len(texto))
