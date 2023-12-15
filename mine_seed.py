"""It is a script, which looks for a seed we can use in our README example."""
import optional_faker
from faker import Faker
import itertools


def main() -> None:
    for seed in itertools.count():
        fake = Faker()
        Faker.seed(seed)
        if (
            fake.none_or(fake.pystr()) is not None
            and fake.none_or(fake.pystr()) is None
            and fake.none_or(fake.pystr, 1, max_chars=10) is not None
            and fake.none_or(fake.pystr, 1, max_chars=10) is None
            and fake.none_or(lambda: "my callable!") is not None
            and fake.none_or(lambda: "my callable!") is None
        ):
            print(seed)


if __name__ == "__main__":
    main()
