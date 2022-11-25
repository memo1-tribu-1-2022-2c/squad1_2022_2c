from config import db

class ProductData():

    def __init__(self):
        self.table = 'products'
        self.cursor = db.cursor()

    def serialize_product(self, product) -> tuple:
        values = "(%s)"
        params = (product.name,)

        return values, params

    def store_new_product(self, product):
        if product.can_be_persisted():
            values, params = self.serialize_product(product)
            self.cursor.execute(f"INSERT INTO {self.table} VALUES{values}", params)
            [new_id] = self.cursor.fetchone()
            product.id = new_id
            db.commit()
        else:
            values, params = self.serialize_product(product)
            self.cursor.execute(f"INSERT INTO {self.table} (nombre) VALUES{values}", params)
            db.commit()
            self.cursor.execute("SELECT LASTVAL()")
            product.id = self.cursor.fetchone()[0]
            #raise Exception("Product has no versions associated")

        

    def update_product(self, product):
        pass

    def get_product_by_id(self, product_id: str) -> dict:
        query = f"SELECT * FROM {self.table} WHERE id=%s"
        
        params = (product_id, )
        self.cursor.execute(query, params)
        result = self.cursor.fetchone()
        if len(result) == 0:
            return None
        
        return {
            'id': result[0],
            'name': result[1]
        }

    def get_products_by_name(self, product_name: str) -> list:
        pass
