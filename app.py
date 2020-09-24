import azure.functions
import flask

app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def index() -> str:
    return 'hello hello world'


azure_main = azure.functions.WsgiMiddleware(app).main


def main() -> int:
    app.run(port=8001)
    return 0


if __name__ == '__main__':
    exit(main())
