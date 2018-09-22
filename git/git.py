import commands
import json
config = {}
try:
	with open("git.json", 'r') as config_file:
		config = json.load(config_file)
	print(config)
except:
	config = {}
a = commands.getoutput("grep url */.git/config | grep https").split()
sal = {}
i = 0
cont = 0
for input in config:
	i = i + 1
for b in a:
	if b == "url":
		print("")
	else:
		if b != "=":
			qwe = 0
			for aux in config:
				#print("config", config[aux])
				if config[aux] == b:
					qwe = 1
					#print("encontrado")
				if config[aux] == b:
					break
			if qwe == 0:
				cont = cont + 1
				config[i + cont] = b
				print(b)
				print("Nuevo repositorio")
i = 0
for s in config:
	sal[i] = config[s]
	i = i + 1
if cont > 0:
	with open('git.json', 'w') as f:
		json.dump(sal, f, indent=2)

