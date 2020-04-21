''' An implementation of the Elle Language interpreter '''
# from lark import Lark, Transformer, v_args, lexer, tree
from typing import List, Set, Union, Iterable, Optional, NamedTuple
import lark


def variable(name: str) -> tuple:
    return ('VAR', name)


def abstraction(args: List[tuple], body) -> tuple:
    return ('LAMBDA', args, body)


def application(tail, head) -> tuple:
    return ('APP', tail, head)


def transform_lark_token(lark_token: lark.lexer.Token):
    token_type = lark_token.type
    token_data = lark_token.value
    if token_type == 'NAME':
        return variable(token_data[0])
    elif token_type == 'LAMBDA':
        return None
    elif token_type == 'NECK':
        return None

    raise Exception('failed to transform lark token')


def transform_lark_tree(lark_tree: lark.tree.Tree):
    tree_type = lark_tree.data
    tree_children = [transform(x) for x in lark_tree.children]
    tree_children = [x for x in tree_children if x]

    if tree_type == "expr" or tree_type == 'atom':
        return tree_children[0]
    elif tree_type == "app":
        return application(tree_children[0], tree_children[1])
    elif tree_type == 'lambda':
        return abstraction(tree_children[0], tree_children[1])

    raise Exception('failed to transform lark tree')


def transform(lark_object):
    if isinstance(lark_object, lark.lexer.Token):
        return transform_lark_token(lark_object)

    elif isinstance(lark_object, lark.tree.Tree):
        return transform_lark_tree(lark_object)

    raise Exception('Something went wrong transforming!')


GRAMMAR = open('lambda_grammar.lark').read()

LISP_PARSER = lark.Lark(GRAMMAR, parser='lalr',
                        lexer='standard',
                        lexer_callbacks={},
                        # transformer=LispTransformer(),
                        # increase speed:
                        propagate_positions=False,
                        maybe_placeholders=False
                        )

ast = LISP_PARSER.parse('(a b c)')

s = transform(ast)
print(s)
