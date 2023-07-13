---
title: Double floating-point precision loss issue
---

# Double float-point precision loss issue

In financial transactions and other domains, the precision loss issue is an important issue.

## Why does there be a loss of precision

I will explain it from a procedural point of view.z

This is `float` data construction in the C program:

```
Sign bit（1 bit） | Exponent（8 bits） | Fraction（23 bits）
```

There is an example that converts the float data structure to decimal.

```
0 10000010 10100000000000000000000
```

1. Sign bit: `0` is a representative negative number.
2. Exponent: the decimal number of `10000010` is `130`, and the result of the decimal exponent is `130 - 127`, equal to `3`.
3. Fraction: `10100000000000000000000`, it means `1.101000...`, convert it to decimal with `1*2^0 + 1*2^(-1) + 0*2^(-2) + 1*2^(-3) = 1 + 0.5 + 0 + 0.125`, equal to `1.625`.
4. So, the `float` represents `+2^3 * 1.625`, equal to `13`.

The same goes for `double`, there is the `double` data structure. 

```
Sign bit（1 bit） | Exponent（11 bits） | Fraction（52 bits）
```

