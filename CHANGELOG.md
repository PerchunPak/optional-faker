# Changelog

We follow [Semantic Versions](https://semver.org/) style.


## Version 2.1.0

- Support Python 3.12 ([e650c775](https://github.com/PerchunPak/optional-faker/commit/e650c775d1258334f0cc545a1aa51549d3e63d70)).


## Version 2.0.0

- Rename our method to `none_or`, which means that you must use `faker.none_or` instead of `faker.optional`. This is because faker added a new proxy, `faker.optional`, which works similary to `faker.unique`, but makes callables optional. This is different approach and doesn't allow to pass values or custom callables, unlike ours. This is why this library isn't deprecated. ([613e719b](https://github.com/PerchunPak/optional-faker/commit/613e719ba87bc22035415e8fffd2f018920fe82e))


## Version 1.0.0-post.2

- Include 'optional-faker' import line in README example. ([#3](https://github.com/PerchunPak/optional-faker/pull/3))


## Version 1.0.0-post.1

- Added better seed in README example. ([93651d99](https://github.com/PerchunPak/optional-faker/commit/93651d99a6d9515f1022e99882f7dabb79a8e7b3))


## Version 1.0.0

Nothing changed.


## Version 0.1.1

- Don't limit `faker` version to `15.x.x`. ([464203e5](https://github.com/PerchunPak/optional-faker/commit/464203e5464e2ff085499802746572ef01eba9b3))


## Version 0.1.0

- Repository initialised.
