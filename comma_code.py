spam = ["apples", "bananas", "tofu", "cats", "mice"]


def function(spam):
    spam.insert(len(spam) - 1, "and")
    sentence = ", ".join(spam)

    print("'{}'".format(sentence))


function(spam)
