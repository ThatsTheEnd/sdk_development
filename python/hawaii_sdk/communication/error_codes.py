from enum import IntEnum


class RCIError(IntEnum):
    """
    Enum representing command interface errors generated by the ICL.

    Attributes:
        UNKNOWN_CMD (int): Error code for an unknown command.
        PARAM_COUNT (int): Error code for an incorrect parameter count.
        PARAM_VALUE (int): Error code for an invalid parameter value.
        COM (int): General communication error code.
        FATAL_ERROR_COM (int): Fatal communication error code.
    """

    UNKNOWN_CMD: int = -501
    PARAM_COUNT: int = -502
    PARAM_VALUE: int = -503
    COM: int = -1
    FATAL_ERROR_COM: int = -1
