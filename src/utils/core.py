import os
from web3 import __version__ as web3_version
from chainutils.retry import async_retry


class SystemCompliance:
    @staticmethod
    def assert_version(required: str = "7.12.0") -> None:
        if web3_version != required:
            raise SystemError(f"CRITICAL: Web3 Version Mismatch. Require {required}, Found {web3_version}")

    @staticmethod
    def cleanse_terminal():
        os.system("cls" if os.name == "nt" else "clear")


def async_error_handler(retries: int = 3, delay: float = 1.0):
    """Retry decorator — thin wrapper around chainutils.async_retry with fixed delay."""
    return async_retry(
        max_attempts=retries,
        base_delay=delay,
        max_delay=delay,
        exponential_base=1.0,
        jitter=False,
    )
