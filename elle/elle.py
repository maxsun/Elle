''' An implementation of the Elle Language interpreter '''
# from lark import Lark, Transformer, v_args, lexer, tree
from typing import Set, Union, Iterable, Optional
import lark


class Token:
    '''Represents named data'''
    data: str
    type: Optional[str]

    def __init__(self, data: str, type: Optional[str] = None) -> None:
        self.data = data
        if type:
            self.type = type

    def __repr__(self) -> str:
        return '(%s %s)' % (self.type, self.data)


class Name(Token):
    '''Represents data which refers to something else'''
    data: str
    type = 'NAME'


class Literal(Token):
    '''Represents data which refers to its own content'''
    data: str
    type = 'LITERAL'


class Ambig(Token):
    '''Represents the unknown'''
    data: str
    type = 'AMBIG'


class Struct:
    '''Represents structured data'''
    members: Set[Union['Struct', Token]]

    def __init__(self, args: Iterable[Union['Struct', Token]]) -> None:
        self.members = set(args)

    def __repr__(self) -> str:
        return '(%s)' % ' '.join([str(x) for x in self.members])


def transform_lark_token(lark_token: lark.lexer.Token) -> Token:
    token_type = lark_token.type
    token_data = lark_token.value
    if token_type == 'ESCAPED_STRING':
        return Literal(token_data[1:-1])
    if token_type == 'NAME':
        return Name(token_data)

    raise Exception('failed to transform lark token')


def transform_lark_tree(lark_tree: lark.tree.Tree) -> Struct:
    return Struct([transform(x) for x in lark_tree.children])


def transform(lark_object):
    if isinstance(lark_object, lark.lexer.Token):
        return transform_lark_token(lark_object)

    elif isinstance(lark_object, lark.tree.Tree):
        return transform_lark_tree(lark_object)

    raise Exception('Something went wrong transforming!')


GRAMMAR = open('grammar.lark').read()

LISP_PARSER = lark.Lark(GRAMMAR, parser='lalr',
                        lexer='standard',
                        lexer_callbacks={},
                        # transformer=LispTransformer(),
                        # increase speed:
                        propagate_positions=False,
                        maybe_placeholders=False
                        )

ast = LISP_PARSER.parse('(a "b" (1 2))')
print(ast)

s = transform(ast)
