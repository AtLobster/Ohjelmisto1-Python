from flask import Flask, Response
import json

app = Flask(__name__)

def isPrime(numero):

    if numero < 2:
        return False

    if numero == 2:
        return True

    if numero % 2 == 0:
        return False

    for i in range(3, int(numero ** 0.5) + 1, 2):
        if numero % i == 0:
            return False

    return True


@app.route('/alkuluku/<luku>')
def alkuluku(luku):

    number = int(luku)
    vastaus = {
        "Number": number,
        "isPrime": isPrime(number)
    }
    tilakoodi = 200


    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=tilakoodi, mimetype="application/json")



if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)