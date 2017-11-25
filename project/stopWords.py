from stop_words import get_stop_words

stop_words = get_stop_words('en')
stop_words = set(stop_words)
stop_words.add("I")
stop_words.add("A")
stop_words.add("m")
stop_words.add("t")
stop_words.add("It")
stop_words.add("If")
