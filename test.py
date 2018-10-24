import database_control as dbc

print "Set log level:"
lvl = input()


dbc.load_database("localhost","root","user",lvl)

db_name = "test_base"
tb_name = "test"

dbc.add_attribute(["ime",dbc.var_char(20),"NOT NULL","PRIMARY KEY"])


dbc.add_user(dbc.User(["Tilen K."]))

dbc.create(db_name,tb_name)

dbc.DB.close()
