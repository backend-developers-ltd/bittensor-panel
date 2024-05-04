from bittensor_panel.core.bt import load_hyperparams, update_remote_hyperparam
from bittensor_panel.core.models import HyperParameter


class HyperParameterUpdateFailed(Exception):
    pass


class HyperParameterSyncFailed(Exception):
    pass


def update_hyperparam(instance: HyperParameter) -> None:
    try:
        result = update_remote_hyperparam(instance.name, instance.value)
    except (SystemExit, Exception) as e:
        raise HyperParameterUpdateFailed(
            "Failed to update remote hyperparameter"
        ) from e
    if not result:
        raise HyperParameterUpdateFailed(
            "Failed to update remote hyperparameter. Subtensor returned False."
        )

    instance.save(update_fields=["value"])


def sync_hyperparams() -> None:
    try:
        hyperparam_dict = load_hyperparams()
    except (SystemExit, Exception) as e:
        raise HyperParameterSyncFailed("Failed to sync hyperparameters") from e

    if not hyperparam_dict:
        return

    objs: list[HyperParameter] = []

    for name, value in hyperparam_dict.items():
        objs.append(HyperParameter(name=name, value=value))

    HyperParameter.objects.bulk_create(
        objs, update_conflicts=True, update_fields=["value"], unique_fields=["name"]
    )
