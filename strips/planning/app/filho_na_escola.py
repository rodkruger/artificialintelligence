from planning.paip.gps import gps

problem = {
	"init": ["filho-esta-em-casa", "carro-necessita-de-nova-bateria",
			 "possui-dinheiro", "possui-lista-telefonica"],
	"finish": ["filho-no-colegio"],
	"ops": [
	{
		"action": "levar-filho-ao-colegio",
		"preconds": ["filho-esta-em-casa", "carro-esta-em-bom-funcionamento"],
		"add": ["filho-no-colegio"],
		"delete": ["filho-esta-em-casa"]
	},
	{
		"action": "efetuar-a-instalacao-da-bateria-na-oficina",
		"preconds": ["carro-necessita-de-nova-bateria",
					 "oficina-instala-nova-bateria",
					 "oficina-recebe-o-dinheiro-do-servico"],
		"add": ["carro-esta-em-bom-funcionamento"],
		"delete": [""]
	},
	{
		"action": "informar-problema-ao-mecanico",
		"preconds": ["em-comunicacao-com-a-oficina"],
		"add": ["oficina-instala-nova-bateria"],
		"delete": [""]
	},
	{
		"action": "telefonar-para-a-oficina",
		"preconds": ["conhece-o-numero-telefone-de-uma-oficina"],
		"add": ["em-comunicacao-com-a-oficina"],
		"delete": [""]
	},
	{
		"action": "procurar-numero-de-telefone-de-uma-oficina",
		"preconds": ["possui-lista-telefonica"],
		"add": ["conhece-o-numero-telefone-de-uma-oficina"],
		"delete": [""]
	},
	{
		"action": "passar-dinheiro-para-o-caixa-da-oficina",
		"preconds": ["possui-dinheiro"],
		"add": ["oficina-recebe-o-dinheiro-do-servico"],
		"delete": ["possui-dinheiro"]
	}
	]
}

def main():
    start = problem['init']
    finish = problem['finish']
    ops = problem['ops']
    msg = 'Deve-se executar: '
    plan = gps(start, finish, ops, msg)
    if plan is not None:
        for action in plan:
            print (action)
    else:
        print('O plano não foi gerado')

if __name__ == '__main__':
    main()
