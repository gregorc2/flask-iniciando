from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)

todos = ['comprar', 'seleccionar', 'carrito']



@app.route("/")
def index():
    user_id = request.remote_addr
    response = make_response(redirect("/hello"))
    response.set_cookie("user_id", user_id)
    return response

@app.route("/hello")
def hello():
    user_id = request.cookies.get("user_id")
    contex = {
        'user_id' : user_id,
        'todos' : todos
    }
    return render_template("hello.html", **contex)


if __name__ == "__main__":
    app.run(port=8080,host='0.0.0.0', debug = True)
