async def get_rank(exp):
        if exp <100:
            return int(1)
        if exp <400:
            return int(2)
        if exp <1000:
            return int(3)
        if exp <3000:
            return int(4)
        if exp <5000:
            return int(5)
        if exp <7500:
            return int(6)
        if exp <12000:
            return int(7)
        if exp <20000:
            return int(8)
        if exp <40000:
            return int(9)
        if exp <100000:
            return int(10)
        else:
            return int(11)