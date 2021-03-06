#!/usr/bin/env python

# Python client recommended by the RabbitMQ team
import pika
import sys

# Distributing tasks among workers

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()
channel.exchange_declare(exchange="topic_logs", exchange_type="topic")

message = ' '.join(sys.argv[2:]) or 'Hello World!'
severity = sys.argv[1] if len(sys.argv) > 1 else 'anonymous.info'

channel.basic_publish(exchange='topic_logs',
                      routing_key=severity,
                      body=message)
print(" [x] Sent %r:%r" % (severity, message))
connection.close()
