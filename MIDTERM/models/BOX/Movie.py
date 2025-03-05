class Movie:
    def __init__(self,MTitle,MType,dur,des):
        self.MTitle=MTitle
        self.MType=MType
        self.dur=dur
        self.des=des
    def __str__(self):
        return f"{self.MTitle}\t{self.MType}\t{self.dur}\t{self.des}"
