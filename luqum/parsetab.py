
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftOR_OPleftAND_OPnonassocMINUSnonassocPLUSnonassocAPPROXnonassocBOOSTnonassocLPARENRPARENnonassocLBRACKETTORBRACKETnonassocPHRASEnonassocTERMTERM PHRASE APPROX BOOST MINUS SEPARATOR PLUS COLUMN LPAREN RPAREN LBRACKET RBRACKET AND_OP NOT OR_OP TOexpression : expression OR_OP expressionexpression : expression AND_OP expressionexpression : expression expressionunary_expression : PLUS unary_expressionunary_expression : MINUS unary_expressionunary_expression : NOT unary_expressionexpression : unary_expressionunary_expression : LPAREN expression RPARENunary_expression : LBRACKET phrase_or_term TO phrase_or_term RBRACKETunary_expression : TERM COLUMN unary_expressionunary_expression : PHRASEunary_expression : PHRASE APPROXexpression : expression BOOSTunary_expression : TERMunary_expression : TERM APPROXunary_expression : TOphrase_or_term : TERM\n                      | PHRASE'
    
_lr_action_items = {'RPAREN':([1,2,5,8,14,16,17,18,19,20,23,24,26,27,28,29,31,],[-7,-16,-14,-11,26,-15,-4,-5,-12,-6,-3,-13,-8,-10,-1,-2,-9,]),'COLUMN':([5,],[15,]),'APPROX':([5,8,],[16,19,]),'AND_OP':([1,2,5,8,10,14,16,17,18,19,20,23,24,26,27,28,29,31,],[-7,-16,-14,-11,22,22,-15,-4,-5,-12,-6,22,-13,-8,-10,22,-2,-9,]),'OR_OP':([1,2,5,8,10,14,16,17,18,19,20,23,24,26,27,28,29,31,],[-7,-16,-14,-11,21,21,-15,-4,-5,-12,-6,21,-13,-8,-10,-1,-2,-9,]),'LBRACKET':([0,1,2,4,5,6,7,8,9,10,14,15,16,17,18,19,20,21,22,23,24,26,27,28,29,31,],[3,-7,-16,3,-14,3,3,-11,3,3,3,3,-15,-4,-5,-12,-6,3,3,3,-13,-8,-10,3,3,-9,]),'$end':([1,2,5,8,10,16,17,18,19,20,23,24,26,27,28,29,31,],[-7,-16,-14,-11,0,-15,-4,-5,-12,-6,-3,-13,-8,-10,-1,-2,-9,]),'TERM':([0,1,2,3,4,5,6,7,8,9,10,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,31,],[5,-7,-16,13,5,-14,5,5,-11,5,5,5,5,-15,-4,-5,-12,-6,5,5,5,-13,13,-8,-10,5,5,-9,]),'RBRACKET':([11,13,30,],[-18,-17,31,]),'NOT':([0,1,2,4,5,6,7,8,9,10,14,15,16,17,18,19,20,21,22,23,24,26,27,28,29,31,],[9,-7,-16,9,-14,9,9,-11,9,9,9,9,-15,-4,-5,-12,-6,9,9,9,-13,-8,-10,-1,-2,-9,]),'PLUS':([0,1,2,4,5,6,7,8,9,10,14,15,16,17,18,19,20,21,22,23,24,26,27,28,29,31,],[6,-7,-16,6,-14,6,6,-11,6,6,6,6,-15,-4,-5,-12,-6,6,6,6,-13,-8,-10,6,6,-9,]),'MINUS':([0,1,2,4,5,6,7,8,9,10,14,15,16,17,18,19,20,21,22,23,24,26,27,28,29,31,],[7,-7,-16,7,-14,7,7,-11,7,7,7,7,-15,-4,-5,-12,-6,7,7,7,-13,-8,-10,7,7,-9,]),'PHRASE':([0,1,2,3,4,5,6,7,8,9,10,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,31,],[8,-7,-16,11,8,-14,8,8,-11,8,8,8,8,-15,-4,-5,-12,-6,8,8,8,-13,11,-8,-10,8,8,-9,]),'BOOST':([1,2,5,8,10,14,16,17,18,19,20,23,24,26,27,28,29,31,],[-7,-16,-14,-11,24,24,-15,-4,-5,-12,-6,24,-13,-8,-10,24,24,-9,]),'TO':([0,1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,26,27,28,29,31,],[2,-7,-16,2,-14,2,2,-11,2,2,-18,25,-17,2,2,-15,-4,-5,-12,-6,2,2,2,-13,-8,-10,2,2,-9,]),'LPAREN':([0,1,2,4,5,6,7,8,9,10,14,15,16,17,18,19,20,21,22,23,24,26,27,28,29,31,],[4,-7,-16,4,-14,4,4,-11,4,4,4,4,-15,-4,-5,-12,-6,4,4,4,-13,-8,-10,4,4,-9,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'phrase_or_term':([3,25,],[12,30,]),'expression':([0,4,10,14,21,22,23,28,29,],[10,14,23,23,28,29,23,23,23,]),'unary_expression':([0,4,6,7,9,10,14,15,21,22,23,28,29,],[1,1,17,18,20,1,1,27,1,1,1,1,1,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> expression OR_OP expression','expression',3,'p_expression_or','parser.py',155),
  ('expression -> expression AND_OP expression','expression',3,'p_expression_and','parser.py',160),
  ('expression -> expression expression','expression',2,'p_expression_implicit','parser.py',165),
  ('unary_expression -> PLUS unary_expression','unary_expression',2,'p_expression_plus','parser.py',170),
  ('unary_expression -> MINUS unary_expression','unary_expression',2,'p_expression_minus','parser.py',175),
  ('unary_expression -> NOT unary_expression','unary_expression',2,'p_expression_not','parser.py',180),
  ('expression -> unary_expression','expression',1,'p_expression_unary','parser.py',185),
  ('unary_expression -> LPAREN expression RPAREN','unary_expression',3,'p_grouping','parser.py',190),
  ('unary_expression -> LBRACKET phrase_or_term TO phrase_or_term RBRACKET','unary_expression',5,'p_range','parser.py',195),
  ('unary_expression -> TERM COLUMN unary_expression','unary_expression',3,'p_field_search','parser.py',202),
  ('unary_expression -> PHRASE','unary_expression',1,'p_quoting','parser.py',210),
  ('unary_expression -> PHRASE APPROX','unary_expression',2,'p_proximity','parser.py',215),
  ('expression -> expression BOOST','expression',2,'p_boosting','parser.py',220),
  ('unary_expression -> TERM','unary_expression',1,'p_terms','parser.py',225),
  ('unary_expression -> TERM APPROX','unary_expression',2,'p_fuzzy','parser.py',230),
  ('unary_expression -> TO','unary_expression',1,'p_to_as_term','parser.py',236),
  ('phrase_or_term -> TERM','phrase_or_term',1,'p_phrase_or_term','parser.py',241),
  ('phrase_or_term -> PHRASE','phrase_or_term',1,'p_phrase_or_term','parser.py',242),
]
