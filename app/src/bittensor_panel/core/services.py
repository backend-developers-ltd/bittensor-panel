from bittensor_panel.core.bt import update_remote_hyperparam
from bittensor_panel.core.models import HyperParameter


class HyperParameterUpdateFailed(Exception):
    pass


def update_hyperparam(instance: HyperParameter):
    try:
        result = update_remote_hyperparam(instance.name, instance.value)
    except Exception as e:
        raise HyperParameterUpdateFailed(
            "Failed to update remote hyperparameter"
        ) from e
    if not result:
        raise HyperParameterUpdateFailed(
            "Failed to update remote hyperparameter. Subtensor returned False."
        )

    instance.save(update_fields=["value"])
