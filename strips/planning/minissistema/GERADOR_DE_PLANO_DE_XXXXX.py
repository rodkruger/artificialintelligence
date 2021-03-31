from planning.paip.gps import gps

### Edite esse arquivo e inclua a definição do problema
### Inclua aqui uma descrição textaul do domínio de
### aplicação

problem = {
    "init": ["aaa",
             "bbb",
             "ccc"],
    "finish": ["oooo"],
    "ops": [
        {"action": "XXXXX",
         "preconds": ["WWWWW"],
         "add": ["AAAAAA"], "delete": [""]
         },

        # [....]

        {"action": "yyyyy",
         "preconds": ["tttttt"],
         "add": ["qqqqqq"],
         "delete": ["yyyyyy"]
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
