# Prolog DCG Tester

Tests Prolog DCG's which conform to an s/3 predicate where s is the top level sentence predicate.

Built for a prolog coursework.

## Usage

Execute via `python dcg_test.py example.pl example.test`

If your predicate is an s/2 which doesn't generate a tree pass `--no-tree` as the 3rd argument

Execute via `python dcg_test.py example.pl example.test --no-tree`

## Requirements

Tested on Python 3.11.9 on a Linux System (NixOs)

Uses the Colorama Python Package

## Building a Tests File

Each test is on a new line, tests which should fail start with an '*'.

The program converts all text to lower case.

Example:
```
The man hires the woman
The men hire the woman
*A man hire the woman
*The women hires the men
```

## Example DCG and Test Results
```prolog
% Sentence
s(s(NP,VP)) --> np(P, NP),vp(P, VP).

% Noun Phrase
np(P, np(Det,N))
    --> det(P, Det),
        n(P, N).

% Verb Phrase
vp(P, vp(V,NP))
    --> tv(P,V),
        np(_,NP).
...
```
```
Tests:
14 Passed
0 Failed
a man hires the woman --> Passed
a man hires the women --> Passed
the man hires the woman --> Passed
the men hire the woman --> Passed
...
```