import sqlite3
# all of my global variables
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

# database class


class db_menu:

    # create statement
    def create(self):

        c.execute('CREATE TABLE TABLE_NAME (field_id INTEGER PRIMARY KEY NULL, col1 TEXT, col2 TEXT,'
                  ' col3 DOUBLE, col4 INTEGER, col5 TEXT, col6 TEXT)')

        print("Table created.")
        conn.commit()

# add method
    def add(self):

        # local variables to be plugged into columns
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
    # update works similarly to add method

    def update(self):

        product = input("Product name to update: ")
        description = input("Enter short description: ")
        price = input("Price: ")
        quantity = input("Quantity: ")
        category = input("Category: ")
        supplier = input("Supplier: ")

        try:
            c.execute('UPDATE TABLE_NAME SET col2=?, col3=?, col4=?, col5=?,'
                      ' col6=? WHERE col1=?'), (description, price, quantity, category, supplier, product)
        except sqlite3.Error:
            print("Error; invalid entry.")

        print("Update successful.")

        conn.commit()


    def delete(self):

        entry = input("Please enter product name to delete: ")

        try:
            c.execute('DELETE FROM TABLE_NAME WHERE  field_id =' + entry + '')


        except sqlite3.Error:
            print("Error; product not found.")

        print("Delete successful.")

        conn.commit()


    def display_all(self):

        c.execute('SELECT * FROM TABLE_NAME')

        all_rows = c.fetchall()

        for row in all_rows:
            print('[Product ID: %i ]\n'
                  '[Product Name: %s ]\n'
                  '[Description: %s ]\n'
                  '[Price: %f ]\n'
                  '[Quantity: %i ]\n'
                  '[Category: %s ]\n'
                  '[Supplier: %s ]\n' % row)

        conn.commit()

    def show_entry(self):

        entry = input("Please enter product Id to look up: ")

        query = 'SELECT * FROM TABLE_NAME WHERE field_id =' + entry + ''

        # try:
        c.execute(query)
        row = c.fetchone()

        print('[Product ID: %i ]\n'
              '[Product Name: %s ]\n'
              '[Description: %s ]\n'
              '[Price: %f ]\n'
              '[Quantity: %i ]\n'
              '[Category: %s ]\n'
              '[Supplier: %s ]\n' % row)

        #print(row)

        # except sqlite3.Error:
        #     print("Error; unknown product.")

        conn.commit()

    def delete_table(self):

        c.execute('DROP TABLE TABLE_NAME')

        print("Table Deleted. Please create new table.")

        conn.commit()

    def close_db(self):

        conn.close()
