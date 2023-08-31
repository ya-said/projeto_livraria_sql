import psycopg2

class ConexaoFactory:
    def get_conexao(self):
        return psycopg2.connect(host='silly.db.elephantsql.com', database='hgotokee', 
                        user='hgotokee', password='Qxzm9T4ZJoOQQDkjQEIz7ncC8GSO4nvd')


