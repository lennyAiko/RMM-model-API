import connexion

app = connexion.App(__name__, specification_dir="./")
app.add_api("swagger.yml")

@app.route('/')
def endpoints():
    data = []
    return data

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000, debug=True)