"""Tests provider from `optional_faker.py`."""
from faker import Faker
from pytest_mock import MockerFixture


class TestOptionalFaker:
    """Tests for `optional_faker.Provider` class."""

    def test_returns_value(self, faker: Faker, mocker: MockerFixture) -> None:
        """Tests, that call with value and `faker.pybool` that returns True gives a value, that we provided."""
        mocker.patch("faker.providers.python.Provider.pybool", lambda *_, **__: True)

        unique = object()
        assert faker.none_or(unique) is unique

    def test_calls_callable(self, faker: Faker, mocker: MockerFixture) -> None:
        """Tests, that provider calls callable with correct arguments."""
        mocker.patch("faker.providers.python.Provider.pybool", lambda *_, **__: True)

        stub = mocker.stub()
        args, kwargs = faker.pytuple(), faker.pydict()
        faker.none_or(stub, *args, **kwargs)

        stub.assert_called_once_with(*args, **kwargs)

    def test_doesnt_call_callable(self, faker: Faker, mocker: MockerFixture) -> None:
        """Tests, that provider doesn't call callable, if `faker.pybool` was False."""
        mocker.patch("faker.providers.python.Provider.pybool", lambda *_, **__: False)

        stub = mocker.stub()
        faker.none_or(stub)

        stub.assert_not_called()

    def test_returns_none(self, faker: Faker, mocker: MockerFixture) -> None:
        """Tests, that provider returns None if `faker.pybool` was False."""
        mocker.patch("faker.providers.python.Provider.pybool", lambda *_, **__: False)

        assert faker.none_or(object()) is None

    def test_returns_none_with_callable(self, faker: Faker, mocker: MockerFixture) -> None:
        """Tests, that provider returns None if `faker.pybool` was False, instead of calling callable."""
        mocker.patch("faker.providers.python.Provider.pybool", lambda *_, **__: False)

        assert faker.none_or(object) is None

    def test_seed_in_readme_is_right(self) -> None:
        fake = Faker()
        Faker.seed(1555)
        assert fake.none_or(fake.pystr()) is not None
        assert fake.none_or(fake.pystr()) is None
        assert fake.none_or(fake.pystr, 1, max_chars=10) is not None
        assert fake.none_or(fake.pystr, 1, max_chars=10) is None
        assert fake.none_or(lambda: "my callable!") == "my callable!"
        assert fake.none_or(lambda: "my callable!") is None
