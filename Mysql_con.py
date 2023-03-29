import mysql.connector

con = mysql.connector.connect(host="localhost", password="Thamizhanda04", user="root" , database = "Phonepe_pulse")

if con.is_connected():
    print("Success")
