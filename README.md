# ZkMarek

[![Lint and test](https://github.com/marekkirejczyk/elliptic_curves_video/actions/workflows/lint_and_test.yml/badge.svg)](https://github.com/marekkirejczyk/elliptic_curves_video/actions/workflows/lint_and_test.yml)

ZkMarek is an educational project created by [ethmarek](https://twitter.com/ethmarek), as an exercise to learn cryptography, with focus on understanding [Plonk](https://vitalik.ca/general/2019/09/22/plonk.html).


ZkMarek consists of two sub projects in two respective folders:
* zkmarek/crypto - educational implementation of basic cryptographic primitives,
* zkmarek/video - source of videos created in Manim, used to create presentations and educational videos.

The code is tested and written in a reasonably readable manner, therefore it should serve well as an educational material. It should be easier to learn cryptographic algorithms than to form production libraries code.

### Warning ⚠️

Implementation here is focused on learning algorithms, rather than building actual production-ready solution. In particular, it is not optimized for security and performance. It is not audited, nor there is a plan to be audited in the future. Do not use it to build actual applications. Use it at your own responsibility.

## Contributing

### Test

Run all tests:

```sh
script/test
```

Run a single test:

```sh
script/test zkmarek.test.algo.test_sqrt.TestSqrt.test_tonelli_shanks_sqrt_none
```

### Manim animations
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

