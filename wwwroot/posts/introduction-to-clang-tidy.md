---
id: introduction-to-clang-tidy
title: Introduction to clang-tidy
abstract: 
created: 2024-07-18
tags: draft, c/c++, clang
---

# Introduction to clang-tidy

## Installation
If you are using a Ubuntu-based distribution, LLVM provides [a shell script](https://apt.llvm.org/) to make the installation easier:
```
wget https://apt.llvm.org/llvm.sh
chmod +x llvm.sh
sudo ./llvm.sh
```
This will install the latest stable version of LLVM by default, which is currently version 18.

```
sudo apt install clang-tidy
```

```
clang-tidy --list-checks
```