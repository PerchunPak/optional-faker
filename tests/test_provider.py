"""Tests provider from `optional_faker.py`."""
from faker import Faker
from pytest_mock import MockFixture


class TestOptionalFaker:
    """Tests for `optional_faker.Provider` class."""

    def test_returns_value(self, faker: Faker, mocker: MockFixture) -> None:
        """Tests, that call with value and `faker.pybool` that returns True gives a value, that we provided."""
        mocker.patch("faker.providers.python.Provider.pybool", lambda *_, **__: True)

        unique = object()
        assert faker.optional(unique) is unique

    def test_calls_callable(self, faker: Faker, mocker: MockFixture) -> None:
        """Tests, that provider calls callable with correct arguments."""
        mocker.patch("faker.providers.python.Provider.pybool", lambda *_, **__: True)

        stub = mocker.stub()
        args, kwargs = faker.pytuple(), faker.pydict()
        faker.optional(stub, *args, **kwargs)

        stub.assert_called_once_with(*args, **kwargs)

    def test_doesnt_call_callable(self, faker: Faker, mocker: MockFixture) -> None:
        """Tests, that provider doesn't call callable, if `faker.pybool` was False."""
        mocker.patch("faker.providers.python.Provider.pybool", lambda *_, **__: False)

        stub = mocker.stub()
        faker.optional(stub)

        stub.assert_not_called()

    def test_returns_none(self, faker: Faker, mocker: MockFixture) -> None:
        """Tests, that provider returns None if `faker.pybool` was False."""
        mocker.patch("faker.providers.python.Provider.pybool", lambda *_, **__: False)

        assert faker.optional(object()) is None

    def test_returns_none_with_callable(self, faker: Faker, mocker: MockFixture) -> None:
        """Tests, that provider returns None if `faker.pybool` was False, instead of calling callable."""
        mocker.patch("faker.providers.python.Provider.pybool", lambda *_, **__: False)

        assert faker.optional(object) is None
