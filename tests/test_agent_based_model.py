```json
{
    "tests/test_agent_based_model.py": {
        "content": "
import logging
from pydantic_ai import Agent, InstrumentationSettings
from opentelemetry.sdk._logs import LoggerProvider
from opentelemetry.sdk.trace import TracerProvider
from typing import Dict, List

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def configure_instrumentation_settings(tracer_provider: TracerProvider, logger_provider: LoggerProvider) -> InstrumentationSettings:
    """
    Configure instrumentation settings for the agent.

    Args:
    - tracer_provider (TracerProvider): The tracer provider to use.
    - logger_provider (LoggerProvider): The logger provider to use.

    Returns:
    - InstrumentationSettings: The configured instrumentation settings.
    """
    try:
        instrumentation_settings = InstrumentationSettings(tracer_provider=tracer_provider, logger_provider=logger_provider)
        logger.info('Instrumentation settings configured successfully')
        return instrumentation_settings
    except Exception as e:
        logger.error(f'Error configuring instrumentation settings: {e}')
        raise

def create_agent(model_name: str, instrumentation_settings: InstrumentationSettings) -> Agent:
    """
    Create an agent with the given model name and instrumentation settings.

    Args:
    - model_name (str): The name of the model to use.
    - instrumentation_settings (InstrumentationSettings): The instrumentation settings to use.

    Returns:
    - Agent: The created agent.
    """
    try:
        agent = Agent(model_name, instrument=instrumentation_settings)
        logger.info(f'Agent created successfully with model name {model_name}')
        return agent
    except Exception as e:
        logger.error(f'Error creating agent: {e}')
        raise

def simulate_rocket_science_problem(agent: Agent, non_stationary_drift_index: float, stochastic_regime_switch: bool) -> Dict[str, List[float]]:
    """
    Simulate the rocket science problem using the given agent and parameters.

    Args:
    - agent (Agent): The agent to use.
    - non_stationary_drift_index (float): The non-stationary drift index to use.
    - stochastic_regime_switch (bool): Whether to use stochastic regime switch.

    Returns:
    - Dict[str, List[float]]: The results of the simulation.
    """
    try:
        # Simulate the rocket science problem
        results = agent.simulate(non_stationary_drift_index, stochastic_regime_switch)
        logger.info('Rocket science problem simulated successfully')
        return results
    except Exception as e:
        logger.error(f'Error simulating rocket science problem: {e}')
        raise

if __name__ == '__main__':
    # Configure instrumentation settings
    tracer_provider = TracerProvider()
    logger_provider = LoggerProvider()
    instrumentation_settings = configure_instrumentation_settings(tracer_provider, logger_provider)

    # Create an agent
    model_name = 'gateway/openai:gpt-5.2'
    agent = create_agent(model_name, instrumentation_settings)

    # Simulate the rocket science problem
    non_stationary_drift_index = 0.5
    stochastic_regime_switch = True
    results = simulate_rocket_science_problem(agent, non_stationary_drift_index, stochastic_regime_switch)

    # Print the results
    print(results)
",
        "commit_message": "feat: implement specialized test_agent_based_model logic"
    }
}
```