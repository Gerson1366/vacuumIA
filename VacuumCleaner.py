'''
Created on Jul 31, 2019

@author: assis
'''
from agents import TrivialVacuumEnvironment, compare_agents
from agents import RandomVacuumAgent, ReflexVacuumAgent, ModelBasedVacuumAgent, TraceAgent

"Inicia variavel para contar movimentos de Reflex"
reflexMoves = 0;

"Inicia Reflex, determina estado do ambiente executa 10 vezes"
agentReflex = ReflexVacuumAgent()
agentReflex = TraceAgent(agentReflex)
environment = TrivialVacuumEnvironment()
"Define estado do ambiente"
environment.setPlaces("Clean", "Clean")
"Joga agente no ambiente"
environment.add_thing(agentReflex)
print(environment.status)
"Roda ambiente"
environment.run(10)
print(environment.status)
"Pega numero de movimentos ateh ter ficado limpo"
moves = environment.return_moves()
"Soma movimentos com contador"
reflexMoves += moves
print("Moves Reflex 1: "+str(moves))

"Realiza as mesmas acoes do primeiro Reflex para cada combinacao de ambiente"
agentReflex = ReflexVacuumAgent()
agentReflex = TraceAgent(agentReflex)
environment = TrivialVacuumEnvironment()
environment.setPlaces("Clean", "Dirty")
environment.add_thing(agentReflex)
print(environment.status)
environment.run(10)
print(environment.status)
moves = environment.return_moves()
reflexMoves += moves
print("Moves Reflex 2: "+str(moves))

agentReflex = ReflexVacuumAgent()
agentReflex = TraceAgent(agentReflex)
environment = TrivialVacuumEnvironment()
environment.setPlaces("Dirty", "Dirty")
environment.add_thing(agentReflex)
print(environment.status)
environment.run(10)
print(environment.status)
moves = environment.return_moves()
reflexMoves += moves
print("Moves Reflex 3: "+str(moves))

agentReflex = ReflexVacuumAgent()
agentReflex = TraceAgent(agentReflex)
environment = TrivialVacuumEnvironment()
environment.setPlaces("Dirty", "Clean")
environment.add_thing(agentReflex)
print(environment.status)
environment.run(10)
print(environment.status)
moves = environment.return_moves()
reflexMoves += moves
print("Moves Reflex 4: "+str(moves))
print("Moves Reflex Total: "+str(reflexMoves))

"Realiza os mesmos movimentos de Reflex para Model"
modelMoves = 0;

agentModel = ModelBasedVacuumAgent()
agentModel = TraceAgent(agentModel)
environment = TrivialVacuumEnvironment()
environment.setPlaces("Clean", "Clean")
environment.add_thing(agentModel)
print(environment.status)
environment.run(10)
print(environment.status)
moves = environment.return_moves()
modelMoves += moves
print("Moves Model 1: "+str(moves))

agentModel = ModelBasedVacuumAgent()
agentModel = TraceAgent(agentModel)
environment = TrivialVacuumEnvironment()
environment.setPlaces("Clean", "Dirty")
environment.add_thing(agentModel)
print(environment.status)
environment.run(10)
print(environment.status)
moves = environment.return_moves()
modelMoves += moves
print("Moves Model 2: "+str(moves))

agentModel = ModelBasedVacuumAgent()
agentModel = TraceAgent(agentModel)
environment = TrivialVacuumEnvironment()
environment.setPlaces("Dirty", "Dirty")
environment.add_thing(agentModel)
print(environment.status)
environment.run(10)
print(environment.status)
moves = environment.return_moves()
modelMoves += moves
print("Moves Model 3: "+str(moves))

agentModel = ModelBasedVacuumAgent()
agentModel = TraceAgent(agentModel)
environment = TrivialVacuumEnvironment()
environment.setPlaces("Dirty", "Clean")
environment.add_thing(agentModel)
print(environment.status)
environment.run(10)
print(environment.status)
moves = environment.return_moves()
modelMoves += moves
print("Moves Model 4: "+str(moves))
print("Moves Model Total: "+str(modelMoves))

print("Media Reflex: "+str(reflexMoves/4))
print("Media Model: "+str(modelMoves/4))
