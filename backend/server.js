const express = require('express')
const cors = require('cors')
const { Kafka } = require('kafkajs')
const app = express()
const PORT = 4000

app.use(express.json())
app.use(cors({
    origin : 'http://localhost:5173'
}))

const kafka = new Kafka({
    clientId : 'my-app',
    brokers : ['192.168.1.253:9092']
})
const producer = kafka.producer();

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

app.post('/createService', async (req , res) => {
    const data = req.body;
    console.log(data);
    await producer.connect();
    const testMessage = {
        user_name: data.userName,
        app_name: data.serviceName,
        image_name: data.imageUrl,
        container_port: data.port,
        hash_value : data.hashValue
    }
    await producer.send({
        topic: 'main',
        messages: [
            {value : JSON.stringify(testMessage)}
        ],
    })
    console.log("Sent:",testMessage);
    await producer.disconnect();
    res.send({
        isSuccess : true
    });
})

app.listen(PORT, () => console.log(`server has started on ${PORT}`))