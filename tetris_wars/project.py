# ТЕТРИС ВОЙНИ:


# Какво ще включва:
#     - Класическият геймплей от 80те
#     - Някои от по-модерните иновации в играта


# Тук има нахвърляни разни идеи:
# https://github.com/m1trix/Tetris-Wars


# Първа стъпка - класиката:
#     - Класическите седем тетриминота, с които се играе;
#     - Параметрите на играта ще са конфигоруеми
# (например размерите на игралното поле);
#     - Въртене - падащото тетримино се върти на 90 градуса
# и в двете посоки, докато не удари натрупана купчина от
# тетриминота;
#     - Soft drop - падането става по-бързо;
#     - Hard drop - падането става веднага, т.е. тетриминото
# удря купчинката на момента и директно се фиксира там;
#     - Scoring система;
#     - Statistics система;
#     - Ще има абстрактен механизъм за рендериране, който ще
# работи еднакво добре с GUI или в конзола (като изключим FPS-а);
#     - Ще има абстрактен механизъм за key event-и.
# Той ще работи добре с GUI, но в конзолата не толкова.


# Втора стъпка - иновациите:
#     - Ghost тетримино - Това е "сянката" на падащото тетримино.
# Показава къде точно ще падне то;
#     - Гравитация - когато се счупи даден ред, тетриминотата
# могат да "пропаднат" надолу, ако има кухини;
#     - Hold на падащото тетримино - при натискане на бутона
# за задържане, текущото и задържаното си разменят местата.
# Дава гъвкавост;
#     - Опашка на предстоящите 4-5 тетриминотата;
#     - Easy spin - Когато тетриминото удари в купчинката,
# то не се "фиксира" веднага. Включва се брояч и преди да
# изтече времето, тетриминото може да бъде завъртяно или преместено,
# което води до нулиране на брояча. Това нулиране може да стане
# краен брой пъти.