"""
Napisz algorytm obliczający entropię.
Porównaj entropie tekstu naturalnego z entropia kryptogramu.
"""
import math

txt = "A complete sentence must have, at minimum, three things: a subject, verb, and an object. The subject is " \
      "typically a noun or a pronoun. And, if there's a subject, there's bound to be a verb because all verbs need a " \
      "subject. Finally, the object of a sentence is the thing that's being acted upon by the subject. "

crp = "¬Õô0l¿ìÁÓÉù*Âô°lrsýò+>9K¢PË*ËúTÿõÔñaÞNÃjÿT~¡bB:a±ëÖ¿vï°ÄÕRKI,QV¼µX×.q®Á×§Po»D&Ð×ÊÙ[u¶Öë¸N" \
      "~¡k¤¼Uµ){@÷*AM4cæåMGõ§ÜÒ~ÊÌØõå(\ppàü YñR¿³yZ¸úàb.cZéFE`D¸Búê--äò;CÙ©ÈR1ÖZ¦þçh¶:ràt$9$Tì5ØE@óûpïuª" \
      "²êòT&rÚS»i-bíÄ/õôwÐNÂhÖ­¥KFÖ6¥ðNFù¯`bÒ¸æ1Y|¯¯Âÿ_VCHoµîz"


def calc_entropy(string):
    """Calculates the Shannon entropy of a string"""

    # get probability of chars in string
    prob = [float(string.count(c)) / len(string) for c in dict.fromkeys(list(string))]

    # calculate the entropy
    entropy = - sum([p * math.log(p) / math.log(2.0) for p in prob])

    return entropy


# print(calc_entropy(txt))
# print(calc_entropy(crp))
