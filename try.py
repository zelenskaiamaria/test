import requests
import json
import telebot
from telebot import types

url = "https://api.telegram.org/bot6978008935:AAG_EXJ_s_016tH3ckye4iXXQVOkh0j0CuY/sendpoll"






bot = telebot.TeleBot('6978008935:AAG_EXJ_s_016tH3ckye4iXXQVOkh0j0CuY')
@bot.message_handler(commands=['start'])
def main(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("GO")
    markup.add(button1)
    bot.send_message(message.chat.id,  'Привет! Я твой бот для подготовки к экзамену. Желаю тебе удачи в прохождении теста!'.format(message.from_user), reply_markup=markup)
    

@bot.message_handler(content_types=['text'])
def func(message):
        if(message.text == "GO"):
            bot.send_poll(message.chat.id, "If someone asks you what the best way of travelling from London to Paris is, you could suggest flying, taking the ferry or going through the Channel Tunnel. The 'Chunnel, as it is known, opened in 1994, and more than 200 million people (A1) ... it.", ['had used','were used', 'were using', 'are used', 'have used'], True, 'quiz',False, 4)


            bot.send_poll(message.chat.id, "Since 2000, pets have also been able to travel.The first plan to connect mainland Britain with France with a tunnel (A2) ... in 1802 by a French engineer. He wanted horse-drawn carriages to carry people through. Napoleon III later considered a tunnel, but thought it was too expensive. ", ['has presented','presented', 'was presented', 'was presending', 'had presented'], True, 'quiz',False, 2)


            bot.send_poll(message.chat.id, "He was right - the modern 'Chunnel' creators overspent by 80 per cent. The tunnels (two for trains and one for maintenance) (A3) ... six years to build and are 50.5 km long.", ['were taken','took', 'take', 'have been taking', 'are taking'], True, 'quiz',False, 1)


            bot.send_poll(message.chat.id, "High-speed trains (A4) ... since 2007.", ['ran','are run', 'are running', 'have been running', 'had run'], True, 'quiz',False, 3)


            bot.send_poll(message.chat.id, "It (A5) ... 35 minutes to travel the length of the Channel Tunnel.", ['was taking','has been taking', 'is taken', 'will be taken', 'takes'], True, 'quiz',False, 4)


            bot.send_poll(message.chat.id, "On a cheerier note, around 12 million roses (A6) ... through the tunnel every year for Valentine's Day.", ['deliver','have delivered', 'are delivering', 'are delivered', 'will deliver'], True, 'quiz',False, 3)


            bot.send_poll(message.chat.id, "As a child, Zack had eaten a wide variety of food and it wasn't until he started secondary school that he became addicted (A7) ... pizza.", ['with','for', 'to', 'in', 'on'], True, 'quiz',False, 2)


            bot.send_poll(message.chat.id, "American school meals have often been criticised for the large amount of fast food present (A8) ... the menu. At Zack's school, pizza was the star dish and he couldn't get enough of it.", ['at','on', 'in','to', 'with'], True, 'quiz',False, 1)


            bot.send_poll(message.chat.id, "Furthermore, there was only one thing he wanted to spend his pocket money on: slices of pizza. Naturally, Zack's family were worried about their son's diet was low (A9) ... vitamins.", ['in', 'at', 'with', 'for', 'by'], True, 'quiz',False, 0)


            bot.send_poll(message.chat.id, "Its aim was to encourage food addicts to beat their addictions with the help of a psychologist and nutritionist. It wasn't easy, but Zack finally demonstrated that he had given (A10) ... eating pizza", ['in', 'off', 'on', 'out', 'up' ], True, 'quiz',False, 4)


            bot.send_poll(message.chat.id, "(A11) Have you ever thought of visiting ... city which combines stunning beauty and a long history? York, the attractive, historical, walled city in North Yorkshire in England, can be ... excellent choice.", ['a, an ', '-,-', '-,the', '-,an','the,-'], True, 'quiz',False, 0)


            bot.send_poll(message.chat.id, "(A12) The Romans built York in AD 71. It has many remarkable sights to see. In ... actual fact, it takes you through a bustling market, dark, smokey houses and a busy wharf. They have all been recreated in .. accurate detail.", ['an,the','-,an', 'an,an', 'the,-', '-,-'], True, 'quiz',False, 4)


            bot.send_poll(message.chat.id, "(A13) As for a walk through York's historic city centre with its narrow medieval streets and modern shops, it'll definitely be a memorable experience. All in ... all, York, which still keeps its traditional style and cultural heritage down the centuries, is .. city to remember.", ['an,a', 'the,the', '-,a', '-,-','the,a'], True, 'quiz',False, 2)


            bot.send_poll(message.chat.id, "Укажите номер фрагмента в котором допущена ошибка.     (A14)We are well used to the influence (1) of changing trends in fashion and beauty(2)  and, although not everyone wishes to follow them(3),  it is undeniable(4) that a large number of people does(5).", ['1','2','3','4','5'], True, 'quiz',False, 4)


            bot.send_poll(message.chat.id, "(A15) Salt, which qualities(1)  have been known since prehistoric times(2), is used in almost every dish in the world(3)  and is admired by(4)  millions of people(5).", ['1','2','3','4','5'], True, 'quiz',False, 0)


            bot.send_poll(message.chat.id, "What is the secret of long life? Reducing calorie intake by 30 per cent is thought to lead to a longer lifespan, but for many, this can mean (A16) ... a starvation-like diet. ", ['going', 'leading','making','following', 'keeping'], True, 'quiz',False, 3)


            bot.send_poll(message.chat.id, "A recent (A17) ... of centenarians (долгожители) found, though, that many in the over-100 age group had led unhealthy lifestyles for a long period of their lives.", ['finding', 'search', 'study', 'proof', 'research'], True, 'quiz',False, 2)

            bot.send_message(5189636740, 'Выберите ответную реплику к предложенной реплике-стимулу.')

            bot.send_poll(message.chat.id, "(A18) It`s hard to convince others if you are not convinced yourself", ['I hope so.', 'I don`t mind it.', 'I couldn`t agree more.', 'I`d rather you didn`t.', 'Don`t mention it.'], True, 'quiz',False, 2)

            bot.send_message(5189636740, 'One of our eco-tourism packeges is the perfect(B1) ... (solve) for your upcoming holidays')


            bot.send_message(5189636740, 'The waiting lists are long so make sure your arrangements are made well in advance. Some eco-holidays are dedicated to protecting (B2) - (DANGER) species and helping them to reproduce.')


            bot.send_message(5189636740, 'There are many ways to experience(B3)...(forget) vacations. What about caring for whales and then windsurfing in your free time?')


            bot.send_message(5189636740, 'Or why not be a part of a group that(B4)...(regular) patrols the grounds of a Kenyan nature reserve?')


            bot.send_message(5189636740, 'Whatever your choice, our organisation will ensure that you don`t experience any major(B5)...(convenience).')


            bot.send_message(5189636740, 'Combine your passion for nature and travel, and do something to support our world! With us, it`s not just a holiday; It`s chance to take a (B6)...(responce) holiday.')

            bot.send_message(5189636740, 'Найдите лишнее слово')

            bot.send_message(5189636740, '(B7) The best thing about the job it is that you get to spend the whole summer outside, doing exciting ')

            bot.send_message(5189636740, '(B8) activities like kayaking and climbing. What could be most better than that? I feel certain you will')

            bot.send_message(5189636740, '(B9) agree that this is would be an enjoyable way to spend the summer holidays. On the other hand, it ')

            bot.send_message(5189636740, '(B10) can be quite stressful because you`re dealing with kids the whole time, and they can be such difficult.')

            bot.send_message(5189636740, '(B11) Clearly, when working with young children can be challenging from time to time. They don`t give')

            bot.send_message(5189636740, '(B12) you much time off, either. Staff who are expected to work upwards of fifty hours per week. So, there`s ')

            bot.send_message(5189636740, '(B13) virtually no downtime when you can just chill in the sunshine. Despite of these disadvantages, I would')

            bot.send_message(5189636740, '(B14) still recommend this job to you. You`d be far perfect for it, given that you`re so active and sporty, and')

            bot.send_message(5189636740, '(B15) you`d be a big hit with the kids. Let me to know if you want any contact names - I`m sure I could find')

            bot.send_message(5189636740, '(B16) some email addresses for you. Please don`t hesitate yourself to contact me if you require further help.')

            bot.send_message(5189636740, 'Переведите на английский язык фрагмент предложения, данный в скобках')

            bot.send_message(5189636740, '(B17) You have to (убедиться) sure that she`s not lying.')
            bot.send_message(5189636740, '(B18) Does Sally (похожа) after her grandfather in her talent for design?')
           
            bot.send_message(message.chat.id, f"ответы на В1,2,3,4: ||solution, endangered, unforgettable, regularly||", parse_mode='MarkdownV2')
            bot.send_message(message.chat.id, f"ответы на В 5,6,7,8: ||inconveniences, responsible, it, most||", parse_mode='MarkdownV2')
            bot.send_message(message.chat.id, f"ответы на В 9,10,11,12: ||is, such, when, who||", parse_mode='MarkdownV2')
            bot.send_message(message.chat.id, f"ответы на В 13,14,15,16: ||of, far, to, yourself||", parse_mode='MarkdownV2')
            bot.send_message(message.chat.id, f"ответы на В 17,18: ||make, take||", parse_mode='MarkdownV2')



bot.polling(non_stop=True)
