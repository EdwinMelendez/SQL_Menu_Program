import sqlite3

sqlite_file = '/Users/DarthVader/Desktop/SQL_Menu_Program/products.sqlite'
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()
table = "Products"
field_id = "Product_ID"
col1 = "Name"
col2 = "Description"
col3 = "Price"
col4 = "Quantity"
col5 = "Category"
col6 = "Supplier"


class db_menu:

    def create(self):

        c.execute('CREATE TABLE {tn} ({f0} INTEGER PRIMARY KEY, {f1} TEXT, {f2} TEXT, {f3} DOUBLE, {f4} INTEGER, {f5} TEXT, {f6} TEXT)'
                  .format(tn=table, f0=field_id, f1=col1, f2=col2, f3=col3, f4=col4, f5=col5, f6=col6))

        print("Table created.")
        conn.commit()


    def add(self):

        product = input("Product name: ")
        description = input("Enter short description: ")
        price = input("Price: ")
        quantity = input("Quantity: ")
        category = input("Category: ")
        supplier = input("Supplier: ")

        try:
            c.execute("INSERT OR IGNORE INTO {tn} ({c1}, {c2}, {c3}, {c4}, {c5} , {c6}) "
                      "VALUES ({f1}, {f2}, {f3}, {f4}, {f5}, {f6})"
                      .format(tn=table, c0=field_id, c1=col1, c2=col2, c3=col3, c4=col4, c5=col5, c6=col6,
                              f1=product, f2=description, f3=price, f4=quantity, f5=category, f6=supplier))

        except sqlite3.IntegrityError:
            print("Error with primary key")
        except sqlite3.Error:
            print("Error; invalid entry")

        print("Entry successful.")

        conn.commit()


    def update(self):

        product = input("Product name to update: ")
        description = input("Enter short description: ")
        price = input("Price: ")
        quantity = input("Quantity: ")
        category = input("Category: ")
        supplier = input("Supplier: ")

        try:
            c.execute('UPDATE {tn} SET ({f2}={c2}}, {f3}={c3}, {f4}={c4}, {f5}={c5}, {f6}={c6}) WHERE {f1}={c1}'
                      .format(tn=table, f1=col1, f2=col2, c2=description, f3=col3, c3=price,
                              f4=col4, c4=quantity, f5=col5,
                              c5=category, c6=supplier,  f6=col6, c1=product))
        except sqlite3.Error:
            print("Error; invalid entry.")

        print("Update successful.")

        conn.commit()


    def delete(self):

        entry = input("Please enter product name to delete: ")

        try:
            c.execute('DELETE * FROM {tn} WHERE {cn}={e}'
                      .format(tn=table, cn=col1, e=entry))

        except sqlite3.Error:
            print("Error; product not found.")

        print("Delete successful.")

        conn.commit()


    def display_all(self):

        c.execute('SELECT * FROM {tn}'.format(tn=table))

        all_rows = c.fetchall()

        print('All Entries:\n' + all_rows.__str__())

        conn.commit()

    def show_entry(self):

        entry = input("Please enter product name to look up: ")

        try:
            c.execute('SELECT * FROM {tn} WHERE {cn}={e}'
                      .format(tn=table, cn=col1, e=entry))
            row = c.fetchall()
            print('Entry for ' + entry + ':\n' + row.__str__())

        except sqlite3.Error:
            print("Error; unknown product.")

        conn.commit()

    def delete_table(self):

        c.execute('DROP TABLE {tn}'.format(tn=table))

        print("Table Deleted. Please create new table.")

        conn.commit()

    def close_db(self):

        conn.close()
