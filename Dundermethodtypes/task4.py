class DatabaseConnection:
    def __enter__(self):
        print("Database Connected")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Database Closed")


with DatabaseConnection():
    print("Performing Query...")
