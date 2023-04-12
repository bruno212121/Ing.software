import os
from main import create_app, db
from main.models import OrderModel, SucursalModel, ShipModel, ArticlesOrderModel

# import logging
# logging.basicConfig()
# logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)


app = create_app()

app.app_context().push()

if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    app.run(host = '0.0.0.0', debug = True, port = 7000)