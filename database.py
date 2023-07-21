from sqlalchemy import create_engine, text


db_connection_string = "mysql+pymysql://a0hd7f0zzz6edz09m2nd:pscale_pw_bwPoDYn6lma8mMNRYeW5fN7IRvBrhZGZjtr1nZrgVmy@aws.connect.psdb.cloud/trackninja?charset=utf8mb4"


ssl_args = {
  "ssl": {
    "ca":
    "/etc/ssl/cert.pem",  
    "check_hostname":
    True  
  }
}

engine = create_engine(db_connection_string, connect_args=ssl_args)

with engine.connect() as conn:
  result = conn.execute(text("select * from jobs"))
  print(result.all())
