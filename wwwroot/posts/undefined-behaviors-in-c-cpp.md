---
id: detecting-undefined-behaviors-in-c-cpp
title: Detecting undefined behaviors in C/C++
abstract: 
created: 2024-07-07
tags: draft, c, c++, static analysis
---
# Detecting undefined behaviors in C/C++

## What do we mean by undefined behavior?
[Undefined behavior (UB)](https://en.m.wikipedia.org/wiki/Undefined_behavior) refers to code whose behavior is unpredictable according to the language specification. When a program executes an operation that has an undefined behavior, the language specification does not specify what should happen. It could lead the program to crash, produce incorrect results, lose/corrupt data, or behave differently depending on the compiler and environment being used. They can lead to security vulnerabilities, which can then be exploited to execute malicious code and gain privileges.

### Examples
Undefined behavior can be triggered in many ways, but the ones below are some of the most common ones in C/C++.

#### Dereferencing a null pointer
Dereferencing a null pointer will cause the program to crash.
```
int* ptr = nullptr;
int value = *ptr; // UB
```

#### Out-of-bounds reads and write
Accessing out-of-bounds memory can cause segmentation faults or corrupt memory.
```
int array[5] = { 1, 2, 3, 4, 5 };
array[5] = 32; // UB
```

#### Integer overflow
```
int x = INT_MAX;
int y = x + 1; // UB
```
Some compilers may assign `INT_MAX` to `y`, while others may wraparound and return `-INT_MAX`.

#### Uninitialized variables
```
int x;
printf("%d", x); // UB: The memory of x is uninitialized, so it contains a random value.
```

