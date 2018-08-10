#-*-coding:utf-8-*-
formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (True, False, False, True)
print formatter % (
    "I had this thing.",
    "That you could right up right.",
    "But it didn't print.",
    "So I said goodnight."
)
