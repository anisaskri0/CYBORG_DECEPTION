from CybORG import CybORG
from CybORG.Simulator.Scenarios import EnterpriseScenarioGenerator
from CybORG.Agents import SleepAgent, EnterpriseGreenAgent, FiniteStateRedAgent
from CybORG.Agents.Wrappers.TrueStateWrapper import TrueStateTableWrapper
from CybORG.Agents.Wrappers import BlueFlatWrapper
steps = 1000
sg = EnterpriseScenarioGenerator(blue_agent_class=SleepAgent, 
                                green_agent_class=EnterpriseGreenAgent, 
                                red_agent_class=FiniteStateRedAgent,
                                steps=steps)
cyborg = CybORG(scenario_generator=sg, seed=1234)
env = TrueStateTableWrapper(cyborg)
# Print host overview table
#env.print_host_overview_table()
#env.print_host_processes_tables()
env.print_agent_session_tables()
#print bluefatwrapper
env = BlueFlatWrapper(env=cyborg)
obs, _ = env.reset()


