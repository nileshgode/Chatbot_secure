#from guardrails import Guard, OnFailAction
#from guardrails.hub import ToxicLanguage

from app.input_guardrails import validate_input


# Initialize a guard that blocks toxic or inappropriate user input
guard = Guard().use(
    ToxicLanguage(threshold=0.5, validation_method="sentence", on_fail=OnFailAction.EXCEPTION)
)

def validate_input(user_input: str):
    """Raise Exception if input fails toxicity check."""
    guard.validate(user_input)
