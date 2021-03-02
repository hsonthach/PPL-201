# ----- 1
#     def visitVarDecl(self, ctx, o):
#         if o.frame is None:
#             dir = self.emit.emitATTRIBUTE(ctx.name, ctx.typ, False)
#             self.emit.printout(dir)
#             return Symbol(ctx.name, ctx.typ, CName('MCClass'))
#         else:
#             idx = o.frame.getNewIndex()
#             dir = self.emit.emitVAR(idx, ctx.name, ctx.typ, o.frame.getStartLabel(), o.frame.getEndLabel())
#             self.emit.printout(dir)
#             return Symbol(ctx.name, ctx.typ, Index(idx))

# ------2
#     def visitId(self, ctx, o):
#         if o.isLeft:
#             for id in o.sym:
#                 if id.name == ctx.name:
#                     if isinstance(id.value, Index):
#                         return self.emit.emitWRITEVAR(id.name, id.mtype, id.value.value, o.frame), id.mtype
#                     else:
#                         return self.emit.emitPUTSTATIC(id.value.value + '.' + id.name, id.mtype, o.frame), id.mtype
#         else:
#             for id in o.sym:
#                 if id.name == ctx.name:
#                     if isinstance(id.value, Index):
#                         return self.emit.emitREADVAR(id.name, id.mtype, id.value.value, o.frame), id.mtype
#                     else:
#                         return self.emit.emitGETSTATIC(id.value.value + '.' + id.name, id.mtype, o.frame), id.mtype

# ------3
#     def visitAssign(self, ctx, o):
#         codeR, typeR = ctx.rhs.accept(self, Access(o.frame, o.sym, False))
#         codeL, typeL = ctx.lhs.accept(self, Access(o.frame, o.sym, True))
#         self.emit.printout(codeR + codeL)

# ------4
#     def visitIf(self, ctx, o):
#         exitLabel = o.frame.getNewLabel()
#         elseLabel = o.frame.getNewLabel() if ctx.estmt else None
#         exprCode, type = ctx.expr.accept(self, Access(o.frame,o.sym,False))
        
#         self.emit.printout(exprCode)
#         if elseLabel:
#             self.emit.printout(self.emit.emitIFFALSE(elseLabel, o.frame))
#             ctx.tstmt.accept(self, o)
#             self.emit.printout(self.emit.emitGOTO(exitLabel, o.frame))
#             self.emit.printout(self.emit.emitLABEL(elseLabel, o.frame))
#             ctx.estmt.accept(self, o)
#             self.emit.printout(self.emit.emitLABEL(exitLabel, o.frame))
#         else:
#             self.emit.printout(self.emit.emitIFFALSE(exitLabel, o.frame))
#             ctx.tstmt.accept(self, o)
#             self.emit.printout(self.emit.emitLABEL(exitLabel, o.frame))

# -----5
#     def visitWhile(self, ctx, o):
#         frame = o.frame
#         sym = o.sym
#         frame.enterLoop()
#         beginLoop = frame.getNewLabel()
#         exitLoop = frame.getNewLabel()
#         continueLabel = frame.getNewLabel()

        
#         # label to begin new iteration
#         self.emit.printout(self.emit.emitLABEL(beginLoop, frame))
        
#         # code for evaluate the condition expression
#         exprCode, typeExpr = ctx.expr.accept(self, Access(frame, sym, False))
#         self.emit.printout(exprCode)
        
#         # check if the condition is false, if false the go to the exit label
#         self.emit.printout(self.emit.emitIFFALSE(exitLoop, frame))
        
#         # visit the statement inside
#         ctx.stmt.accept(self, o)
        
#         # continue statement ??
#         self.emit.printout(self.emit.emitLABEL(continueLabel, frame))
#         #self.emit.printout(self.emit.emitLABEL(frame.getContinueLabel(), frame))
        
#         # go back to the expression
#         self.emit.printout(self.emit.emitGOTO(beginLoop, frame))
#         self.emit.printout(self.emit.emitLABEL(exitLoop, frame))
        
#         # break statement
#         self.emit.printout(self.emit.emitLABEL(frame.getBreakLabel(), frame))
        
#         frame.exitLoop()

#     def visitWhile(self,ctx,o):
#         frame= o.frame
#         # enter loop 
#         frame.enterLoop()
#         # exit loop
#         beginLabel = frame.getNewLabel() 
#         endLabel = frame.getNewLabel() 
#         continueLabel = frame.getContinueLabel()
#         breakLabel = frame.getBreakLabel()

#         self.emit.printout(self.emit.emitLABEL(beginLabel,frame))
#         # expr 
#         expr,type_expr = ctx.expr.accept(self,Access(frame,o.sym,False)) 

#         # put expr into stack
#         self.emit.printout(expr)

