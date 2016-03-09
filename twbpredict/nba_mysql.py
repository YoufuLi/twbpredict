import mysql.connector
cnx = mysql.connector.connect(user='root', host='127.0.0.1', database='twb')
cursor = cnx.cursor()

def GetConnectedNodes(uid):
    query_nodes = ("SELECT followee_uid FROM user_sns WHERE follower_uid = %s"%(uid))
    cursor.execute(query_nodes)
    conNodes = [str(item[0]) for item in cursor.fetchall()]
    return conNodes

def GetConnectedItems(uid):
    conNodes = GetConnectedNodes(uid)
    count=0
    for node in conNodes:
        query_items=("SELECT EXISTS(SELECT item_id FROM item WHERE item_id =%s)"%(node))
        cursor.execute(query_items)
        print cursor.fetchall()
    #return conNodes