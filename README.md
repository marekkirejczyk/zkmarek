# Elliptic curves

[![Lint and test](https://github.com/marekkirejczyk/elliptic_curves_video/actions/workflows/lint_and_test.yml/badge.svg)](https://github.com/marekkirejczyk/elliptic_curves_video/actions/workflows/lint_and_test.yml)

Educational implementation and Manim videos about elliptic curves cryptography.

## Test

Run all tests:

```sh
script/test
```

Run a single test:

```sh
script/test zkmarek.test.algo.test_sqrt.TestSqrt.test_tonelli_shanks_sqrt_none
```

## Manim animations
Generate and open movie:

```sh
script/movie
```

Generate and open single slide:
```sh
SLIDES=<slide_class_name> script/movie
```

Generate presentation:

```sh
script/presentation
```

Note: Movie related scripts are tested and work on OS X.

