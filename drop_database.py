from database_control import *

load_database("localhost","root","user",0)

log_on_level("Enter database name to drop:",0)
db_name = str(raw_input())

drop_database(db_name)
