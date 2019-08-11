'''
Created on Jul 31, 2019

@author: assis
'''
from agents import TrivialVacuumEnvironment, compare_agents
from agents import RandomVacuumAgent, ReflexVacuumAgent, ModelBasedVacuumAgent, TraceAgent

print()
print(" Executando os 4 ambientes com o Agent Reflex")
print()

"Inicia variavel para contar movimentos de Reflex"
reflexMoves = 0;

print("Ambiente 1 - Agent Reflex")
print()
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
print()

"Realiza as mesmas acoes do primeiro Reflex para cada combinacao de ambiente"
print("Ambiente 2 - Agent Reflex")
print()
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
print()

print("Ambiente 3 - Agent Reflex")
print()
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
print()

print("Ambiente 4 - Agent Reflex")
print()
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
print()


print()
print(" Executando os mesmos ambientes agora com o Agent Model")
print()

"Realiza os mesmos movimentos de Reflex para Model"
modelMoves = 0;

print("Ambiente 1 - Agent Model")
print()
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
print()

print("Ambiente 2 - Agent Model")
print()
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
print()

print("Ambiente 3 - Agent Model")
print()
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
print()

print("Ambiente 4 - Agent Model")
print()
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
print()


print("Desempenho")
print()
print("Total")
print()
print("Moves Reflex Total: "+str(reflexMoves))
print("Moves Model Total: "+str(modelMoves))
print()
print("Media")
print()
print("Media Reflex: "+str(reflexMoves/4))
print("Media Model: "+str(modelMoves/4))
