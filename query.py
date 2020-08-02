 #Python Packages used : SQLAlchemy , Pandas
 #WorkFlow-
 # Import packages - Create database engine - connect to the engine - query the database - save query as dataframe  - close connection
 
 # First method
 from sqlalchemy import create_engine
 import pandas as pd
 engine = create_engine(" ---SQlFileName.sql_extension----")
 con = engine.connect()
 rs = con.exceute("---------SQLQuery------")
 #can be (fetchmany(size= )) also
 df = pd.DataFram(rs.fetchall())      
 con.close()
 
 
 
 #Second method -  Context manager
 from sqlalchemy import create_engine
 import pandas as pd
 engine = create_engine(" ---SQlFileName.sql_extension----")
 with engine.connect as con:
       rs= con.execute("-------SQLQuery----")
       df=pd.DataFrame(rs.fetchall())
       df.columns=rs.keys()
       
       
 #Third method
 from sqlalchemy import create_engine
 import pandas as pd
 engine = create_engine(" ---SQlFileName.sql_extension----")
 df = pd.read_sql_query("------SQLQuery----", engine)
