from config import db, connect_and_return, try_commit, rollback

class VersionData():

    def __init__(self):
        self.table='versions'
        self.cursor = db.cursor()

    def store_new_version(self, version):
        self.renew_cursor()
        args = (version.number, version.state, version.product,)
        query = f"INSERT INTO {self.table} (numero, estado, producto) VALUES(%s, %s, %s)"
        try:

            self.cursor.execute(query, args)
        except:
            rollback()
            raise Exception("Could not store new version")

        try_commit()
        self.cursor.execute("SELECT LASTVAL()")
        version.id = self.cursor.fetchone()[0]
    

    def retrieve_version_by_product(self, product_id) -> list:
        self.renew_cursor()
        args = (product_id,)
        query = f"SELECT * FROM {self.table} WHERE producto=%s"
        try:

            self.cursor.execute(query, args)
        except:
            rollback()
            raise Exception("Could not find product")

        try_commit()
        return self.cursor.fetchall()

    def retrieve_version_by_id(self, version_id: int):
        self.renew_cursor()
        args = (version_id,)
        query = f"SELECT * FROM {self.table} WHERE id=%s"
        try:

            self.cursor.execute(query, args)
        except:
            rollback()
            raise Exception(f"Could not find version: {version_id}")

        try_commit()
        return self.cursor.fetchone()

    def retrieve_all_by_id(self, version_ids: list):

        return [self.retrieve_version_by_id(version_id) for version_id in version_ids]

    def update_version(self, version):
        self.renew_cursor()
        args = (version.number, version.state,version.id)
        query = f"""
                UPDATE {self.table}
                SET numero=%s, estado=%s
                WHERE id=%s
                """
        try:

            self.cursor.execute(query, args)
        except:
            rollback()
            raise Exception(f"Could not update version: {version.id}")
        try_commit()

    def renew_cursor(self):
        if self.cursor.closed:
            data_base = connect_and_return()
            self.cursor = data_base.cursor()