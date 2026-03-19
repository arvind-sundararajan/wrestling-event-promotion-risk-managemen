```json
{
    "utils/pydantic_logfire_utils.py": {
        "content": "
import logging
from pydantic_ai import Agent, InstrumentationSettings
from opentelemetry.sdk._logs import LoggerProvider
from opentelemetry.sdk.trace import TracerProvider
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from typing import Dict, List

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def configure_instrumentation(
    tracer_provider: TracerProvider, 
    logger_provider: LoggerProvider
) -> InstrumentationSettings:
    """
    Configure instrumentation settings for Pydantic AI.

    Args:
    - tracer_provider (TracerProvider): Tracer provider for OpenTelemetry.
    - logger_provider (LoggerProvider): Logger provider for OpenTelemetry.

    Returns:
    - InstrumentationSettings: Instrumentation settings for Pydantic AI.
    """
    try:
        instrumentation_settings = InstrumentationSettings(
            tracer_provider=tracer_provider, 
            logger_provider=logger_provider
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
    - instrumentation_settings (InstrumentationSettings): Instrumentation settings for Pydantic AI.

    Returns:
    - Agent: Pydantic AI agent.
    """
    try:
        agent = Agent(model_name, instrument=instrumentation_settings)
        logger.info(f'Agent created successfully for model {model_name}')
        return agent
    except Exception as e:
        logger.error(f'Error creating agent: {e}')
        raise

def classify_text(
    agent: Agent, 
    text: str
) -> Dict[str, float]:
    """
    Classify text using a Pydantic AI agent.

    Args:
    - agent (Agent): Pydantic AI agent.
    - text (str): Text to classify.

    Returns:
    - Dict[str, float]: Classification results.
    """
    try:
        # Load pre-trained model and tokenizer
        model = AutoModelForSequenceClassification.from_pretrained('distilbert-base-uncased')
        tokenizer = AutoTokenizer.from_pretrained('distilbert-base-uncased')

        # Preprocess text
        inputs = tokenizer(text, return_tensors='pt')

        # Classify text
        outputs = model(**inputs)
        logits = outputs.logits
        classification_results = {
            'non_stationary_drift_index': logits[:, 0].item(),
            'stochastic_regime_switch': logits[:, 1].item()
        }
        logger.info(f'Text classified successfully: {classification_results}')
        return classification_results
    except Exception as e:
        logger.error(f'Error classifying text: {e}')
        raise

if __name__ == '__main__':
    # Create tracer and logger providers
    tracer_provider = TracerProvider()
    logger_provider = LoggerProvider()

    # Configure instrumentation settings
    instrumentation_settings = configure_instrumentation(tracer_provider, logger_provider)

    # Create agent
    agent = create_agent('gateway/openai:gpt-5.2', instrumentation_settings)

    # Classify text
    text = 'This is a sample text to classify'
    classification_results = classify_text(agent, text)
    print(classification_results)
",
        "commit_message": "feat: implement specialized pydantic_logfire_utils logic"
    }
}
```