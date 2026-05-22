from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from tools.transcript import get_transcript
from tools.summarize import summarize_video
from tools.qa import ask_video

app = FastAPI(title="YouTube MCP Server")

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


class VideoRequest(BaseModel):
    url: str


class QARequest(BaseModel):
    url: str
    question: str


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )


@app.post("/get_transcript")
def transcript(req: VideoRequest):
    return {
        "result": get_transcript(req.url)
    }


@app.post("/summarize")
def summarize(req: VideoRequest):
    return {
        "result": summarize_video(req.url)
    }


@app.post("/ask")
def ask(req: QARequest):
    return {
        "result": ask_video(req.url, req.question)
    }