import telebot
import os
import requests
import subprocess


API_TOKEN = os.environ.get('TOKEN_BOT')
GL_TOKEN = os.environ.get('GITLAB_TOKEN_BOT')
AWS_ACCESS_KEY_ID = os.environ.get('AWS_AK')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_AKK')

bot = telebot.TeleBot(API_TOKEN)
bot.remove_webhook()

headers = {
    'Content-type': 'application/json',
}

# @bot.message_handler(commands=['start'])
# def start_message(message):
#     first_name = message.from_user.first_name
#     bot.send_message(message.chat.id, 'Hi, {0}, lets deploy some staff!'.format(first_name))
#     bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAMaYZAsQ6emp4v5gSWzhW94nMUHYQ0AAvAFAALQhvsK4Fq2WYLRqo4iBA')


@bot.message_handler(content_types=['sticker'])
def start_message(message):
    bot.send_message(message.chat.id, 'ID стикера: ' + message.sticker.file_id)

@bot.message_handler(content_types=['text'])
def send_text(message):
    print(message.chat.id)

    first_name = message.from_user.first_name
    if message.text == 'help':
        HLP_MSG = 'deploy-stage - deploy application to STAGE envinronment\n' \
                  'deploy-prod - deploy application to PROD envinronment \n' \
                  'destroy - destroy application\n'\
                  'status - check status, get new commits, images , etc\n' \
                  'vm_create - створити віртуалку зі старою версією KDE з операційною системою FreeBSD;\n'\
                  'vm_show_version — показати встановлену версію FreeBSD та KDE;\n' \
                  'vm_kde_patch — запатчити KDE під FreeBSD;\n' \
                  'vm_destroy — видалити віртуалку.\n' \
                  'hi - wellcome message\n' \
                  'bye - goodbye message\n'
        bot.send_message(message.chat.id, HLP_MSG)
    elif message.text == 'hi':
        bot.send_message(message.chat.id, 'Hi, {0}, lets deploy some staff!'.format(first_name))
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAMaYZAsQ6emp4v5gSWzhW94nMUHYQ0AAvAFAALQhvsK4Fq2WYLRqo4iBA')
    elif message.text == 'bye':
        bot.send_message(message.chat.id, 'Bye, {0}, comeback and get more funny deploys!'.format(first_name) )
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAMcYZAsutkE6xbmqt0dTb1U84rGl-IAAhMGAALQhvsKAAHLy4pQ08HHIgQ')
    elif message.text == 'deploy-stage':
        bot.send_message(message.chat.id, '{0}, we start deploy to STAGE'.format(first_name) )
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAANSYZAxv5DoTDp95x_Hu-4J0tC6IesAAv4FAALQhvsKO4WCLDpZI3AiBA')
    elif message.text == 'deploy-prod':
        bot.send_message(message.chat.id, '{0}, we start deploy to PROD'.format(first_name) )
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAANUYZAyYUdlxgKCGJuaqTJCBrQ63vIAAgcGAALQhvsKmHa1rPaP4c8iBA')
        #response = requests.post('https://gitlab.com/api/v4/projects/31382958/ref/master/trigger/pipeline',
        #                         headers=headers, data=data)
        #bot.send_message(message.chat.id, 'Status {0} '.format(response))
    elif message.text == 'destroy':
        bot.send_message(message.chat.id, 'Bye, {0}, comeback and get more funny deploys!'.format(first_name) )
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAANQYZAxq_hk8j7RYbRyQne7nneo10MAAvgFAALQhvsKHseZIWpYyuAiBA')
    elif message.text == 'status':
        bot.send_message(message.chat.id, '{0}, we got new image for deploy'.format(first_name) )
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAANOYZAxkIf7yvbHBrsGW0o_Xu73GxQAAuwFAALQhvsKE2A2mx6WnBkiBA')
    elif message.text == 'vm_create':
        bot.send_message(message.chat.id, '{0}, go create new freebsd vm'.format(first_name) )
        bot.send_sticker(message.chat.id, 'CAACAgQAAxkBAAIC8GG0lcTD1GahDkrWa_JvrMn8RPq3AAJQAQACqCEhBrG98bXN6YSiIwQ')
        try:
          bot.send_message(message.chat.id, '{0}, start init creation VM '.format(first_name))
          result = subprocess.run(['terraform', 'init'], stdout=subprocess.PIPE)
          bot.send_message(message.chat.id, '{0}, end init creation VM - success '.format(first_name))
          bot.send_message(message.chat.id, '{0}, start creation VM '.format(first_name))
          result = subprocess.run(['terraform', 'apply', '-auto-approve'], stdout=subprocess.PIPE)
          bot.send_message(message.chat.id, '{0}, end creation VM - success '.format(first_name))
          print(result)
        except OSError as err:
          print("OS error: {0}".format(err))
        except (RuntimeError, TypeError, NameError):
          bot.send_message(message.chat.id, '{0}, creation process started with errors'.format(first_name) )
    elif message.text == 'vm_show_version':
        bot.send_message(message.chat.id, '{0}, let see wat we have'.format(first_name) )
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIC8mG0llFwXo906tcWpf3LJhA2IfcLAAJhBgAC0Ib7Cta8ASwdLTLCIwQ')
    elif message.text == 'vm_kde_patch':
        bot.send_message(message.chat.id, '{0}, lets patch KDE ..'.format(first_name) )
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIC9GG0lnKxAAEMz-c7WGWioEVXK6vSbAACKAYAAtCG-woIDzT9MQ4DDiME')
    elif message.text == 'vm_destroy':
        bot.send_message(message.chat.id, '{0}, lets destroy target vm'.format(first_name) )
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIC9mG0lo1hgb-z6aIEwM8uUcu8Ds_nAAIdBgAC0Ib7CqlkyVcb17KgIwQ')
        try:
          bot.send_message(message.chat.id, '{0}, start destroy VM '.format(first_name))
          result = subprocess.run(['terraform', 'destroy', '-auto-approve'], stdout=subprocess.PIPE)
          bot.send_message(message.chat.id, '{0}, end destroy VM - success '.format(first_name))
          print(result)
        except OSError as err:
          print("OS error: {0}".format(err))
        except (RuntimeError, TypeError, NameError) as err:
          bot.send_message(message.chat.id, '{0}, process destroy has errors'.format(first_name) )
          print("Runtime or Type  error: {0}".format(err))
    else:
        bot.send_message(message.chat.id, 'Easy, {0}, i dont know this command! Please check list of commands. Use command help'.format(first_name))
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAANDYZAw3acsnnm45iJ6lXu-d4qhS88AAu0FAALQhvsKhkdk35fp7K8iBA')

if __name__ == '__main__':
    bot.polling()