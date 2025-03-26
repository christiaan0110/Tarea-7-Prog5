Propósito de la funcion:
.El propósito de la función Lambda es gestionar y registrar préstamos de libros de manera eficiente en una base de datos (como DynamoDB). Esta función recibe información detallada de un préstamo (usuario, libro, fecha de préstamo y fecha de devolución), valida que los datos sean correctos y los almacenados.


Cómo ejecutarla y probarla localmente:
.Instalar dependencias: pip install boto3 moto.
.Ejecutar pruebas locales (ejemplo incluido).


Instrucciones básicas para desplegarla en Amazon Lambda:
.Subir el código a la consola de AWS Lambda.
.Configurar permisos de acceso ( roles IAM).
.Integrar con API Gateway para recibir solicitudes HTTP.
