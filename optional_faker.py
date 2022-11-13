"""The `optional_faker` sources."""
from __future__ import annotations

import typing as t
from collections.abc import Callable as CallableRuntimeType

import faker.config
from faker.generator import Generator
from faker.providers import BaseProvider
from faker.providers.python import Provider as PythonProvider

if t.TYPE_CHECKING:
    import typing_extensions as te

    _ANY = t.TypeVar("_ANY", bound=t.Any)
    _P = te.ParamSpec("_P")


class Provider(BaseProvider):
    """Faker provider for optional values."""

    def __init__(self, generator: Generator) -> None:
        """Declare the other faker providers."""
        super().__init__(generator)
        self.__python = PythonProvider(generator)

    @t.overload
    def optional(self, value: _ANY, /) -> t.Optional[_ANY]:
        """Overload with value."""

    @t.overload
    def optional(self, callable: t.Callable[_P, _ANY], /, *args: _P.args, **kwargs: _P.kwargs) -> t.Optional[_ANY]:
        """Overload with callable."""

    def optional(
        self, value_or_callable: t.Callable[_P, _ANY], /, *args: _P.args, **kwargs: _P.kwargs
    ) -> t.Optional[_ANY]:
        """Takes value or callable, and returns the value or the result of the callable, or None.

        Args:
            value_or_callable: Value or callable to return, if `faker.pybool()` is True.
            args: Passed to callable.
            kwargs: Passed to callable.

        Returns:
            `value_or_callable` if value was passed, or callable result if `faker.pybool()` is True. Else - None.
        """
        if not self.__python.pybool():
            return None

        if isinstance(value_or_callable, CallableRuntimeType):  # type: ignore[arg-type] # false-positive
            return value_or_callable(*args, **kwargs)
        else:
            return value_or_callable  # type: ignore[return-value] # false-positive


faker.config.PROVIDERS.append("optional_faker")
