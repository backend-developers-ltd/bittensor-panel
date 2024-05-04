from dataclasses import asdict

import bittensor
from django.conf import settings


def get_subtensor() -> bittensor.subtensor:
    return bittensor.subtensor(settings.SUBTENSOR_ADDRESS)


def get_wallet() -> bittensor.wallet:
    return bittensor.wallet(
        name=settings.WALLET_NAME,
        hotkey=settings.WALLET_HOTKEY,
        path=settings.WALLET_PATH,
    )


def load_hyperparams() -> dict[str, int] | None:
    st = get_subtensor()

    hyperparams = st.get_subnet_hyperparameters(settings.SUBNET_UID)

    if not hyperparams:
        return None

    return asdict(hyperparams)


def update_remote_hyperparam(name: str, value: int) -> bool:
    st = get_subtensor()
    wallet = get_wallet()

    return st.set_hyperparameter(
        wallet=wallet,
        netuid=settings.SUBNET_UID,
        parameter=name,
        value=value,
        wait_for_inclusion=False,
        wait_for_finalization=True,
        prompt=False,
    )
