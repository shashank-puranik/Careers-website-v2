from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://m4hx3iar2eu4jsc4oz8a:pscale_pw_lWEMOwGP2kKCmgQN2xc19JkAsy9fawJITyFS3nJYDGx@aws.connect.psdb.cloud/shashank_test?charset=utf8mb4"

engine = create_engine(db_connection_string,
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
})

with engine.connect() as conn:
  result = conn.execute(text("SELECT * FROM jobs"))

dict =[]
for row in result:
    row_as_dict = dict.append(row._mapping)

print(dict[0])

