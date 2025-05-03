const express = require('express')
const cors = require('cors')
const app = express()
app.use(cors({
    origin : 'http://localhost:5173'
}))
app.use(express.json())
const PORT = 4000

app.get('/', (req, res)=>{
    res.sendStatus(200)
})

app.post('/login', (req, res) => {
    res.send({
        isSuccess : true
    });
})

app.post('/signup', (req, res) => {
    const data = req.body;
    console.log(data);
    res.send({
        isSuccess : true
    });
})

app.listen(PORT, () => console.log(`server has started on ${PORT}`))