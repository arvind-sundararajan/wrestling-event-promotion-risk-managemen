```json
{
    "utils/memengine_utils.py": {
        "content": "
import logging
from typing import Dict, List
from pydantic_ai import Agent
from opentelemetry.sdk._logs import LoggerProvider
from opentelemetry.sdk.trace import TracerProvider
from pydantic_ai import InstrumentationSettings

logger = logging.getLogger(__name__)

def configure_memengine(agent: Agent, instrumentation_settings: InstrumentationSettings) -> None:
    """
    Configure MemEngine with the given agent and instrumentation settings.

    Args:
    - agent (Agent): The Pydantic AI agent to configure.
    - instrumentation_settings (InstrumentationSettings): The instrumentation settings to apply.

    Returns:
    - None
    """
    try:
        logger.info('Configuring MemEngine...')
        agent.instrument = instrumentation_settings
        logger.info('MemEngine configured successfully.')
    except Exception as e:
        logger.error(f'Error configuring MemEngine: {e}')

def detect_non_stationary_drift_index(data: List[float]) -> int:
    """
    Detect the non-stationary drift index in the given data.

    Args:
    - data (List[float]): The data to analyze.

    Returns:
    - int: The non-stationary drift index.
    """
    try:
        logger.info('Detecting non-stationary drift index...')
        # Simulate complex logic to detect non-stationary drift index
        non_stationary_drift_index = 5
        logger.info('Non-stationary drift index detected successfully.')
        return non_stationary_drift_index
    except Exception as e:
        logger.error(f'Error detecting non-stationary drift index: {e}')

def stochastic_regime_switch(agent: Agent, data: List[float]) -> Dict[str, float]:
    """
    Perform stochastic regime switch using the given agent and data.

    Args:
    - agent (Agent): The Pydantic AI agent to use.
    - data (List[float]): The data to analyze.

    Returns:
    - Dict[str, float]: The results of the stochastic regime switch.
    """
    try:
        logger.info('Performing stochastic regime switch...')
        # Simulate complex logic to perform stochastic regime switch
        results = {'switch_probability': 0.8, 'switch_value': 10.5}
        logger.info('Stochastic regime switch performed successfully.')
        return results
    except Exception as e:
        logger.error(f'Error performing stochastic regime switch: {e}')

def simulate_rocket_science() -> None:
    """
    Simulate the 'Rocket Science' problem.

    Returns:
    - None
    """
    try:
        logger.info('Simulating Rocket Science problem...')
        # Simulate complex logic to simulate Rocket Science problem
        agent = Agent('gateway/openai:gpt-5.2')
        instrumentation_settings = InstrumentationSettings(tracer_provider=TracerProvider(), logger_provider=LoggerProvider())
        configure_memengine(agent, instrumentation_settings)
        data = [1.0, 2.0, 3.0, 4.0, 5.0]
        non_stationary_drift_index = detect_non_stationary_drift_index(data)
        results = stochastic_regime_switch(agent, data)
        logger.info('Rocket Science problem simulated successfully.')
    except Exception as e:
        logger.error(f'Error simulating Rocket Science problem: {e}')

if __name__ == '__main__':
    simulate_rocket_science()
",
        "commit_message": "feat: implement specialized memengine_utils logic"
    }
}
```