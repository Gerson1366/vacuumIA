'''
Created on Jul 31, 2019

@author: assis
'''
from agents import TrivialVacuumEnvironment, compare_agents
from agents import RandomVacuumAgent, ReflexVacuumAgent, ModelBasedVacuumAgent, TraceAgent
    
"""agentRandom = RandomVacuumAgent()
agentRandom = TraceAgent(agentRandom)
environment = TrivialVacuumEnvironment()
environment.add_thing(agentRandom)
print(environment.status)
environment.run(20)
print(environment.status)"""

reflexMoves = 0;

agentReflex = ReflexVacuumAgent()
agentReflex = TraceAgent(agentReflex)
environment = TrivialVacuumEnvironment()
environment.add_thing(agentReflex)
print(environment.status)
environment.run(20)
print(environment.status)
moves = environment.return_moves()
reflexMoves += moves
print("Moves Reflex 1: "+str(moves))

agentReflex = ReflexVacuumAgent()
agentReflex = TraceAgent(agentReflex)
environment = TrivialVacuumEnvironment()
environment.add_thing(agentReflex)
print(environment.status)
environment.run(20)
print(environment.status)
moves = environment.return_moves()
reflexMoves += moves
print("Moves Reflex 2: "+str(moves))

agentReflex = ReflexVacuumAgent()
agentReflex = TraceAgent(agentReflex)
environment = TrivialVacuumEnvironment()
environment.add_thing(agentReflex)
print(environment.status)
environment.run(20)
print(environment.status)
moves = environment.return_moves()
reflexMoves += moves
print("Moves Reflex 3: "+str(moves))

agentReflex = ReflexVacuumAgent()
agentReflex = TraceAgent(agentReflex)
environment = TrivialVacuumEnvironment()
environment.add_thing(agentReflex)
print(environment.status)
environment.run(20)
print(environment.status)
moves = environment.return_moves()
reflexMoves += moves
print("Moves Reflex 4: "+str(moves))
print("Moves Reflex Total: "+str(reflexMoves))

modelMoves = 0;

agentModel = ModelBasedVacuumAgent()
agentModel = TraceAgent(agentModel)
environment = TrivialVacuumEnvironment()
environment.add_thing(agentModel)
print(environment.status)
environment.run()
print(environment.status)
moves = environment.return_moves()
modelMoves += moves
print("Moves Model 1: "+str(moves))

agentModel = ModelBasedVacuumAgent()
agentModel = TraceAgent(agentModel)
environment = TrivialVacuumEnvironment()
environment.add_thing(agentModel)
print(environment.status)
environment.run()
print(environment.status)
moves = environment.return_moves()
modelMoves += moves
print("Moves Model 2: "+str(moves))

agentModel = ModelBasedVacuumAgent()
agentModel = TraceAgent(agentModel)
environment = TrivialVacuumEnvironment()
environment.add_thing(agentModel)
print(environment.status)
environment.run()
print(environment.status)
moves = environment.return_moves()
modelMoves += moves
print("Moves Model 3: "+str(moves))

agentModel = ModelBasedVacuumAgent()
agentModel = TraceAgent(agentModel)
environment = TrivialVacuumEnvironment()
environment.add_thing(agentModel)
print(environment.status)
environment.run()
print(environment.status)
moves = environment.return_moves()
modelMoves += moves
print("Moves Model 4: "+str(moves))
print("Moves Model Total: "+str(modelMoves))

print("Media Reflex: "+str(reflexMoves/4))
print("Media Model: "+str(modelMoves/4))
