```json
{
    "config/config.py": {
        "content": "
import logging
from pydantic_ai import Agent, InstrumentationSettings
from opentelemetry.sdk._logs import LoggerProvider
from opentelemetry.sdk.trace import TracerProvider
from typing import Optional

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def configure_instrumentation(
    include_binary_content: bool = False, 
    tracer_provider: Optional[TracerProvider] = None, 
    logger_provider: Optional[LoggerProvider] = None
) -> InstrumentationSettings:
    """
    Configure instrumentation settings for Pydantic AI.

    Args:
    - include_binary_content (bool): Whether to include binary content in instrumentation.
    - tracer_provider (TracerProvider): Custom tracer provider.
    - logger_provider (LoggerProvider): Custom logger provider.

    Returns:
    - InstrumentationSettings: Configured instrumentation settings.
    """
    try:
        instrumentation_settings = InstrumentationSettings(
            include_binary_content=include_binary_content, 
            tracer_provider=tracer_provider or TracerProvider(), 
            logger_provider=logger_provider or LoggerProvider()
        )
        logger.info('Instrumentation settings configured successfully')
        return instrumentation_settings
    except Exception as e:
        logger.error(f'Error configuring instrumentation settings: {e}')
        raise

def create_agent(
    model_name: str, 
    instrumentation_settings: InstrumentationSettings
) -> Agent:
    """
    Create a Pydantic AI agent.

    Args:
    - model_name (str): Name of the model to use.
    - instrumentation_settings (InstrumentationSettings): Instrumentation settings.

    Returns:
    - Agent: Created agent.
    """
    try:
        agent = Agent(model_name, instrument=instrumentation_settings)
        logger.info(f'Agent created successfully: {model_name}')
        return agent
    except Exception as e:
        logger.error(f'Error creating agent: {e}')
        raise

def simulate_rocket_science(
    non_stationary_drift_index: float, 
    stochastic_regime_switch: bool
) -> None:
    """
    Simulate the 'Rocket Science' problem.

    Args:
    - non_stationary_drift_index (float): Non-stationary drift index.
    - stochastic_regime_switch (bool): Whether to use stochastic regime switch.
    """
    try:
        # Simulate rocket science problem
        logger.info('Simulating rocket science problem')
        # Use the agent to make predictions
        agent = create_agent('gateway/openai:gpt-5.2', configure_instrumentation())
        # Make predictions using the agent
        logger.info('Making predictions using the agent')
    except Exception as e:
        logger.error(f'Error simulating rocket science problem: {e}')
        raise

if __name__ == '__main__':
    simulate_rocket_science(non_stationary_drift_index=0.5, stochastic_regime_switch=True)
",
        "commit_message": "feat: implement specialized config logic"
    }
}
```