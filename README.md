# djangosakiladb

## Actor Model
### Query 1: (select all columms from Actor table)
SELECT "actor"."actor_id", "actor"."first_name", "actor"."last_name", "actor"."last_update" FROM "actor"

>>> from sakilaapp.models import Actor 
>>> qset = Actor.objects.all()
>>> print(qset.query)
SELECT "actor"."actor_id", "actor"."first_name", "actor"."last_name", "actor"."last_update" FROM "actor"