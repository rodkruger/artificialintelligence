from planning.paip.gps import gps

### Inclua abaixo a definição para o problema
### descrito no arquivo "Exercicio_gerador_de_plano_de_ensino.docx"

problem = {
    "init": ["1111",
             "2222",
             "3333",
             "4444"],
    "finish": ["9999"],
    "ops": [
        {"action": "aaaa",
         "preconds": ["1111"],
         "add": ["9999"], "delete": [""]},

        # [ .... ]

        {"action": "kkkk",
         "preconds": ["3333"],
         "add": ["8888"],
         "delete": ["4444"]
         }
    ]
}

def main():
    start = problem['init']
    finish = problem['finish']
    ops = problem['ops']
    msg="Você deve: "
    
    plan = gps(start, finish, ops, msg)
    if plan is not None:
        for action in plan:
            print (action)
    else:
        print('O plano não foi gerado')
        
if __name__ == '__main__':
    main()
