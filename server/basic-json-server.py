from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def get_users():
    users = [
        {
            "id": 1,
            "name": "Leanne Graham",
            "email": "lgraham@Romaguera.biz",
            "company_name": "Romaguera-Crona"
        },
        {
            "id": 2,
            "name": "Ervin Howell",
            "email": "ervin.howell@melissa.tv",
            "company_name": "Deckow-Crist"
        },
        {
            "id": 3,
            "name": "Clementine Bauch",
            "email": "cbauch@Romaguera.net",
            "company_name": "Romaguera-Jacobson"
        }
    ]
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)
