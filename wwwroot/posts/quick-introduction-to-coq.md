---
id: quick-introduction-to-coq
title: Quick introduction to Coq
abstract: Learn the basics of Coq, an interactive theorem prover that is based on the calculus of inductive constructions.
created: 2024-01-01
tags: coq, proof
---
# Quick introduction to Coq
Writing proofs can be a challenging task, but checking the correctness
of a proof should be straightforward: read the proof line-by-line and
validate each of its arguments. However in practice, this seemingly
simple task can be exceedingly hard. To help address these issues,
computer scientists have created tools that help humans write and prove
theorems: *automatic theorem provers* and *interactive theorem provers*.

**Automatic theorem provers** : As the name implies, automatic theorem
provers automatically prove theorems. They usually can only prove
domain-specific theorems. For instance,
[Beagle](https://bitbucket.org/peba123/beagle/src/master/) specializes
in first-order logic and MetiTarski specializes in numeric formulas
verification. As their use is limited in the field of language-based
security, we will instead focus on interactive theorem provers.

**Interactive theorem provers**: Interactive theorem provers do not seek
to automatically prove theorems, their main goal is instead to help
users write error-free proofs. As the user writes the proof, the prover
validates each argument and keeps track of what remains to be proved.
Hence, this process results in a machine-checked proof.

In the field of language-based security, [Coq](https://coq.inria.fr/)
and [Isabelle](https://isabelle.in.tum.de/) are the two most popular
theorem provers.

## Programming
Coq's language syntax is similar to [OCaml's](https://ocaml.org/).

### Defining constants
Constants can be defined using the keyword `Definition`. For example:

    Definition zero := 0.

### Inductive types
The set of natural numbers can be defined inductively as follows:

    Inductive nat : Set :=
      | O : nat
      | S : nat -> nat.

This definition states that a natural number is either zero or the
successor of a natural number. The successor here is defined as a
function that takes a natural number and returns a natural number
(`nat -> nat`).

#### Enumerations

    Inductive bool : Set :=
      | false : bool
      | true : bool.

For inductive definitions, the types are optional. That is, the
following definition would be equivalent:

    Inductive bool : Set :=
      | false
      | true.

### Coinductive types
Coq also supports coinductive types. This can be used to represent
infinite data structures such as streams.

    CoInductive nat_stream : Type :=
      | Cons : nat -> nat_stream -> nat_stream.

    CoFixpoint stream_of_zeroes : nat_stream :=
      Cons 0 stream_of_zeroes. (* 0::0::0::0::0::0::0... *)

### Functions
Functions can be declared using the keyword `Function`.

    Function pred (n : nat) : nat :=
      match n with
      | O => O
      | S n' => n'
      end.

    Check pred.
                                                            pred : nat -> nat

One particularity of Coq is that it does not allow non-terminating
functions; doing so would lead to logical inconsistencies.

To verify that a recursive function terminates, Coq uses a simple
heuristic: it verifies that each recursive call reduces the size of
arguments. Meaning that Coq will only accept recursive functions if the
recursive calls use subterms of the original argument.

### Extraction
One interesting feature of Coq is that it can extract and translate
functions to other languages (Ocaml, Haskell or Scheme). For example,
executing the code below would generate a file `imperative.ml` which
contains the OCaml version of function `eval` as well as any other
definitions on which it depends.

``` {.sourceCode .ocaml}
Extraction Language Ocaml. (*Target language*)
Require Import Foo. (*Module in which the function definition is located*)
Extraction "imperative.ml" eval. (*Filename and function to extract*)
```

This means that we can use Coq to not only be used to verify programs,
but also generate certified programs.

## Tactics
Tactics are functions/algorithms that transform propositions. In this
section, we will go through a set of basic tactics that can be used to
prove most theorems (or at least most of those found in Software
Foundations).

### admit

Used to admit that goal or subgoal is true. This tactic can be used to
temporarily skip over\
goals/subgoals. If a proof contains an admit, `Admitted` must be used
instead of `Qed`.

``` {.coq}
Lemma modus_ponens:
  forall p q : Prop, (p -> q) -> p -> q.
Proof.
  admit.
Admitted.
```

### apply/eapply
Used to apply hypotheses/lemmas/theorem to the current goal. In the
following example,\
we have as hypothesis that (p -\> q)

``` {.coq}
Lemma modus_ponens:
  forall p q : Prop, (p -> q) -> p -> q.
Proof.
  intros.       (* *)
  apply H.      (* *)
  assumption.   (* *)
Qed.
```

### assert/cut
Used to assert something and add it to the current context. This can be
useful if we need an additional hypothesis to solve the current goal.

In the case of assert (see `xyz_with_assert`), we must demonstrate that
it is true before it is added to the context.

``` {.coq}
Lemma xyz_with_assert:
  forall (f: bool->bool) x y z, x = y -> y = z -> f x = f z.
Proof.
  intros.
  assert (x = z). { subst. reflexivity. } (* Proof of the assert *)
  subst. reflexivity. (* Proof of the main goal *)
Qed.
```

A similar tactic to `assert` is `cut`. In the case of cut (see
`xyz_with_cut`), we can use it immediately to prove the current goal,
but will have to prove that the hypothesis added is true before the end
of the proof.

    Lemma xyz_with_cut:
      forall (f: bool->bool) x y z, x = y -> y = z -> f x = f z.
    Proof.
      intros.
      cut (x = z).
      - intro. subst. reflexivity. (* Proof of the main goal *)
      - subst. reflexivity. (* Proof of the cut (x = z) *)
    Qed.

### assumption
Used when our current goal is already one of our assumptions (i.e.,
already present in the context).

``` {.coq}
Lemma modus_ponens:
  forall p q : Prop, (p -> q) -> p -> q.
Proof.        (* |- forall p q : Prop, (p -> q) -> p -> q *)
  intros.     (* p q:Prop, H:(p -> q), H0:p |- q *)
  apply H.    (* p q:Prop, H:(p -> q), H0:p |- p *)
  assumption. (* True *)
Qed.
```

### destruct
Used to perform case analyses. In the example below, we use `destruct`
to prove that the expression is true for all possible values of `b`
(true and false).

``` {.coq}
Lemma not_not_b_equals_b:
  forall b:bool, not (not b) = b.
Proof.
  intro.
  destruct b.
  - (* Case b = true *)   (* |- not (not true) = true *)
    simpl.                (* |- true = true *)
    reflexivity.          (* True *)
  - (* Case b = false *)  (* |- not (not false) = false *)
    simpl.                (* |- false = false *)
    reflexivity.          (* True *)
Qed.
```

The main difference between `destruct` and `induction` is that
`destruct` does not add induction hypotheses to the context.

### exists/eexists
When we want to prove that something exists, we need to provide Coq with
a witness (i.e., an instance) and then prove that the goal is true using
the witness. In the example below, we tell Coq that the value `2` should
satisfy the equation and then prove by simplying the equation that it
indeed does.

    Example one_plus_x : exists x, 1 + x = 3.
    Proof.                        (* |- exists x, 1 + x = 3 *)
      exists 2.                   (* |- 1 + 2 = 3 *)
      simpl.                      (* |- 3 = 3 *)
      reflexivity.                (* |- True *)
    Qed.

Use the `eexists` tactic when you need to symbolically manipulate
propositions (i.e, without instanciating existential variables). This
can be useful when we do not yet know what the witness should be.

    Example one_plus_x' : exists x, 1 + x = 3.
    Proof.                        (* |- exists x, 1 + x = 3 *)
      eexists.                    (* |- 1 + ?x = 3 *)
      simpl.                      (* |- S ?x = 3 *)
      apply f_equal.              (* |- ?x = 2 *)
      reflexivity.                (* True *)
    Qed.

After the `eexists`, the `x` is replaced with `?x`. Before the proof can
be completed, witnesses/values for each of the `?` variables must be
found.

### induction
Used to perform induction. In the example below, the `induction` tactic
adds two subgoals/cases to prove: one for each the constructor of
natural numbers (since `n` is a natural number).

    Lemma n_plus_O:
      forall n, (add n O) = n.
    Proof.
      induction n as [ | n'].
      - (* Case n = 0 *)
                      (* |- 0 + 0 = 0 *)
        simpl.        (* 0 = 0 *)
        reflexivity.  (* True *)
      - (* Case n = S n' *)
                      (* n':nat, IHn':n' + 0 = n' |- S n' + 0 = S n' *)
        simpl.        (* n':nat, IHn':n' + 0 = n' |- S (n' + 0) = S n' *)
        rewrite IHn'. (* n':nat, IHn':n' + 0 = n' |- S n' = S n' *)
        reflexivity.  (* True *)
    Qed.

### intro/intros
Used to introduce variables and hyptheses into the context. The tactic
`intro` introduces one variable/hypothesis at a time while `intros`
introduces them all at once.

### inversion
Used to infer the necessary conditions for a hypothesis to be true and
add them to the current context. For instance, in the example below,
applying the `inversion` tactic on hypothesis `H : S a = S b` adds
hypothesis `H1 : a = b` to the context.

    Lemma successors_equal_implies_equal:
      forall a b, S a = S b -> a = b.
    Proof.
      intros.       (* a, b : nat, H : S a = S b |- a = b*)
      inversion H.  (* a, b : nat, H : S a = S b, H1 : a = b |- b = b*)
      reflexivity.  (* True *)
    Qed.

This tactic is also useful to solve goals that contain an hypothesis
that is false (recall that false -\> anything is true).

    Lemma false_hypothesis : 1 = 2 -> 1 + 1 = 4.
    Proof.         (* |- 1 = 2 -> 1 + 1 = 4. *)
      intros.      (* H : 1 = 2 |- 1 + 1 = 4 *)
      inversion H. (* True (since the hypothesis is false))
    Qed.

### reflexivity
Used to finish equality proofs.

    Lemma refl:
      forall x:Type, x = x.
    Proof.          (* |- forall x:Type, x = x *)
      intro.        (* x : Type |- x = x*)
      reflexivity.  (* True *)
    Qed.

### rewrite
Used to rewrite expressions which we know are equivalent. For example,
since we know have as hypothesis `H : x = y`, `rewrite H` replaces
instances of `x` with `y` in the current goal. Similarly, since we know
that `H0 : y = z`, `rewrite <- H0` replaces instances of `z` with `y`.
The arrow denotes the direction of the rewrite (it is `->` by default).

    Lemma trans_eq :
      forall x y z:nat, x = y -> y = z -> x = z.
    Proof.            (* |- forall x y z:nat, x = y -> y = z -> x = z *)
      intros.         (* x y z:nat, H : x = y, H0 : y = z |- x = z *)
      rewrite H.      (* x y z:nat, H : x = y, H0 : y = z |- y = z *)
      rewrite <- H0.  (* x y z:nat, H : x = y, H0 : y = z |- y = y *)
      reflexivity.    (* True *)
    Qed.

### simpl
Used to simplify expressions. If it is unable to, it will leave the goal
unchanged. In the example below, `simpl` is able to simplify the
expression `plus O n` to `n`.

    Theorem O_plus_n : forall n : nat, plus O n = n.
    Proof.            (* |- forall n : nat, plus O n = n *)
      intro.          (* n : nat |- plus O n = n *)
      simpl.          (* n : nat |- n = n *)
      reflexivity.    (* True *)
    Qed.

Yet it is unable to simplify expression `plus n O`.

    Theorem n_plus_O : forall n : nat, plus n O = n.
    Proof.
    Proof.            (* |- forall n : nat, plus n O = n *)
      intro.          (* n : nat |- plus n O = n *)
      simpl.          (* n : nat |- plus n O = n *)
      (* simpl is unable to simplify *)

The reason becomes apparent if we look at the definition of `plus`.

    Fixpoint plus (n m : nat) : nat :=
      match n with
        | O => m
        | S n' => S (plus n' m)
      end.

In the case of `plus O n`, Coq matches the first argument `O` and
returns the second argument `n` (because of `| O => m`). While in the
case of `plus n O`, Coq is unable to match the first argument `n` with
either cases (`O` or `S n'`) as it could be either.

### split
Used to split goals that have a logical and into two goals.

### unfold
Used to replace a function with its definition. It is sometimes
necessary in order to progress.

    Definition square n := n * n.
    Lemma square_mult : forall n m, square (n * m) = square n * square m.
    Proof.
      intros n m.
      simpl. (* Unable to simplify. Would be stuck without unfold. *)
      unfold square.
    ...

## Commands
Coq includes some useful commands. Here are the ones that I found myself
using the most often.

### Check
Used to check the type of an expression. For example, checking the type
of `plus` returns that it is a function that takes two natural numbers
and returns a natural number.

    Check plus.
                                                      plus : nat -> nat -> nat

### Compute
Used to evaluate an expression. Useful when testing the definitions of
functions.

    Compute 2+2.
                                                                     = 4 : nat

### Locate
Used to learn the meaning behind a notation. For example, we can use it
to learn which function is called when the `+` operator is used. In this
case, we can see that the `+` operator can call different functions
depending on the type of its arguments.

    Locate "+".
                                   Notation                         Scope
                                   "{ A } + { B }" := sumbool A B : type_scope
                                   "A + { B }" := sumor A B       : type_scope
                                   "x + y" := Nat.add x y         : nat_scope
                                   "x + y" := sum x y             : type_scope

### Print
Used to print the definition of an expression. For example, printing the
definition of `nat` reveals that it is a set defined inductively and has
two constructors.

    Print nat.
                              Inductive nat : Set :=  O : nat | S : nat -> nat

Print can also be used to print the \"proof\" of a theorem, although the
result can be hard to interpret.

### Search
Used to search among the definitions of currently loaded modules. The
parameter can be either a type, a keyword or a pattern. Multiple
parameters can be specified in order to refine the search. For example,
the following command searches for definitions that involve the type
`list`, whose name contain `"eq"` and whose type contain something of
the form `(_ ++ _ = _)`.

    Search list "eq" (_ ++ _ = _).

            app_eq_nil:
                forall (A : Type) (l l' : list A), l ++ l' = nil ->
                l = nil /\ l' = nil
            app_eq_unit:
                forall (A : Type) (x y : list A) (a : A), x ++ y = a :: nil ->
                x = nil /\ y = a :: nil \/ x = a :: nil /\ y = nil

### SearchRewrite
Same as **Search**, but shows only theorems that can be used to rewrite
an expression and can only take a pattern as parameter. For example, if
we are interested in rewriting an expression of the form
`((_ ++ _) ++ _)`, **SearchRewrite** tells us that there are two
possibilities: `app_assoc` and `app_assoc_reverse`.

    SearchRewrite ((_ ++ _) ++ _).

            app_assoc:
               forall (A : Type) (l m n : list A), l ++ m ++ n = (l ++ m) ++ n
            app_assoc_reverse:
               forall (A : Type) (l m n : list A), (l ++ m) ++ n = l ++ m ++ n

