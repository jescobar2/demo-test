from flask import Flask
import os
import pika

app = Flask(__name__)

@app.route('/')
def hello():
    host = os.uname()[1]
    # Configuración de la conexión a RabbitMQ
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(os.environ['RABBITMQ_HOST']))
        channel = connection.channel()

        # Declarar una cola
        channel.queue_declare(queue='mi_cola')

        # Mensaje que deseas enviar
        mensaje = "Hola, RabbitMQ! this is it"

        # Publicar el mensaje en la cola
        channel.basic_publish(exchange='', routing_key='mi_cola', body=mensaje)

        print(f"Mensaje enviado: '{mensaje}'")
        connection.close()
    except Exception as e:
        values_exp = str(e)
    # Cerrar la conexión
    return f"Hello, publisher fucking world!\nVersion: 1.0.0\nHostname: {host} and {os.environ['RABBITMQ_HOST']} and {values_exp}\n"

if __name__ == '__main__':
    port = os.environ.get('PORT', '8080')
    app.run(host='0.0.0.0', port=int(port))

