% ---------- Gender Facts ----------
male(john).
male(mike).
male(david).
male(kevin).

female(mary).
female(linda).
female(susan).
female(anna).

% ---------- Parent Relationships ----------
parent(john, mike).
parent(mary, mike).

parent(john, linda).
parent(mary, linda).

parent(mike, david).
parent(susan, david).

parent(mike, anna).
parent(susan, anna).

parent(linda, kevin).

% ---------- Marriage Relationships ----------
married(john, mary).
married(mike, susan).

% =====================================================
%               FAMILY RELATIONSHIP RULES
% =====================================================

% -----------------------------------------------------
% Father Rule
% X is father of Y if:
% 1. X is a parent of Y
% 2. X is male
% -----------------------------------------------------
father(X, Y) :-
    parent(X, Y),
    male(X).


% -----------------------------------------------------
% Mother Rule
% X is mother of Y if:
% 1. X is a parent of Y
% 2. X is female
% -----------------------------------------------------
mother(X, Y) :-
    parent(X, Y),
    female(X).


% -----------------------------------------------------
% Sibling Rule
% X and Y are siblings if:
% 1. They share at least one common parent Z
% 2. X and Y are not the same person
% -----------------------------------------------------
sibling(X, Y) :-
    parent(Z, X),
    parent(Z, Y),
    X \= Y.


% -----------------------------------------------------
% Brother Rule
% X is brother of Y if:
% 1. X and Y are siblings
% 2. X is male
% -----------------------------------------------------
brother(X, Y) :-
    sibling(X, Y),
    male(X).


% -----------------------------------------------------
% Sister Rule
% X is sister of Y if:
% 1. X and Y are siblings
% 2. X is female
% -----------------------------------------------------
sister(X, Y) :-
    sibling(X, Y),
    female(X).


% -----------------------------------------------------
% Grandparent Rule
% X is grandparent of Y if:
% 1. X is parent of Z
% 2. Z is parent of Y
% -----------------------------------------------------
grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).


% -----------------------------------------------------
% Grandfather Rule
% X is grandfather of Y if:
% 1. X is grandparent of Y
% 2. X is male
% -----------------------------------------------------
grandfather(X, Y) :-
    grandparent(X, Y),
    male(X).


% -----------------------------------------------------
% Grandmother Rule
% X is grandmother of Y if:
% 1. X is grandparent of Y
% 2. X is female
% -----------------------------------------------------
grandmother(X, Y) :-
    grandparent(X, Y),
    female(X).


% -----------------------------------------------------
% Uncle Rule
% X is uncle of Y if:
% 1. X is brother of Z
% 2. Z is parent of Y
% -----------------------------------------------------
uncle(X, Y) :-
    brother(X, Z),
    parent(Z, Y).


% -----------------------------------------------------
% Aunt Rule
% X is aunt of Y if:
% 1. X is sister of Z
% 2. Z is parent of Y
% -----------------------------------------------------
aunt(X, Y) :-
    sister(X, Z),
    parent(Z, Y).


% -----------------------------------------------------
% Cousin Rule
% X and Y are cousins if:
% 1. Their parents are siblings
% 2. X and Y are not the same person
% -----------------------------------------------------
cousin(X, Y) :-
    parent(P1, X),
    parent(P2, Y),
    sibling(P1, P2),
    X \= Y.


% -----------------------------------------------------
% Ancestor Rule (Recursive Rule)
%
% Base Case:
% X is ancestor of Y if X is direct parent of Y
% -----------------------------------------------------
ancestor(X, Y) :-
    parent(X, Y).

% -----------------------------------------------------
% Recursive Case:
% X is ancestor of Y if:
% 1. X is parent of Z
% 2. Z is ancestor of Y
% -----------------------------------------------------
ancestor(X, Y) :-
    parent(X, Z),
    ancestor(Z, Y).



% =====================================================
%           ADVANCED FAMILY RELATIONSHIPS
% =====================================================

% -----------------------------------------------------
% Husband Relationship
% X is husband of Y if:
% 1. X is male
% 2. X and Y are married
% -----------------------------------------------------
husband(X,Y) :-
    male(X),
    married(X,Y).


% -----------------------------------------------------
% Wife Relationship
% X is wife of Y if:
% 1. X is female
% 2. X and Y are married
% -----------------------------------------------------
wife(X,Y) :-
    female(X),
    married(X,Y).


% -----------------------------------------------------
% Child Relationship
% X is child of Y if Y is parent of X
% -----------------------------------------------------
child(X,Y) :-
    parent(Y,X).


% -----------------------------------------------------
% Son Relationship
% X is son of Y if:
% 1. X is child of Y
% 2. X is male
% -----------------------------------------------------
son(X,Y) :-
    child(X,Y),
    male(X).


% -----------------------------------------------------
% Daughter Relationship
% X is daughter of Y if:
% 1. X is child of Y
% 2. X is female
% -----------------------------------------------------
daughter(X,Y) :-
    child(X,Y),
    female(X).


% -----------------------------------------------------
% Father-in-law Relationship
% X is father-in-law of Y if:
% 1. X is father of Z
% 2. Z is married to Y
% -----------------------------------------------------
father_in_law(X,Y) :-
    father(X,Z),
    married(Z,Y).


% -----------------------------------------------------
% Mother-in-law Relationship
% X is mother-in-law of Y if:
% 1. X is mother of Z
% 2. Z is married to Y
% -----------------------------------------------------
mother_in_law(X,Y) :-
    mother(X,Z),
    married(Z,Y).


% -----------------------------------------------------
% Nephew Relationship
% X is nephew of Y if:
% 1. X is male
% 2. X parent is sibling of Y
% -----------------------------------------------------
nephew(X,Y) :-
    male(X),
    parent(Z,X),
    sibling(Z,Y).

% -----------------------------------------------------
% Niece Relationship
% X is niece of Y if:
% 1. X is female
% 2. X parent is sibling of Y
% -----------------------------------------------------
niece(X,Y) :-
    female(X),
    parent(Z,X),
    sibling(Z,Y).