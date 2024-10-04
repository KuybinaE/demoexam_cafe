from peewee import*

connect = MySQLDatabase(
'KujE1234_dem_cafe',
    user = 'KujE1234_admCafe',
    password = '111111',
    host = '10.11.13.118',
    port = 3306
)
if __name__ == "__main__":
    connect.connect()