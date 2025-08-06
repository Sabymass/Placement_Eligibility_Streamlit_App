import mysql.connector

def get_connection(config):
    return mysql.connector.connect(
        host=config["host"],
        user=config["user"],
        password=config["password"],
        database=config["database"],
        port=config.get("port", 4000),
        ssl_ca=r"D:\Sample final\Certs\isrgrootx1.pem"
    )
