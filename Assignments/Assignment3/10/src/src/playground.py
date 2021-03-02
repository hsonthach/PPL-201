def visitBinExpr(self, ctx, o):
    code = self.emit.emitPUSHICONST(ctx.value, o.frame)
    return code, IntType()
