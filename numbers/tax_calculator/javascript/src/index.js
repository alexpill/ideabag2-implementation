const express = require('express');
const app = express();
const port = 3000;

app.use(express.static("public"));

app.get('/', (req, res) => {
    res.sendFile('public/html/', {root: __dirname})
})

app.listen(
    port,
    () => console.info('Server listening on port ', port)
);