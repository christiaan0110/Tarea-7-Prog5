import json
import uuid
import boto3
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('PrestamosLibros')


# Función Lambda
def lambda_handler(event, context):

    try:
        body = json.loads(event['body'])

        required_fields = ['usuario', 'libro', 'fecha_prestamo', 'fecha_devolucion']
        for field in required_fields:
            if field not in body:
                return {
                    'statusCode': 400,
                    'body': json.dumps({'error': f'Campo {field} es obligatorio'})
                }

        try:
            datetime.strptime(body['fecha_prestamo'], '%Y-%m-%d')
            datetime.strptime(body['fecha_devolucion'], '%Y-%m-%d')
        except ValueError:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Las fechas deben tener el formato YYYY-MM-DD'})
            }

        prestamo_id = str(uuid.uuid4())

        table.put_item(
            Item={
                'prestamo_id': prestamo_id,
                'usuario': body['usuario'],
                'libro': body['libro'],
                'fecha_prestamo': body['fecha_prestamo'],
                'fecha_devolucion': body['fecha_devolucion']
            }
        )

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Préstamo registrado exitosamente', 'prestamo_id': prestamo_id})
        }

    except Exception as e:

        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }