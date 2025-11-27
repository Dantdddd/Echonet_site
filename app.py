from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

database = []

@app.route("/forms", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        cidade = request.form["cidade"]
        bairro = request.form["bairro"]
        rua = request.form["rua"]
        mensagem = request.form["mensagem"]

        database.append({
            "cidade": cidade,
            "bairro": bairro,
            "rua": rua,
            "mensagem": mensagem
        })

        return redirect("/database")

    return render_template("form.html")

@app.route("/database")
def db():
    return render_template("database.html", entries=database)

@app.route("/")
def home():
    return redirect("/forms")

@app.route("/buscar", methods=["GET", "POST"])
def buscar():
    resultados = []

    if request.method == "POST":
        termo = request.form["termo"].lower()

        resultados = [
            entry for entry in database
            if termo in entry["cidade"].lower()
            or termo in entry["bairro"].lower()
            or termo in entry["rua"].lower()
        ]

    return render_template("buscar.html", resultados=resultados)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
