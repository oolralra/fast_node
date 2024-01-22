from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List

app = FastAPI()

# 게시글을 저장할 리스트
messages = []


class Message(BaseModel):
    username: str
    text: str


# 게시판 홈
@app.get("/board", response_class=HTMLResponse)
def read_board():
    return """
    <html>
        <head>
            <title>게시판</title>
        </head>
        <body>
            <h1>게시판</h1>
            <form action="/board" method="post">
                <label for="username">이름:</label>
                <input type="text" id="username" name="username" required><br>
                <label for="text">메시지:</label>
                <textarea id="text" name="text" required></textarea><br>
                <button type="submit">게시글 작성</button>
            </form>
            <h2>게시글 목록</h2>
            <ul>
                %s
            </ul>
        </body>
    </html>
    """ % create_messages_list()


# 게시글 작성
@app.post("/board", response_class=HTMLResponse)
def create_message(username: str = Form(...), text: str = Form(...)):
    new_message = Message(username=username, text=text)
    messages.append(new_message)
    return read_board()


def create_messages_list():
    message_list_html = ""
    for message in messages:
        message_list_html += f"<li><strong>{message.username}:</strong> {message.text}</li>"
    return message_list_html
