class Config:
    SECRET_KEY = '9f91cea27eebcb6b4d224192fe96696d'

class DevelopmentConfig(Config):
    DEBUG=True
    MYSQL_HOST = 'localhost'
    MYSQL_PORT = 3307 
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = '' 
    MYSQL_DB = 'flask login'
    
    

config={
    'development':DevelopmentConfig
}

config['EXPLAIN_TEMPLATE_LOADING'] = True #ojo lo agrege 21/09/22 para tratar de resolver el problema del hosting 