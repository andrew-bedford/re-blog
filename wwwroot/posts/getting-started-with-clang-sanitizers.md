---
id: getting-started-with-clang-sanitizers
title: Getting started with clang sanitizers
abstract: Learn about the different clang sanitizers, 
created: 2024-07-22
tags: draft, c/c++, clang
---

# Getting started with clang sanitizers
Sanitizers are runtime tools used to detect various types of bugs and undefined behaviors in programs, such as out-of-bounds accesses, memory leaks, use-after-free and uninitialized memory. They work by instrumentating your program (i.e., inserting runtime checks). For this reason, they can have a significant impact on performance and are typically not enabled in release mode. Still, they are invaluable tools that can be used during development to identify bugs that might otherwise go unnoticed.

Both [clang](https://clang.llvm.org/docs/index.html) and [gcc](https://gcc.gnu.org/onlinedocs/gcc/Instrumentation-Options.html) come with a set of integreated sanitizers that can be enable using specific flags. For the purposes of this article, we will focus on the ones from clang. More specifically, we will look at the most commonly used ones, how to enable them and how to interpret their results.

## Installation
If you do not already have clang installed, you could install your distribution's version using its package manager (e.g., `sudo apt install clang clang++`), but chances are that it won't be a recent version. To install the latest stable version, LLVM provides a nice [shell script](https://apt.llvm.org/) that simplifies its installation:
```
wget https://apt.llvm.org/llvm.sh
chmod +x llvm.sh
sudo ./llvm.sh
```
This will install LLVM's latest stable version by default, but it can also be used to install a specific version using
```
sudo ./llvm.sh <version number>
```
That's it, you should now have everything you need to start using sanitizers!

## Sanitizers
### AddressSanitizer
 (ASan) Detects memory errors such as out-of-bounds accesses, use-after-free, and memory leaks1.

#### Use-after-free
(dangling pointer dereference)
#### Use after return
#### Use after scope
```
volatile int *p = 0;

int main() {
  {
    int x = 0;
    p = &x;
  } // x goes out of scope, so its address is no longer valid
  *p = 5; // dereferences a dangling pointer
  return 0;
}
```
```
clang -g -fsanitize=address test.cpp
```
```
================================================================
==272015==ERROR: AddressSanitizer: stack-use-after-scope on address 0x7ffea8c87800 at pc 0x598a936b1ff5 bp 0x7ffea8c877d0 sp 0x7ffea8c877c8
WRITE of size 4 at 0x7ffea8c87800 thread T0
    #0 0x598a936b1ff4 in main /home/abedford/Projects/Sanitizers/test.cpp:8:6
    #1 0x73908f429d8f  (/lib/x86_64-linux-gnu/libc.so.6+0x29d8f) (BuildId: 490fef8403240c91833978d494d39e537409b92e)
    #2 0x73908f429e3f in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x29e3f) (BuildId: 490fef8403240c91833978d494d39e537409b92e)
    #3 0x598a935f4304 in _start (/home/abedford/Projects/Sanitizers/a.out+0x1e304) (BuildId: 8437efe4effc2d9d8c6e538df72d49b4df425585)

Address 0x7ffea8c87800 is located in stack of thread T0 at offset 32 in frame
    #0 0x598a936b1eaf in main /home/abedford/Projects/Sanitizers/test.cpp:3

  This frame has 1 object(s):
    [32, 36) 'x' (line 5) <== Memory access at offset 32 is inside this variable
HINT: this may be a false positive if your program uses some custom stack unwind mechanism, swapcontext or vfork
      (longjmp and C++ exceptions *are* supported)
SUMMARY: AddressSanitizer: stack-use-after-scope /home/abedford/Projects/Sanitizers/test.cpp:8:6 in main
==270877==ABORTING

```

    Heap buffer overflow
    Stack buffer overflow
    Global buffer overflow
    Initialization order bugs
    Memory leaks


### ThreadSanitizer
 (TSan) Identifies data races and other threading issues2.
### MemorySanitizer
 (MSan) Finds uses of uninitialized memory2.
### UndefinedBehaviorSanitizer
 (UBSan) Catches various kinds of undefined behavior, such as integer overflows and invalid type casts2.
### LeakSanitizer
 (LSan) Specifically targets memory leaks2.

These sanitizers are integrated into the Clang compiler and can be enabled using specific compiler flags (e.g., -fsanitize=address for AddressSanitizer). They are invaluable for improving code quality and security by catching bugs that might otherwise go unnoticed3.

In order to use them you, you need to compile and link your program using clang with the -fsanitize=address switch. To get a reasonable performance add -O1 or higher. To get nicer stack traces in error messages add -fno-omit-frame-pointer. 


```
sudo apt install clang-tidy
```