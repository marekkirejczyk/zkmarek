# ZkMarek

[![Lint and test](https://github.com/marekkirejczyk/elliptic_curves_video/actions/workflows/lint_and_test.yml/badge.svg)](https://github.com/marekkirejczyk/elliptic_curves_video/actions/workflows/lint_and_test.yml)

zkMarek is an educational project created by [zkMarek](https://twitter.com/zkmarek), as an exercise to learn cryptography, with focus on understanding [Plonk](https://vitalik.ca/general/2019/09/22/plonk.html).


ZkMarek consists of two sub projects in two respective folders:
* `zkmarek/crypto` - educational implementation of basic cryptographic primitives,
* `zkmarek/video` - source of videos created in Manim, used to create presentations and educational videos.

The code is tested and written in a reasonably readable manner, therefore it should serve well as an educational material. It should be easier to learn cryptographic algorithms than to form production libraries code.

### ⚠️ Warning

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

Generate and open movie for specific deck:
```sh
DECK=TEASER script/movie
DECK=E1 script/movie
DECK=E2 script/movie
```

Default is E1 (Episode 1).

Generate and open movie from specific slides:
```sh
SLIDES=<slide_class_name> script/movie
SLIDES=<index_of_slide> script/movie
SLIDES=<list,of,indexes,and,class_names> script/movie
```

Generate and open movie from specific slides of specific deck:
```sh
DECK=TEASER SLIDES=1 script/movie
```


Generate presentation:

```sh
script/presentation
```

Note: Movie related scripts are tested and work on OS X.

### Command line interface

There is a useful calc script, which allows to perform miscellaneous calculations like finding all subgroups of an elliptic curve. Run with -h options to see the syntax.

```sh
script/calc -h
```

### Music license

Thannoid - Bodytonic

License: #2601

Date: 08/01/2023

app.sessions.blue

