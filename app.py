from flask import Flask
import os
import pika
import json
import os
import pydash as _
from typing import Callable
from concurrent import futures
from google.cloud import pubsub_v1

# app = Flask(__name__)

# @app.route('/')
# def hello():
#     host = os.uname()[1]
    # Configuración de la conexión a RabbitMQ
    # try:
    #     connection = pika.BlockingConnection(pika.ConnectionParameters(os.environ['RABBITMQ_HOST']))
    #     channel = connection.channel()

    #     # Declarar una cola
    #     channel.queue_declare(queue='mi_cola')

    #     # Mensaje que deseas enviar
    #     mensaje = "Hola, RabbitMQ! this is it"

    #     # Publicar el mensaje en la cola
    #     channel.basic_publish(exchange='', routing_key='mi_cola', body=mensaje)

    #     print(f"Mensaje enviado: '{mensaje}'")
    #     connection.close()
    # except Exception as e:
    #     values_exp = str(e)
    # Cerrar la conexión
    # a = "si publico"
    # try:
    #     message = {"dataFormat": "JSON_API_V1", 
    #             "eventType": "SECRET_ROTATE", 
    #             "secretId": "solictando traslado a operador x",
    #             "project_id": "hazel-champion-399821"}

    #     project_id = "hazel-champion-399821"
    #     topic_id = "traslado-operador"
    #     publisher = pubsub_v1.PublisherClient()
    #     topic_path = publisher.topic_path(project_id, topic_id)

    #     data = json.dumps(message)
    #     # When you publish a message, the client returns a future.
    #     publish_future = publisher.publish(topic_path, data.encode("utf-8"))
    #     # Non-blocking. Publish failures are handled in the callback function.
    #     print(f"publish message: {publish_future.result()}")
    #     publish_future.add_done_callback(get_callback(publish_future, data))
    #     publish_futures = publish_future

    #     # Wait for all the publish futures to resolve before exiting.
    #     futures.wait(publish_futures, return_when=futures.ALL_COMPLETED)
   
    #     print(f"Published messages with error handler to {topic_path}.")
    # except Exception as e:
    #     a = "no publico"

#    return f"Hello, publisher fucking world!\nVersion: 1.0.0\nHostname: {host} and {os.environ['RABBITMQ_HOST']}\n"

# if __name__ == '__main__':
#     port = os.environ.get('PORT', '8080')
#     app.run(host='0.0.0.0', port=int(port))


# def main():
#     """Continuously pull messages from subsciption"""
#     def get_callback(
#         publish_future: pubsub_v1.publisher.futures.Future, data: str
#     ) -> Callable[[pubsub_v1.publisher.futures.Future], None]:
#         def callback(publish_future: pubsub_v1.publisher.futures.Future) -> None:
#             try:
#                 # Wait 60 seconds for the publish call to succeed.
#                 print(publish_future.result(timeout=60))
#             except futures.TimeoutError:
#                 print(f"Publishing {data} timed out.")

#         return callback

#     try:
#         message = {"dataFormat": "JSON_API_V1", 
#                 "eventType": "SECRET_ROTATE", 
#                 "secretId": "solictando traslado a operador xxx",
#                 "project_id": "hazel-champion-399821"}

#         project_id = "hazel-champion-399821"
#         topic_id = "traslado-operador"
#         publisher = pubsub_v1.PublisherClient()
#         topic_path = publisher.topic_path(project_id, topic_id)

#         data = json.dumps(message)
#         # When you publish a message, the client returns a future.
#         publish_future = publisher.publish(topic_path, data.encode("utf-8"))
#         # Non-blocking. Publish failures are handled in the callback function.
#         print(f"publish message: {publish_future.result()}")
#         publish_future.add_done_callback(get_callback(publish_future, data))
#         publish_futures = publish_future

#         # Wait for all the publish futures to resolve before exiting.
#         futures.wait(publish_futures, return_when=futures.ALL_COMPLETED)
   
#         print(f"Published messages with error handler to {topic_path}.")
#     except Exception as e:
#         raise Exception(str(e))


# if __name__ == '__main__':
#     main()

import json
from flask import Flask, request

app = Flask(__name__)

# Configuración de Google Cloud Pub/Sub
from google.cloud import pubsub_v1

# def get_callback(
#     publish_future: pubsub_v1.publisher.futures.Future, data: str
# ):
#     def callback(publish_future: pubsub_v1.publisher.futures.Future):
#         try:
#             print(publish_future.result(timeout=60))
#         except futures.TimeoutError:
#             print(f"Publishing {data} timed out.")

#     return callback

@app.route('/')
def publish_message():
    try:
        project_id = "hazel-champion-399821"
        topic_id = "traslado-operador"
        publisher = pubsub_v1.PublisherClient()
        topic_path = publisher.topic_path(project_id, topic_id)
        message = {"dataFormat": "JSON_API_V1", 
                "eventType": "SECRET_ROTATE", 
                "secretId": "solictando traslado a operador z",
                "project_id": "hazel-champion-399821"}
        # message_data = request.get_json()
        data = json.dumps(message)

        # Publicar el mensaje en Google Cloud Pub/Sub
        publisher.publish(topic_path, data.encode("utf-8"))
        # print(f"Published message: {publish_future.result()}")

        # publish_future.add_done_callback(get_callback(publish_future, data))
        # publish_futures = publish_future

        # Wait for all the publish futures to resolve before exiting.
        # futures.wait(publish_futures, return_when=futures.ALL_COMPLETED)
   
        print(f"Published messages with error handler to {topic_path}.")
        return "Message published successfully!", 200
    except Exception as e:
        return str(e), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)


# from flask import Flask, request, jsonify, make_response
# import requests, json


# app = Flask(__name__)

# @app.route('/v1/trasladar_ciudadano', methods=['DELETE'])
# def delete_record():
#     try:
#         data = request.get_json()

#         delete_url = "https://govcarpeta-76300fb42a5a.herokuapp.com/api-docs/#/default/delete_apis_unregisterCitizen"
#         response = requests.delete(delete_url, json=data)
#         print(response.status_code)
#         if response.status_code == 200:
#             print(response.content)
#             message = {"id": data["id"],"operatorId": data["operatorId"], "operatorName": data["operatorName"]}
#             response_content = response.content.decode('utf-8')
#             data = json.dumps(data)
#             return jsonify({'status_code': response.status_code, 'content': response_content, 'message': 'Ciudadano trasladado con exito', 'data':data}), 200
#         else:
#             return jsonify({'Error': "Error deleting record"}), response.status_code

#     except Exception as e:
#         app.logger.error("Error Request: %s", str(e))
#         return jsonify ({"Error": "Error Request"})


# @app.errorhandler(500)
# def internal_server_error(error):
#     return make_response(jsonify({"message": "Failed: Application Error.."}), 500)

# @app.errorhandler(501)
# def not_implemented(error):
#     return make_response(jsonify({"message": "Failed: Wrong Parameters.."}), 501)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8080)