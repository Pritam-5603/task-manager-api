from database import engine

try:
    connection = engine.connect()

    print("Successfully connected to MySQL!")

    connection.close()

except Exception as error:
    print("Database connection failed!")
    print(error)