#         self.emit.printout(self.emit.emitIFFALSE(endLabel,frame))

#         ctx.stmt.accept(self,o) 

#         self.emit.printout(self.emit.emitLABEL(continueLabel,frame))

#         self.emit.printout(self.emit.emitGOTO(beginLabel,frame))

#         self.emit.printout(self.emit.emitLABEL(breakLabel,frame))

#         self.emit.printout(self.emit.emitLABEL(endLabel,frame))


#     def visitFor(ctx,o,frame):
#         self.emit.printout(self.emit.emitLABEL(endLabel,frame))
#         frame= o.frame
#         expr1,expr1_type = ctx.exrp1.accept(self,Access(frame,o.sym,False))
#         expr2,expr2_type = ctx.exrp2.accept(self,Access(frame,o.sym,False))
#         expr3,expr3_type = ctx.exrp3.accept(self,Access(frame,o.sym,False))
#         # enter loop 
#         frame.enterLoop()
#         beginLabel = frame.getNewLabel() 
#         endLabel = frame.getNewLabel() 
#         continueLabel = frame.getContinueLabel()
#         breakLabel = frame.getBreakLabel()
        
#         self.emit.printout(expr1)

#         self.emit.printout(self.emit.emitLABEL(beginLabel,frame))

#         self.emit.printout(expr2)

#         self.emit.printout(self.emit.emitIFFALSE(endLabel,frame))

#         ctx.stmt.accept(self,o)


#         self.emit.printout(self.emit.emitLABEL(continueLabel,frame))

#         self.emit.printout(expr3)

#         self.emit.printout(self.emit.emitGOTO(beginLabel))

#         self.emit.printout(self.emit.emitLABEL(continueLabel,frame))
#         self.emit.printout(self.emit.emitLABEL(endLabel,frame))




#     def visitFor(ctx,o,frame):

#     # continueLabel:
#     # expr3 


#     def visitBinExpr(self,ctx,o):
#         frame= o.frame
#         trueLabel = frame.getNewLabel() 
#         falseLabel = frame.getNewLabel() 
#         endLabel = frame.getNewLabel() 
#         code = ''
#         if (ctx.op == '&&'):
#             expr1,expr1_type = ctx.e1.accept(self,o)
#             code += (self.emit.emitIFFALSE(falseLabel,frame))
#             expr2,expr2_type = ctx.e2.accept(self,o)
#             code += (self.emit.emitIFFALSE(falseLabel,frame))
#             code += (self.emit.emitPUSHICONST(1,frame))
#             code += (self.emit.emitGOTO(endLabel,frame))

#             code += (self.emit.emitLABEL(falseLabel,frame))
#             code += (self.emit.emitPUSHICONST(0,frame))

#         else :
#             expr1,expr1_type = ctx.e1.accept(self,o)
#             code += (self.emit.emitIFTRUE(trueLabel,frame))
#             expr2,expr2_type = ctx.e2.accept(self,o)
#             code += (self.emit.emitIFTRUE(trueLabel,frame))
#             code += (self.emit.emitPUSHICONST(0,frame))
#             code += (self.emit.emitGOTO(endLabel,frame))

#             code += (self.emit.emitLABEL(trueLabel,frame))
#             code += (self.emit.emitPUSHICONST(1,frame))

#         code += (self.emit.emitLABEL(endLabel,frame))
#         return code , BoolType()




# -----6
#     def visitFuncDecl(self, ctx, o):
#         sym = o.sym
#         frame = Frame(ctx.name, ctx.returnType)
#         frame.enterScope(False)
#         # directive for method
        
#         intype = []
#         dir = ""
#         for x in ctx.param:
#             idx = frame.getNewIndex()
#             dir += self.emit.emitVAR(idx, x.name, x.typ, frame.getStartLabel(), frame.getEndLabel())
#             intype += [Symbol(x.name, x.typ, Index(idx))]
        
#         self.emit.printout(self.emit.emitMETHOD(ctx.name, MType([x.mtype for x in intype], ctx.returnType), True))
#         # directive for parameters and variables
#         self.emit.printout(dir)
#         reduce(lambda acc,ele: acc + [ele.accept(self,SubBody(frame, acc[::-1]))], ctx.body[0], sym)
        
#         self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
#         [x.accept(self, SubBody(frame, sym[::-1])) for x in ctx.body[1]]
#         self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
#         self.emit.printout(self.emit.emitENDMETHOD(frame))
        
#         return Symbol(ctx.name, MType([x.mtype for x in intype], ctx.returnType), CName('MCClass'))

from functools import reduce

def maximum(lst):
    reduce(lambda a,b: b if b>=a else a ,lst,lst[0])

lst = [3,9,7]
print(maximum(lst))