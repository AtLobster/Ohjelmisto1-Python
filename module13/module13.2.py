from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='k1ssa',
    database='flight_game',
    collation = 'utf8mb4_unicode_ci',
)

@app.route('/kenttä/<icao>')
def hae_lentokentan_tiedot(icao):
    cursor = conn.cursor()

    sql = "SELECT ident, name, municipality FROM airport WHERE ident = %s"
    cursor.execute(sql, (icao,))
    tulos = cursor.fetchone()

    cursor.close()
    conn.close()

    if tulos:
        vastaus = {
            "ICAO": tulos[0],
            "Name": tulos[1],
            "Municipality": tulos[2]
        }
        return jsonify(vastaus)



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000)
