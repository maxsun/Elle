# Elle

## Overview

Elle is an experimental/toy programming language for building and playing language games.

In $\lambda$-Calculus, expressions denote either functions or application of functions. The syntactic mechanics of computation are implicit within the calculus rather than explicitly described (e.g. $\beta$-reduction). Consequently, $\lambda$-Calculus models computation at the level of abstract algorithms, but not at the level of data-manipulations. 

In Elle, a computation is a context sensitive process mapping input data to output data.

EDIT: a computation doesn't need to be context sensitive, but a representation of one is...

```

Parse :: in Data, ctx Data -> out Computation_Rep
Computation_Rep :: in Data -> out Data


```



```
Computation :: in Data, ctx Data -> out Data
```

Computations are performed by an interpreter which has 2 main jobs:

1. Establishing a semantic baseline; assigning reference to context-free data.  
2. Performing "valid" symbolic manipulations.

The Elle Interpreter is a tool for performing the computations described in Elle. Since interpretation is a computation, it's also a context sensitive mapping.

```
# Interpretation is-a Computation
Interpretation :: in Data, ctx Data -> out Data
```

Interpretation parses Elle data into representations of computations according to contextual data. These abstractions represent mappings between sets of data, which may be reduced or manipulated according to symbolic rules. Relative to some context, a string of data "denotes" the set of representations which it maps to. Informally, the job of the Elle interpreter is to identify abstract Types/patterns in data and the relationships between them.



## Extra Notes

Curry-Howard-Lambek Correspondence:

Lambek showed that Lambda Calculus can be modeled with Cartesian closed categories. Roughly, a category with finite products is Cartesian if:

1. It is possible to specify the product for each pair of objects or
2. a global axiom of choice (every object in a given set is distinguishable)
3. the monoidal product is an "anafunctor" (a functor that doesn't require the axiom of choice)

Lambek's Calculus birthed the family of formalisms called "Categorical Grammars".



## Excerpts

From "Categorifying CCCs: Computation as a Process (John Baez)"

> the λ-calculus could be seen as a particularly elegant computer language, in which computations were really just proofs ... the λ-calculus was in some sense equivalent to the formalism of cartesian closed categories ... objects of the CCC correspond to “data types”. 
>
> ... morphisms in a CCC were really more like *equivalence classes of proofs*, where the equivalence relation seemed to wash out some really interesting stuff - stuff that looks like "2-morphisms between morphisms".
>
> I got even more upset when these “2-morphisms” seemed to be precisely the “computational work” that a computer implementing the λ-calculus would need to do to actually compute anything. I’m talking about things like β-reduction.

From "Lambda Calculus (SEP)"

> **Theorem** (Church-Rosser) If $P \triangleright βQ$ and $P \triangleright β R$, then there exists a term S such that both $Q \triangleright βS$ and $R \triangleright βS$.
>
> ...
>
> The Church-Rosser theorem gives us, among other things, that the plain λ-calculus—that is, the theory **λ** of equations between λ-terms—is consistent, in the sense that not all equations are derivable.
>
> [Note: Because if an expression is in normal form, there is no $\beta$-reduction sequence which can "prove" it]
>
> ...
>
> The cardinality argument shows that if we are to have a semantics for λ-calculus, the interpretation of λ-terms cannot simply be functions in the set-theoretic sense of the term ... models solve the cardinality problem by restricting the domain $X$ of interpretation, so that, in them, $X$ is in a suitable sense isomorphic to the ‘function space’ $X^X$.
>
> ...
>
> One could understand λ-terms as denoting relations, and read an abstraction term '$λx[M]$' as the unary relation (or property) $R$ that holds of an argument $x$ just in case $M$ does (see Carnap 1947, p. 3). On the relational reading, we can understand an application term $MN$ as a form of predication. 



## Incomplete Ideas/Questions

1. Is there a relationship between Kripke Semantics and Information Algebras?



## References

[^0] [Categorifying CCCs: Computation as a Process (Catefory Cafe)](https://golem.ph.utexas.edu/category/2006/08/categorifying_cccs_seeing_comp.html)

[^1] [CCCs and the Lambda-Calculus (Category Cafe)](https://golem.ph.utexas.edu/category/2006/08/cartesian_closed_categories_an_1.html)

[^2] [Cartesian Category (nLab)](https://ncatlab.org/nlab/show/cartesian+monoidal+category)

[^3] [Intuitionistic Logic (SEP)](https://plato.stanford.edu/entries/logic-intuitionistic/#KriSemForIntLog)

[^4] [Substructural Logics (SEP)](https://plato.stanford.edu/entries/logic-substructural/)

[] [Sequent Calculus (MathWorld)](https://mathworld.wolfram.com/SequentCalculus.html)

[] [Interactive Sequent Calculus (MIT)](http://logitext.mit.edu/tutorial)