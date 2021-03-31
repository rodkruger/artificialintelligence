from planning.paip.gps import gps

problem = {
	"init": ["c-1", "c-4", "c-10", "c-9"],
    "finish": ["c-3"],
    "ops": [
	{ 	"action": "a-1",
		"preconds": ["c-1", "c-2"],
		"add": ["c-3"],
		"delete": ["c-1"]
	},
	{ 	"action": "a-2",
		"preconds": ["c-4", "c-5", "c-6"],
		"add": ["c-2"],
		"delete": [""]
	},
    { 	"action": "a-3",
		"preconds": ["c-7"],
		"add": ["c-5"],
		"delete": [""]
	},
    { 	"action": "a-4",
		"preconds": ["c-8"],
		"add": ["c-7"],
		"delete": [""]
	},
    { 	"action": "a-5",
		"preconds": ["c-9"],
		"add": ["c-8"],
		"delete": [""]
	},
    { 	"action": "a-6",
		"preconds": ["c-10"],
		"add": ["c-6"],
		"delete": ["c-10"]
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
