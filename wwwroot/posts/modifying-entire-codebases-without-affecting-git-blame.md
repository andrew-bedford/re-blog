---
id: modifying-entire-codebases-without-affecting-git-blame
title: Modifying entire codebases without affecting git blame
abstract: 
created: 2025-02-24
tags: git
---

# Modifying entire codebases without affecting `git blame`
There are times when we might want to modify the entire codebase, for example to reformat the code, to do some automated large-scale refactoring, or to automatically apply fixes offered by some static analysis tools. One thing that might make us hesitate is that these actions would affect the output of `git blame`, which is often useful in understanding why the code is the way it is. Large portions of the code would blame tools that automatically modified the codebase. To address this problem, git introduced in version 2.23 the ability for `git blame` to ignore specific commits.
```
git blame --ignore-rev <hash>
```

That is, for the lines that blame commit `<hash>`, `git blame` would now return the previous commit instead. A file can also be used to store all the commit hashes to ignore. This file can be named however you want, but the convention appears to be to use `.git-blame-ignore-revs`. For example, see the one used by [llvm](https://github.com/llvm/llvm-project/blob/main/.git-blame-ignore-revs):
```
#[libc++][NFC] Apply clang-format on large parts of the code base
5aa03b648b827128d439f705cd7d57d59673741d

#[clang][NFC] Remove trailing whitespaces and enforce it in lib, include and docs
f6d557ee34b6bbdb1dc32f29e34b4a4a8ad35e81
```

Then it can be used to ignore multiple commits at the same time:
```
git blame --ignore-revs-file .git-blame-ignore-revs
```

To avoid having to add these options everytime you use `git blame`, or to have it work in some development environments, we can use:
```
git config --global blame.ignoreRevsFile .git-blame-ignore-revs
```
