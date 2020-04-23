

"(" = Enter new abstraction, 1 order "deeper" than the current context.

")" = Exit the current abstraction

"?" = Ambiguity object

"[" = Begin meta-group

"]" = Close meta-group

"*" = Kleene star (for meta groups)

"|" = Meta group union / Sum Type

"@" = Meta-variable indicator

All the meta stuff is for dealing with literal code.

```
A => (A)
(A) => ((A))
[A] => A
[(A)] => (A)

(A B) => ((A B))



([A]*) => (
	(A)
)

(A [B | C]) => (
	(A B)
	(A C)
)
```



```lisp
[(A B]* => (
	(A B)
	(A B (A B))
	(A B (A B (A B)))
	....
)

#Alias Number:
(Number
	[Zero | [(Succ @Number]*]
)
=> (
	(Number Zero)
	(Number (Succ (Number Zero)))
)

("1" (Succ (Number Zero)))


(implies
	// meta-variables are equivalent strings of data as long as they're within the same meta-group
	[
        (and (implies @P @Q) (implies @Q @R))
        (implies @P @R)
	]
)


#Alias List:
(List
	(Head A)
	(Tail (List
			(Head B)
			(Tail ?)
          )
	)
)
```



