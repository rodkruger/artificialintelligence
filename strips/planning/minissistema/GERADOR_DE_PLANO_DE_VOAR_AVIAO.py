from planning.paip.gps import gps

### Edite esse arquivo e inclua a definição do problema
### Inclua aqui uma descrição textaul do domínio de
### aplicação

problem = {
    "init": ["baterias-ligadas"],

    "finish": ["aviao-limpo"],

    "ops": [

        {"action": "fechar-portas",
         "preconds": ["baterias-ligadas"],
         "add": ["portas-fechadas"],
         "delete": []
         },

        {"action": "ligar-instrumentos",
         "preconds": ["baterias-ligadas"],
         "add": ["instrumentos-ligados"],
         "delete": []
         },

        {"action": "ligar-motor",
         "preconds": ["instrumentos-ligados"],
         "add": ["motores-ligados"],
         "delete": []
         },

        {"action": "baixar-flaps",
         "preconds": ["motores-ligados"],
         "add": ["flaps-baixados"],
         "delete": []
         },

        {"action": "ligar-luzes",
         "preconds": ["instrumentos-ligados"],
         "add": ["luzes-ligadas"],
         "delete": []
         },

        {"action": "check-pre-voo",
         "preconds": ["luzes-ligadas"],
         "add": ["voo-checado"],
         "delete": []
         },

        {"action": "acelerar",
         "preconds": ["motores-ligados"],
         "add": ["acelerado"],
         "delete": []
         },

        {"action": "subir-2000-pes",
         "preconds": ["acelerado"],
         "add": ["aviao-em-voo"],
         "delete": []
         },

        {"action": "recolher-trem-pouso",
         "preconds": ["aviao-em-voo"],
         "add": ["aviao-limpo"],
         "delete": []
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
