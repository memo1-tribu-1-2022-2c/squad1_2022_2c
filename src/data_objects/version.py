from config import db

class VersionData():

    def __init__(self):
        self.table='versions'
        self.cursor = db.cursor()

    def store_new_version(self, version):
        args = (version.number, version.state, version.product,)
        query = f"INSERT INTO {self.table} (numero, estado, producto) VALUES(%s, %s, %s)"
        self.cursor.execute(query, args)
        db.commit()
        self.cursor.execute("SELECT LASTVAL()")
        version.id = self.cursor.fetchone()[0]
    

    def retrieve_version_by_product(self, product_id) -> list:
        args = (product_id,)
        query = f"SELECT * FROM {self.table} WHERE producto=%s"
        self.cursor.execute(query, args)
        return self.cursor.fetchall()