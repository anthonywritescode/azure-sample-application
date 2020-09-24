import azure.functions

from app import app

main = azure.functions.WsgiMiddleware(app).main
