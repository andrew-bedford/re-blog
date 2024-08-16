---
id: getting-started-with-clang-sanitizers
title: Getting started with clang sanitizers
abstract: Learn about the different clang sanitizers, 
created: 2024-08-16
tags: c/c++, clang, dynamic analysis
---

# Getting started with clang sanitizers
Sanitizers are runtime tools used to detect various types of bugs and undefined behaviors in programs, such as out-of-bounds accesses, memory leaks, use-after-free and uninitialized memory. They work by instrumentating your program (i.e., inserting runtime checks). For this reason, they can have a significant impact on performance and are typically not enabled in release mode. Still, they are invaluable tools that can be used during development to identify bugs that might otherwise go unnoticed.

Both [clang](https://clang.llvm.org/docs/index.html) and [gcc](https://gcc.gnu.org/onlinedocs/gcc/Instrumentation-Options.html) come with a set of integrated sanitizers that can be enable using specific flags. For the purposes of this article, we will focus on the ones from clang. More specifically, we will look at the most commonly used ones, how to enable them and how to interpret their results.
 
## Installation
If you do not already have clang installed, you could install your distribution's version using its package manager:
```
sudo apt install clang clang++
```
However, chances are that it won't be a recent version. To install the latest stable version, LLVM provides a nice [shell script](https://apt.llvm.org/) that simplifies its installation:
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
Once you've recompiled your program with a sanitizer enabled (see below), execute your program as usual. The sanitizer will monitor its execution and report issues on the standard output, if it finds any. Note that clang only allows one sanitizer to be enable at a time.

### AddressSanitizer
The AddressSanitizer (ASan) detects memory errors such as out-of-bounds accesses, use-after-free, and memory leaks. It is one of the most used clang sanitizers.

<!-- #### Use after free -->
<!-- (dangling pointer dereference) -->
<!-- #### Use after return -->
#### Use after scope
Consider the following example where the address of scoped variable `x` is assigned to the global pointer variable `p`. Once `x` goes out of scope, its address is no longer valid.
```cpp
int* p = 0;

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
```bash
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
hadow bytes around the buggy address:
  0x100055188eb0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x100055188ec0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x100055188ed0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x100055188ee0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x100055188ef0: 00 00 00 00 00 00 00 00 00 00 00 00 f1 f1 f1 f1
=>0x100055188f00:[f8]f3 f3 f3 00 00 00 00 00 00 00 00 00 00 00 00
  0x100055188f10: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x100055188f20: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x100055188f30: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x100055188f40: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x100055188f50: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:           00
  Partially addressable: 01 02 03 04 05 06 07 
  Heap left redzone:       fa
  Freed heap region:       fd
  Stack left redzone:      f1
  Stack mid redzone:       f2
  Stack right redzone:     f3
  Stack after return:      f5
  Stack use after scope:   f8
  Global redzone:          f9
  Global init order:       f6
  Poisoned by user:        f7
  Container overflow:      fc
  Array cookie:            ac
  Intra object redzone:    bb
  ASan internal:           fe
  Left alloca redzone:     ca
  Right alloca redzone:    cb
==270877==ABORTING
```
<!-- Heap buffer overflow
Stack buffer overflow
Global buffer overflow
Initialization order bugs
Memory leaks -->

<!-- ### ThreadSanitizer
The ThreadSanitizer (TSan) identifies data races and other threading issues.

-### MemorySanitizer
The MemorySanitizer (MSan) finds uses of uninitialized memory.

-### UndefinedBehaviorSanitizer
The UndefinedBehaviorSanitizer (UBSan) catches various kinds of undefined behavior, such as integer overflows and invalid type casts.

-### LeakSanitizer
The LeakSanitizer (LSan) specifically targets memory leaks. -->
