''' A lambda calculus interpreter '''
# from lark import Lark, Transformer, v_args, lexer, tree
from typing import Set, Union, Iterable, Optional, List
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

    def pretty(self, indent=0) -> str:
        return self.__repr__()

    def interpret(self, context: 'Abstraction') -> str:
        raise NotImplementedError


class Name(Token):
    '''Represents data which refers to something else'''
    data: str
    type = 'NAME'

    def interpret(self, context: 'Abstraction') -> str:
        if self.data == 'apply':
            print('- Interpreting Application')
            # print(context)
        if self.data == 'map':
            print('- Interpreting Map')
            print(context)
        return "LOOKUP: %s" % self.data


class Literal(Token):
    '''Represents data which refers to its own content'''
    data: str
    type = 'LITERAL'

    def interpret(self, context: 'Abstraction') -> str:
        return self.data


class Ambig(Token):
    '''Represents the unknown'''
    data: str
    type = 'AMBIG'

    def __repr__(self) -> str:
        return '?'

    def interpret(self) -> str:
        return '?'


class Abstraction:
    '''Represents something abstract??'''
    args: List[Union['Abstraction', Token]]

    def __init__(self, args: Iterable[Union['Abstraction', Token]]) -> None:
        self.args = list(args)

    def __repr__(self) -> str:
        return '(%s)' % ' '.join([str(x) for x in self.args])

    def pretty(self, indent=1) -> str:
        indent_txt = '    ' * indent
        return '(\n%s\n%s)' % (
            '\n'.join([indent_txt + x.pretty(indent + 1) for x in self.args]),
            indent_txt[:-4])

    def interpret(self, context: 'Abstraction') -> str:
        ctx = self
        # union with current context
        return '(%s)' % ' '.join([x.interpret(ctx) for x in self.args])



def transform_lark_token(lark_token: lark.lexer.Token) -> Token:
    token_type = lark_token.type
    token_data = lark_token.value
    if token_type == 'LITERAL':
        return Literal(token_data[1:-1])
    if token_type == 'NAME':
        return Name(token_data)
    if token_type == 'AMBIG':
        return Ambig(*token_data)

    raise Exception('failed to transform lark token')


def transform_lark_tree(lark_tree: lark.tree.Tree) -> Abstraction:
    return Abstraction([transform(x) for x in lark_tree.children])


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


def parse(text) -> Abstraction:
    ast = LISP_PARSER.parse(text)
    struct = transform(ast)
    return struct


def interpret(struct: Union[Abstraction, Token]) -> str:
    # if isinstance(struct, Abstraction):
    #     # return '(%s)' % ' '.join([interpret(x) for x in struct.args])
    # elif isinstance(struct, Token):
    #     return struct.interpret()
    return struct.interpret(Abstraction([]))


S = parse('''
    (apply
        (map 
            ("arg" "x")
            ("body" "x"))
        "'ABC'")
''')

# print('=== AST ===')
# print(S.pretty())
# print('\n=== INTERPRETING ===')

out = interpret(S)
print(out)

