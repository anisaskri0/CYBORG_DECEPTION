from CybORG import CybORG
from CybORG.Simulator.Scenarios import EnterpriseScenarioGenerator
from CybORG.Agents.SimpleAgents.LinearAgent import LinearAgent
from CybORG.Agents import EnterpriseGreenAgent, FiniteStateRedAgent
from CybORG.Agents.Wrappers.VisualiseRedExpansion import VisualiseRedExpansion
from CybORG.Agents.SimpleAgents.KeyboardAgent import KeyboardAgent
steps = 5
sg = EnterpriseScenarioGenerator(blue_agent_class=KeyboardAgent, 
                                green_agent_class=EnterpriseGreenAgent, 
                                red_agent_class=FiniteStateRedAgent,
                                steps=steps)
cyborg = CybORG(scenario_generator=sg, seed=7629)

visualise = VisualiseRedExpansion(cyborg, steps)
visualise.run()
