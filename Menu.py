import sqlite3

sqlite_file = '/Users/DarthVader/Desktop/SQL_Menu_Program/products.sqlite'
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()
table_name = "Products"
field_id = "Product_ID"
col1 = "Name"
col2 = "Description"
col3 = "Price"
col4 = "Quantity"
col5 = "Category"
col6 = "Supplier"


class db_menu:

    def create(self):

        c.execute('CREATE TABLE TABLE_NAME (field_id INTEGER PRIMARY KEY NULL, col1 TEXT, col2 TEXT,'
                  ' col3 DOUBLE, col4 INTEGER, col5 TEXT, col6 TEXT)')

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
            c.execute("INSERT INTO TABLE_NAME (col1, col2, col3, col4, col5 , col6) "
                      "VALUES (?, ?, ?, ?, ?, ?)", (product, description, price, quantity, category, supplier))
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
            c.execute('UPDATE TABLE_NAME SET col2=description, col3=price, col4=quantity, col5=category,'
                      ' col6=supplier WHERE col1=product')
        except sqlite3.Error:
            print("Error; invalid entry.")

        print("Update successful.")

        conn.commit()


    def delete(self):

        entry = input("Please enter product name to delete: ")

        try:
            c.execute('DELETE FROM TABLE_NAME WHERE col1=entry')


        except sqlite3.Error:
            print("Error; product not found.")

        print("Delete successful.")

        conn.commit()


    def display_all(self):

        c.execute('SELECT * FROM TABLE_NAME ')

        all_rows = c.fetchall()

        print('All Entries:\n' + all_rows.__str__())

        conn.commit()

    def show_entry(self):

        entry = input("Please enter product name to look up: ")

        try:
            c.execute('SELECT * FROM TABLE_NAME WHERE col1=entry')
            row = c.fetchall()
            print('Entry for ' + entry + ':\n' + row.__str__())

        except sqlite3.Error:
            print("Error; unknown product.")

        conn.commit()

    def delete_table(self):

        c.execute('DROP TABLE TABLE_NAME')

        print("Table Deleted. Please create new table.")

        conn.commit()

    def close_db(self):

        conn.close()
