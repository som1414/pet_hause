class AttrDisplay:
    def gatherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append(f'{getattr(self, key)}')
        return attrs

    def __repr__(self):
        return f'{self.gatherAttrs()[0]}, г.{self.gatherAttrs()[1]}, статус "{self.gatherAttrs()[2]}"'