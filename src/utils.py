import os
from typing import Dict
import random
from dotenv import load_dotenv
import numpy as np
import torch


def initialize_env():
    """
    does what it says on the tin.
    """
    load_dotenv()


def load_env_var(variable_name: str) -> str:
    """
    Loads a single environment variable.

    Raises:
        Exception: If the environment variable does not exist.
    """
    if variable_name not in os.environ:
        raise KeyError(f"{variable_name} does not exist in os.environ")
    return os.environ[variable_name]


def load_env_vars(*args: str) -> Dict[str, str]:
    """
    Loads multiple environment variables.
    """
    return {arg: load_env_var(arg) for arg in args}


def set_seed(seed: int) -> None:
    """
    Set random seeds for reproducibility.
    """
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
