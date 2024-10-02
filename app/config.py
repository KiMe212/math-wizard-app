from functools import lru_cache

from pydantic import Field, NonNegativeInt, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

INTERVAL_ERROR_TEMPLATE = "Начальное значение `{}` не может быть больше конечного"


class UvicornSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="UVICORN_")

    host: str = "0.0.0.0"
    port: int = 8008
    log_level: str = "info"
    reload: bool = True


class Settings(BaseSettings):
    uvicorn: UvicornSettings = UvicornSettings()

    random_multiplier_range: tuple[int, int] = Field(
        default=(-10, 10),
        description="Диапазон чисел для случайного множителя",
    )

    random_delay_range: tuple[NonNegativeInt, NonNegativeInt] = Field(
        default=(0, 3),
        description="Диапазон времени задержки для выполнения задачи в секундах",
    )

    @staticmethod
    def _validate_range(range_: tuple[int, int]) -> bool:
        return range_[0] <= range_[1]

    @field_validator("random_multiplier_range", "random_delay_range")
    @classmethod
    def validate_ranges(cls, range_: tuple[int, int], info) -> tuple[int, int]:
        if not cls._validate_range(range_):
            raise ValueError(INTERVAL_ERROR_TEMPLATE.format(info.field_name))

        return range_


@lru_cache()
def get_settings() -> Settings:
    return Settings()


config: Settings = get_settings()
