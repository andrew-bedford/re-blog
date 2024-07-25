---
id: detecting-undefined-behaviors-in-c-cpp
title: Detecting undefined behaviors in C/C++
abstract: 
created: 2024-07-07
tags: draft, c, c++, static analysis
---
# Detecting undefined behaviors in C/C++
C and C++ are incredibly powerful programming languages, known for their efficiency and fine-grained control over system resources (e.g., memory). However, this power comes with a caveat: they make it easy to “shoot yourself in the foot”. This phrase highlights the potential pitfalls, such as undefined behaviors and subtle bugs, that can arise from improper memory management, pointer arithmetic, and other low-level operations. It is one of the reasons why the [NSA recommended](https://media.defense.gov/2022/Nov/10/2003112742/-1/-1/0/CSI_SOFTWARE_MEMORY_SAFETY.PDF) to avoid using those languages if possible and using modern languages instead (e.g., C#, Java, Rust).

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
array[10] = 32; // UB
```

#### Integer overflow
```
int x = INT_MAX;
int y = x + 1; // UB
```
Some compilers may assign `INT_MAX` to `y`, while others may wraparound and return `-INT_MAX`.

#### Uninitialized variables
This may come as a surprise for people coming from other languages, but C/C++ doesn't initialize built-ins variables to a default value (e.g., `0` for `int`). Instead, the value will be whatever value is stored in the address at the time of initialization, so it's basically random.
```
int x;
printf("%d", x); // UB: The memory of x is uninitialized, so it contains a random value.
```

# How to avoid undefined behaviors?
## Initialize variables
Always initialize variables, especially pointers, when you declare them. If you don’t have a valid address to assign, set them to `NULL` in C or `nullptr` in C++.
```
int x{};
int* ptr1 = NULL;    // C
int* ptr2 = nullptr; // C++
```

###### Check


Check Pointers Before Dereferencing: Before you dereference a pointer, always check if it is nullptr or NULL.

if (ptr != nullptr) {
    // Safe to dereference ptr
    *ptr = 10;
}

Use Smart Pointers: In C++, use smart pointers like std::unique_ptr or std::shared_ptr which automatically manage the memory and help avoid null pointer dereferences.

std::unique_ptr<int> ptr = std::make_unique<int>(10);
if (ptr) {
    // Safe to use ptr
    *ptr = 20;
}

Handle Memory Allocation Failures: Always check the return value of memory allocation functions like malloc or new to ensure they succeeded.

int* ptr = (int*)malloc(sizeof(int));
if (ptr != NULL) {
    // Allocation succeeded
    *ptr = 10;
}

Use nullptr Instead of NULL: In modern C++, prefer using nullptr over NULL as it provides better type safety.

int* ptr = nullptr; // Modern C++

Avoid Dangling Pointers: Ensure that pointers are not left pointing to memory that has been freed. Set them to nullptr after freeing the memory.

free(ptr);
ptr = nullptr;

Use Static Analysis Tools: Utilize static analysis tools that can detect potential null pointer dereferences in your code. 