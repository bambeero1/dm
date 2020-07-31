import mysql.connector
from mysql.connector import Error
from wordpress_xmlrpc import Client,WordPressPost
from wordpress_xmlrpc.methods import posts



try:
    connection = mysql.connector.connect(host='localhost',
                                         database='datam',
                                         user='datam',
                                         password='######')

    sql_select_Query = "select title,body,tags,id from data LIMIT 100000"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    print("Total number of rows in datam is: ", cursor.rowcount)

    print("\nPrinting each laptop record")
    for row in records:
        client = Client('https://saudi.ml/xmlrpc.php', 'saudi', '######')
        title = row[0]
        body = row[1]
        tags = row[2].split(",")
        post = WordPressPost()
        post.terms_names = {
                'post_tag': tags,
                'category': tags,
                }
        post.title = title
        post.content = body
        post.id = client.call(posts.NewPost(post))

        post.post_status = 'publish'
        client.call(posts.EditPost(post.id, post))
        print("Titl = ", row[3], )

except Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if (connection.is_connected()):
        connection.close()
        cursor.close()
        print("MySQL connection is closed")
