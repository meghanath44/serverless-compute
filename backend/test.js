const { Kafka } = require('kafkajs');

// Kafka broker connection
const kafka = new Kafka({
  clientId: 'my-producer',
  brokers: ['192.168.1.253:9092'] // replace with your Kafka broker(s)
});

const producer = kafka.producer();

const run = async () => {
  // Connect the producer
  await producer.connect();
  
  // Send a message
  await producer.send({
    topic: 'main', // replace with your topic
    messages: [
      { key: 'key1', value: 'Hello Kafka from Node.js!' },
    ],
  });

  console.log("Message sent successfully");

  // Disconnect the producer
  await producer.disconnect();
};

run().catch(console.error);
