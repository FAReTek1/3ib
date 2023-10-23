class Style:
    def __init__(self, **kwargs):
        self.__dict__["styling"] = kwargs

    def __getattr__(self, item):
        if self.__dict__.get("styling").get(item) is None:
            if self is DefaultStyle:
                return None
            return DefaultStyle.__getattr__(item)
        return self.__dict__.get("styling").get(item)

    def __setattr__(self, key, value):
        self.__dict__["styling"][key] = value

    def __str__(self):
        return f"""Style(
{self.styling}
)"""


PointStyle = Style(
    thickness=5,
    fill="black",
)

LineStyle = Style(
    thickness=5,
    fill="black",
    cap="round",
    join="round",
)
DefaultStyle = Style(
    thickness=5,
    fill="black",
    cap="round",
    join="round",
    outline="#000000",
    height=1,
    width=1,
)
