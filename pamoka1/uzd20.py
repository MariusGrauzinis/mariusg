class Matematika:
    @staticmethod
    def faktorialas(n):
        if n < 0:
            raise ValueError("Faktorialas nėra apibrėžtas neigiamiems skaičiams.")
        if n == 0:
            return 1
        return n * Matematika.faktorialas(n - 1)
    