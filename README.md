# devchell-final-bot
manager FreeBSD 



Bot: https://t.me/IzabellaDeployerBot


Ідея рішення полягає у наступному:

1. Бот виступає агентом для  aws і виконує розгортання та видалення віртуальної машини в хмарі . Команди vm_create та vm_destroy.

2. Коли відбувається розгортання віртуальної машини, через user_data завантажити скрипт patch_kde.sh та скрипт розгортання docker, docker-compose для розгортання на цільовій freebsd vm,  api server (код API в каталозі server-manager-api) з методами :


   - kde_patch - відпрацьовує запит команди vm_kde_patch

   - show_veshion - відпрацьовує запит команди vm_show_version

