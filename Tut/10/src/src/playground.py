def visitBinExpr(self, ctx, o):
    frame = o.frame
    trueLabel = frame.getNewLabel()
    falseLabel = frame.getNewLabel()
     endLabel = frame.getNewLabel()
      code = ''
       if (ctx.op == '&&'):
            expr1, expr1_type = ctx.e1.accept(self, o)
            code += (self.emit.emitIFFALSE(falseLabel, frame))
            expr2, expr2_type = ctx.e2.accept(self, o)
            code += (self.emit.emitIFFALSE(falseLabel, frame))
            code += (self.emit.emitPUSHICONST(1, frame))
            code += (self.emit.emitGOTO(endLabel, frame))

            code += (self.emit.emitLABEL(falseLabel, frame))
            code += (self.emit.emitPUSHICONST(0, frame))

        else:
            expr1, expr1_type = ctx.e1.accept(self, o)
            code += (self.emit.emitIFTRUE(trueLabel, frame))
            expr2, expr2_type = ctx.e2.accept(self, o)
            code += (self.emit.emitIFTRUE(trueLabel, frame))
            code += (self.emit.emitPUSHICONST(0, frame))
            code += (self.emit.emitGOTO(endLabel, frame))

            code += (self.emit.emitLABEL(trueLabel, frame))
            code += (self.emit.emitPUSHICONST(1, frame))

        code += (self.emit.emitLABEL(endLabel, frame))
        return code, BoolType()
