# #   idx1: Id
# #     expr1:Expr
# #     expr2:Expr
# #     expr3:Expr
# #     loop: Tuple[List[VarDecl],List[Stmt]]

# expr1
# continueLabel:
# startLabel:
#     if expr2 false -> endLabel
#     stmt
#     expr3
# goto startLabel

# breakLabel:
# endLabel:


# def visitFor(self, ctx, o):
#     frame = o.frame
#     expr1 = ctx.expr1.accept(self, o)
#     expr2 = ctx.expr2.accept(self, o)
#     expr3 = ctx.expr3.accept(self, o)

#     self.emit.printout(expr1)

#     frame.enterLoop()
#     startLabel = frame.getNewLabel()
#     endLabel = frame.getNewLabel()
#     continueLabel = frame.getContinueLabel()
#     breakLabel = frame.getBreakLabel()

#     self.emit.printout(self.emit.emitLABEL(continueLabel, frame))
#     self.emit.printout(self.emit.emitLABEL(startLabel, frame))

#     self.emit.printout(expr2)
#     self.emit.printout(self.emit.emitIFFALSE(endLabel, frame))

#     map(lambda x: x.accept(self, o), ctx.loop[0])
#     map(lambda x: x.accept(self, o), ctx.loop[1])

#     self.emit.printout(expr3)
#     self.emit.printout(self.emit.emitGOTO(startLabel, frame))

#     self.emit.printout(self.emit.emitLABEL(endLabel, frame))
#     self.emit.printout(self.emit.emitLABEL(breakLabel, frame))


# ----- 1


# def visitVarDecl(self, ctx, o):
#     if o.frame is None:
#         dir = self.emit.emitATTRIBUTE(ctx.name, ctx.typ, False)
#         self.emit.printout(dir)
#         return Symbol(ctx.name, ctx.typ, CName('MCClass'))
#     else:
#         idx = o.frame.getNewIndex()
#         dir = self.emit.emitVAR(idx, ctx.name, ctx.typ,
#                                 o.frame.getStartLabel(), o.frame.getEndLabel())
#         self.emit.printout(dir)
#         return Symbol(ctx.name, ctx.typ, Index(idx))


# ------2


# def visitId(self, ctx, o):
#     if o.isLeft:
#         for id in o.sym:
#             if id.name == ctx.name:
#                 if isinstance(id.value, Index):
#                     return self.emit.emitWRITEVAR(id.name, id.mtype, id.value.value, o.frame), id.mtype
#                 else:
#                     return self.emit.emitPUTSTATIC(id.value.value + '.' + id.name, id.mtype, o.frame), id.mtype
#     else:
#         for id in o.sym:
#             if id.name == ctx.name:
#                 if isinstance(id.value, Index):
#                     return self.emit.emitREADVAR(id.name, id.mtype, id.value.value, o.frame), id.mtype
#                 else:
#                     return self.emit.emitGETSTATIC(id.value.value + '.' + id.name, id.mtype, o.frame), id.mtype


# ------3


# def visitAssign(self, ctx, o):
#     codeR, typeR = ctx.rhs.accept(self, Access(o.frame, o.sym, False))
#     codeL, typeL = ctx.lhs.accept(self, Access(o.frame, o.sym, True))
#     self.emit.printout(codeR + codeL)


# ------4


# def visitIf(self, ctx, o):
#     exitLabel = o.frame.getNewLabel()
#     elseLabel = o.frame.getNewLabel() if ctx.estmt else None
#     exprCode, type = ctx.expr.accept(self, Access(o.frame, o.sym, False))

#     self.emit.printout(exprCode)
#     if elseLabel:
#         self.emit.printout(self.emit.emitIFFALSE(elseLabel, o.frame))
#         ctx.tstmt.accept(self, o)
#         self.emit.printout(self.emit.emitGOTO(exitLabel, o.frame))
#         self.emit.printout(self.emit.emitLABEL(elseLabel, o.frame))
#         ctx.estmt.accept(self, o)
#         self.emit.printout(self.emit.emitLABEL(exitLabel, o.frame))
#     else:
#         self.emit.printout(self.emit.emitIFFALSE(exitLabel, o.frame))
#         ctx.tstmt.accept(self, o)
#         self.emit.printout(self.emit.emitLABEL(exitLabel, o.frame))


# -----5


# def visitWhile(self, ctx, o):
#     frame = o.frame
#     sym = o.sym
#     frame.enterLoop()
#     beginLoop = frame.getNewLabel()
#     exitLoop = frame.getNewLabel()

#     # label to begin new iteration
#     self.emit.printout(self.emit.emitLABEL(beginLoop, frame))

#     # code for evaluate the condition expression
#     exprCode, typeExpr = ctx.expr.accept(self, Access(frame, sym, False))
#     self.emit.printout(exprCode)

#     # check if the condition is false, if false the go to the exit label
#     self.emit.printout(self.emit.emitIFFALSE(exitLoop, frame))

#     # visit the statement inside
#     ctx.stmt.accept(self, o)

#     # continue statement ??
#     self.emit.printout(self.emit.emitLABEL(frame.getContinueLabel(), frame))

#     # go back to the expression
#     self.emit.printout(self.emit.emitGOTO(beginLoop, frame))
#     self.emit.printout(self.emit.emitLABEL(exitLoop, frame))

#     # break statement
#     self.emit.printout(self.emit.emitLABEL(frame.getBreakLabel(), frame))

#     frame.exitLoop()


# -----6


# def visitFuncDecl(self, ctx, o):
#     sym = o.sym
#     frame = Frame(ctx.name, ctx.returnType)
#     frame.enterScope(False)
#     # directive for method

#     intype = []
#     dir = ""
#     for x in ctx.param:
#         idx = frame.getNewIndex()
#         dir += self.emit.emitVAR(idx, x.name, x.typ,
#                                  frame.getStartLabel(), frame.getEndLabel())
#         intype += [Symbol(x.name, x.typ, Index(idx))]

#     self.emit.printout(self.emit.emitMETHOD(ctx.name, MType(
#         [x.mtype for x in intype], ctx.returnType), True))
#     # directive for parameters and variables
#     self.emit.printout(dir)
#     reduce(lambda acc, ele: acc +
#            [ele.accept(self, SubBody(frame, acc[::-1]))], ctx.body[0], sym)

#     self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
#     [x.accept(self, SubBody(frame, sym[::-1])) for x in ctx.body[1]]
#     self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
#     self.emit.printout(self.emit.emitENDMETHOD(frame))

#     return Symbol(ctx.name, MType([x.mtype for x in intype], ctx.returnType), CName('MCClass'))
