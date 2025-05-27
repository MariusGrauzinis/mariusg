class StringUtils:
    @classmethod
    def reverse(cls, s: str) -> str:
        return ''.join(reversed(s))


print(StringUtils.reverse("Hello, world!"))
