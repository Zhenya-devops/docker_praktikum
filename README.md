# docker_praktikum

## Структура дериктории
- Dockerfile
- main.py
- mongo
  - app.py
  - storage.py
- README.md
-requirements.txt
- resources
  - response.json

## Комментарии по файлам
- Dockerfile (**Dockerfile** - это файл, который сообщает Docker о том, как собирать образы, на основе которых создаются контейнеры.)
- main.py (Этот файл отвечает отвечает за запусе Flask проекта и его логику)
- mongo (Директория в которой хранятся файлы, которые отвечают за логику внесения и вывод данных в MongoDB)
  - app.py (логика программы)
  - storage.py (работа с MongoDB и структура базы)
- README.md
-requirements.txt (Файл, который отвечает какие модули потребуется скачать для Python (pip install [название модуля]))
- resources (Диркутория, которая отвечает за ресурсы в программе main.py)
  - response.json (JSON файл, который отвечает за вывод информации на сайт)

## Основные команды и комментарии к ним
- docker ps (список запущенных контейнеров)
  - docker ps -a (саисок всех контейнеров)
  - docker rm [id] (удалить контейнер)
  - docker rm $(docker ps -a -q) (удалить все контейнеры)
- docker images (список образов)
  - docker rmi [id] (удалить образ)
  - docker rmi $(docker images $(docker images -q) (удаление всех образов)
- docker build (создание образов)
  - docker build -t web-flask .
- docker run (запуск контейнера)
  - docker run --rm -d -p 27017:27017 mongo (запуск контейнера и при его завершении удалить(--rm), в посивном режиме (-d) и проброс портов (-p))
  - docker run --rm --name web-project -p 8081:8080 -e TZ=Europe/Minsk web-flask (переменная(-e))
  - docker run --rm --name web -p 8081:8080 -v web:/usr/src/app/resources web-flask (использование томов (-v))
  - docker run --rm --name web-project -p 8081:8080 -e TZ=Europe/Minsk -v /home/zhenya/dev/docker_project/resources:/usr/src/app/resources web-flask
  - docker volume create web (создание тома)
  - docker volume ls (просмотров томов)
  - 
- docker stop (остановка контейнера)
