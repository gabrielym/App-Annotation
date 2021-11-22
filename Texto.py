import sqlite3
conn = sqlite3.connect('notas.db')
# definindo um cursor
cursor = conn.cursor()

# criando a tabela (schema)
class Notas():
    def __init__(self, texto):
        self.texto = texto

    def inserir(self):
        conn = sqlite3.connect("notas.db")
        C = conn.cursor()
        C.execute("INSERT INTO notas "
                  "values(\'{}\',\'{}\',{},{}, {}, {}, \'{}\')".format(self.nome,
                                                self.descricao, self.preco, self.desconto,
                                                 self.qtde,self.cateCod, self.codigo))
        conn.commit()
        conn.close()


# desconectando...
conn.close()