from sqlalchemy import create_engine,select,insert,update,delete


import os
from db_models.list_nodes import create_all,ListNode


class DBService():
    
    def __init__(self):
        """
        We are going to check for the existence of the file, and if it does not exist we will create one
        """
        if not os.path.isfile("list_db.sql"):
            self.engine = create_engine("sqlite:///list_nodes.db")
            create_all(self.engine)
        else:
            self.engine = create_engine("sqlite:///list_nodes.db")
    def filter_data(self,data):
        with self.engine.connect() as session:
            stmt = select(ListNode)
            breakpoint
            stmt = stmt.where(ListNode.text.like(f"{data}%"))  
            rs = session.execute(stmt)
            return [{"id":row[0],"desc":row[1]} for row in rs.fetchall()]     
    def read_data(self):
        with self.engine.connect() as session:
            stmt = select(ListNode)
            rs = session.execute(stmt)
            return [{"id":row[0],"desc":row[1]} for row in rs.fetchall()]
        
    def delete_item(self,id):
        with self.engine.connect() as session:
            stmt = delete(ListNode).where(ListNode.id == id)
            session.execute(stmt)
            session.commit()
    def update_item(self,id,value):
        with self.engine.connect() as session:
            stmt = update(ListNode).where(ListNode.id == id).values(desc=value)
            session.execute(stmt)
            session.commit()        
                 
    def new_item(self,value):
        with self.engine.connect() as session:
            stmt = insert(ListNode).values(desc=value)
            result = session.execute(stmt)
            session.commit()
            return result.inserted_primary_key[0]