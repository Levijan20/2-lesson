from transliterate import translit
from num2words import num2words


print(translit('''Ladies and gentlemen, I'm 78 years old and I've finally had my once-in-a-lifetime 15 minutes of fame and I think it's mine. People also told me to make these next few minutes painfully shameful and take revenge on my enemies. Neither one nor the other will happen.
More than 3 years ago I moved to Novo-Novsk, but for the last 40 years I have been working on a new magnetic storage device. When I was 8...''', 'ru'))
print("78-",translit(num2words('78'),'ru'))
print("15-",translit(num2words('15'),"ru"))
print("3-",translit(num2words('3'),"ru"))
print("40-",translit(num2words('40'),"ru"))
print("8-",translit(num2words('8'),"ru"))

