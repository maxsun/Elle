# Elle

*A functional programming language built for Language Oriented Programming & proof assistance.*

## Introduction

Expressions in Elle are written in Data; finite ordered sequences of symbols. For practicality, any UTF-8 String is valid Data.

The Elle interpreter takes Data as input and produces Data as output according to “context” Data:
$$
\text{Interpretation} : \text{Data}, \text{Data} \rightarrow \text{Data}
$$
Critically, Data by itself is meaningless -- its only meaning is in Interpretation. The first step in Interpretation is the conversion of Elle expressions into objects in the Elle Algebra called "Structures".
$$
\text{Parse} : \text{Data} \rightarrow \text{Struct}
$$


