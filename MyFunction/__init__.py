import azure.functions
import flask

app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def index() -> str:
    return 'hello hello world'


@app.route('/MyFunction', methods=['GET'])
def myfunction() -> str:
    return 'hello hello world from myfunction'


# XXX: https://github.com/Azure/azure-functions-python-library/issues/71
hax_main = azure.functions.WsgiMiddleware(app).main


def main(
        req: azure.functions.HttpRequest,
        context: azure.functions.Context,
) -> azure.functions.HttpResponse:
    return hax_main(req, context)
