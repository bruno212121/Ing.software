import os
from main import create_app, db
from main.models import ArticleModel, CategoryModel

# import logging
# logging.basicConfig()
# logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)


app = create_app()

app.app_context().push()

@app.route('/healthcheck', methods=['GET'])
def health_check():
    # Verificar aquí la salud de tu aplicación
    # Puedes agregar lógica adicional, como verificar conexiones a la base de datos u otros servicios

    # Devolver código de estado 200 si la aplicación está saludable
    return 'App working correctly', 200

if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    app.run(host = '0.0.0.0', debug = True, port = 7000)