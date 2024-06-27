const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const port = 3000;

// Pug 템플릿 엔진 설정
app.set('view engine', 'pug');
app.set('views', './views');

// body-parser 미들웨어 설정
app.use(bodyParser.urlencoded({ extended: true }));

// 게시글을 저장할 리스트
let messages = [];

// 게시판 홈
app.get('/board', (req, res) => {
    res.render('board', { messages: messages });
});

// 게시글 작성
app.post('/board', (req, res) => {
    const username = req.body.username;
    const text = req.body.text;

    const newMessage = { username: username, text: text };
    messages.push(newMessage);

    res.redirect('/board');
});

// 서버 시작
app.listen(port, () => {
    console.log(`Server is running at http://localhost:${port}`);
});
