from config import db, connect_and_return, try_commit

class ProductData():

    def __init__(self):
        self.table = 'products'
        self.cursor = db.cursor()

    def serialize_product(self, product) -> tuple:
        values = "(%s)"
        params = (product.name,)

        return values, params

    def store_new_product(self, product):
        self.renew_cursor()
        if product.can_be_persisted():
            values, params = self.serialize_product(product)
            self.cursor.execute(f"INSERT INTO {self.table}(nombre) VALUES{values}", params)
            self.cursor.execute("SELECT LASTVAL()")
            [new_id] = self.cursor.fetchone()
            product.change_id(new_id)
            try_commit()
        else:
            raise Exception("Product has no versions associated")

        

    def update_product(self, product):
        self.renew_cursor()
        args = (product.name, product.id,)
        query = f"""UPDATE {self.table}
                    SET nombre=%s
                    WHERE id=%s
                """
        self.cursor.execute(query, args)
        try_commit()

    def get_product_by_id(self, product_id: str) -> dict:
        self.renew_cursor()
        query = f"SELECT * FROM {self.table} WHERE id=%s"
        
        params = (product_id, )
        self.cursor.execute(query, params)
        result = self.cursor.fetchone()
        try_commit()
        if not result:
            return None
        
        return {
            'id': result[0],
            'name': result[1]
        }

    def renew_cursor(self):
        if self.cursor.closed:
            data_base = connect_and_return()
            self.cursor = data_base.cursor()
