import psycopg2


if __name__ == '__main__':
    conexao = psycopg2.connect(host='silly.db.elephantsql.com', database='hgotokee', 
                     user='hgotokee', password='Qxzm9T4ZJoOQQDkjQEIz7ncC8GSO4nvd')
    print('Conectou!')
    conexao.close()
