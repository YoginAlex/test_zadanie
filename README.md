**Тестовое задание**

Реализовать django app , который можно подключать для любого класса модели django, который позволяет проголосовать за конкретный объект "нравится/не нравится".

**Приведено готовое web-приложение**
Нужный нам app - __likedislike__
- Подключаем в `settings.py`
- Делаем `syncdb`
- В urls.py - `url(r'^setlike/$', 'likedislike.views.setlike', name='setlike'),`
- В шаблоне подгружаем `{% load class_tag %}`
- В нужном файле модели делаем импорт - `from likedislike.decorator import likedecor`
- Нужную нам модель декорируем `@likedecor`
- В шаблоне пишем нечто подобное:
```
    {% if o.likedislike|length > 0 %}
        {% for ll in o.likedislike %}
            {% if ll.obj_id == o.id %}
            <a href="{% url setlike %}?model={{o|get_class}}&obj_id={{o.id}}">
                {{ll.like_dislike}}
            </a>
            {% endif %}
        {% endfor %}
    {% endif %}
```
