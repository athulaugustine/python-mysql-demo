from flask import Flask, request
import mysql.connector
import jsonify
app = Flask(__name__)

def connect_db():
    mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="mydatabase"
    )

    return mydb

def insert_table(mydb,name,address):
    mycursor = mydb.cursor()
    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    val = ("John", "Highway 21")
    mycursor.execute(sql, val)
    mydb.commit()

@app.route("/update",methods=["PUT"])
def update_table():
    try:
        data = request.form
        db = connect_db()
        status = insert_table(db,data['name'],data['address'])
        return jsonify({"status":status})

    except:
        return jsonify({"status":"error inserting data"})






