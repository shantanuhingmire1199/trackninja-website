from sqlalchemy import create_engine, text

# Update your database connection string with the ssl_ca parameter pointing to the path of the CA certificate file.
db_connection_string = "mysql+pymysql://a0hd7f0zzz6edz09m2nd:pscale_pw_bwPoDYn6lma8mMNRYeW5fN7IRvBrhZGZjtr1nZrgVmy@aws.connect.psdb.cloud/trackninja?charset=utf8mb4"

# Set up SSL options
ssl_args = {
  "ssl": {
    "ca":
    "/etc/ssl/cert.pem",  # Replace with the actual path to your CA certificate file
    "check_hostname":
    True  # Set to False if you don't need hostname verification
  }
}

# Create the engine with the ssl_args
engine = create_engine(db_connection_string, connect_args=ssl_args)

with engine.connect() as conn:
  result = conn.execute(text("select * from jobs"))
  print(result.all())
