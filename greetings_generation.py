import random
from typing import Mapping, Sequence

GREETINGS = {
    "С Новым годом,": [
        "с новым счастьем!",
        "365 новых дней. 365 новых шансов!",
        "наслаждайтесь каждым его моментом!",
        "примите мои искренние поздравления!",
        "годом Кролика!",
        "новый старт начинается снова!",
        "и пусть самые лучшие сюрпризы будут у вас впереди!",
    ],
    "Я желаю": [
        "много новых достижений, крепкого здоровья и любви, пусть "
        "задуманное сбудется,",
        "чтобы этот год подарил много поводов для"
        " радости и счастливых моментов,",
        "чтобы будущий год принес столько радостей, сколько дней в году, и "
        "чтобы каждый день дарил вам улыбку и частичку добра,",
        "вам прекрасного года, полного здоровья и благополучия,",
        "чтобы Кролик принес в вашу семью любовь, нежность, взаимопонимание и "
        "счастье,",
        "всем в Новом году быть здоровыми, красивыми, любимыми и успешными,",
        "чтобы сбылось все то, что вы пожелали. Все цели были достигнуты, а "
        "планы перевыполнены,",
    ],
    "и пусть": [
        "Новый год принесет много радостных и счастливых дней.",
        "каждый новый миг наступающего года приносит в дом счастье, везение, "
        "уют и теплоту!",
        "все, что мы планировали, обязательно сбудется!",
        "наступающий год станет самым плодотворным годом в вашей жизни!",
        "год будет полон ярких красок, приятных впечатлений и радостных "
        "событий!",
        "этот год будет ВАШИМ годом!",
        "Новый год принесет все, о чем вы мечтаете, и немного больше!",
    ],
}


def generate_greeting(greetings: Mapping[str, Sequence[str]]) -> str:
    result = ""

    for prefix, suffixes in greetings.items():
        result += f"{prefix} {random.choice(suffixes)} "

    return result
