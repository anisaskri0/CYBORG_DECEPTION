from CybORG import CybORG
from CybORG.Simulator.Actions.AbstractActions import Impact
from CybORG.Simulator.Actions.Action import InvalidAction
from CybORG.Simulator.Scenarios import EnterpriseScenarioGenerator
from CybORG.Agents import FiniteStateRedAgent
# Set up the scenario
steps = 100
scenario_generator = EnterpriseScenarioGenerator(
    red_agent_class=FiniteStateRedAgent,  # Red agent class
    steps=steps
)
cyborg = CybORG(scenario_generator=scenario_generator, seed=1234)

# Initialize the red agent
red_agent_name = 'red_agent_0'
red_agent = FiniteStateRedAgent()

# Reset the environment
results = cyborg.reset()

# Red agent takes an action
for step in range(3):  # Simulate 3 steps
    from rich import print

    # Get the current observation and action space for the red agent
    obs = results.observation
    action_space = cyborg.get_action_space(red_agent_name)

    # Red agent decides on an action
    action = red_agent.get_action(obs, action_space)

    # Execute the action in the environment
    results = cyborg.step(agent=red_agent_name, action=action)

    # Print the results of the action
    print(f"Step {step + 1}:")
    print(f"Action Taken: {action}")
    print(f"Observation: {results.observation}")
    print(f"Reward: {results.reward}")
    print(f"Done: {results.done}")
    print("-" * 30)


