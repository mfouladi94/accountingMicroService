import pika, json, os, django , sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

django.setup()

from accountingmicroservice.wallet.models import Wallet

QUEUE_NAME = "registration_queue"
RABBIT = "rabbit"
RABBIT_local = "localhost"

# Establish connection to RabbitMQ server

connection = pika.BlockingConnection(pika.ConnectionParameters('rabbit'))
channel = connection.channel()
channel.queue_declare(queue=QUEUE_NAME)


# Define a callback function to process incoming messages
def callback(ch, method, properties, body):
    print(f"Received message: {body}")
    wallet, _ = Wallet.objects.get_or_create(userId=int(body))


# Consume messages from the queue
channel.basic_consume(queue=QUEUE_NAME, on_message_callback=callback, auto_ack=True)

print('Waiting for messages. To exit press CTRL+C')

# Start consuming messages
channel.start_consuming()
