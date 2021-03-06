# djangosakiladb

## Actor Model
### Query 1: (select all columms from Actor table)
```
>>> from sakilaapp.models import Actor
>>> qset = Actor.objects.all()
>>> print(qset.query)
SELECT "actor"."actor_id", "actor"."first_name", "actor"."last_name", "actor"."last_update" FROM "actor"

>>> print(qset.values())

<QuerySet [{'actor_id': 1, 'first_name': 'PENELOPE', 'last_name': 'GUINESS', 'last_update': datetime.datetime(2006, 2, 15, 4, 34, 33, tzinfo=<UTC>)}, {'actor_id': 2, 'first_name': 'NICK', 'last_name': 'WAHLBERG', 'last_update': datetime.datetime(2006, 2, 15, 4, 34, 33, tzinfo=<UTC>)}, {'actor_id': 3, 'first_name': 'ED', 'last_name': 'CHASE', 'last_update': datetime.datetime(2006, 2, 15, 4, 34, 33, tzinfo=<UTC>)}, {'actor_id': 4, 'first_name': 'JENNIFER', 'last_name': 'DAVIS', 'last_update': datetime.datetime(2006, 2, 15, 4, 34, 33, tzinfo=<UTC>)}, {'actor_id': 5, 'first_name': 'JOHNNY', 'last_name': 'LOLLOBRIGIDA', 'last_update': datetime.datetime(2006, 2, 15, 4, 34, 33, tzinfo=<UTC>)}, {'actor_id': 6, 'first_name': 'BETTE', 'last_name': 'NICHOLSON', 'last_update': datetime.datetime(2006, 2, 15, 4, 34, 33, tzinfo=<UTC>)}, {'actor_id': 7, 'first_name': 'GRACE', 'last_name': 'MOSTEL', 'last_update': datetime.datetime(2006, 2, 15, 4, 34, 33, tzinfo=<UTC>)}, {'actor_id': 8, 'first_name': 'MATTHEW', 'last_name': 'JOHANSSON', 'last_update': datetime.datetime(2006, 2, 15, 4, 34, 33, tzinfo=<UTC>)}, {'actor_id': 9, 'first_name': 'JOE', 'last_name': 'SWANK', 'last_update': datetime.datetime(2006, 2, 15, 4, 34, 33, tzinfo=<UTC>)}, {'actor_id': 10, 'first_name': 'CHRISTIAN', 'last_name': 'GABLE', 'last_update': datetime.datetime(2006, 2, 15, 4, 34, 33, tzinfo=<UTC>)}, {'actor_id': 11, 'first_name': 'ZERO', 'last_name': 'CAGE', 'last_update': datetime.datetime(2006, 2, 15, 4, 34, 33, tzinfo=<UTC>)}'...(remaining elements truncated)...']>

```

### Query 2: Limit the number of rows returned (Limit to 3 records)

```
>>> qset = Actor.objects.all()[:3] 
>>> print(qset.query)
SELECT "actor"."actor_id", "actor"."first_name", "actor"."last_name", "actor"."last_update" FROM "actor" LIMIT 3
>>> print(qset.values())
<QuerySet [{'actor_id': 1, 'first_name': 'PENELOPE', 'last_name': 'GUINESS', 'last_update': datetime.datetime(2006, 2, 15, 4, 34, 33, tzinfo=<UTC>)}, {'actor_id': 2, 'first_name': 'NICK', 'last_name': 'WAHLBERG', 'last_update': datetime.datetime(2006, 2, 15, 4, 34, 33, tzinfo=<UTC>)}, {'actor_id': 3, 'first_name': 'ED', 'last_name': 'CHASE', 'last_update': datetime.datetime(2006, 2, 15, 4, 34, 33, tzinfo=<UTC>)}]>
```
### Query 3: Limit the number of columns returned

```
>>> set = Actor.objects.all().values('first_name','last_name')
>>> print(qset.query)
SELECT "actor"."first_name", "actor"."last_name" FROM "actor"

>>> print(qset.values('first_name','last_name'))
<QuerySet [{'first_name': 'PENELOPE', 'last_name': 'GUINESS'}, {'first_name': 'NICK', 'last_name': 'WAHLBERG'}, {'first_name': 'ED', 'last_name': 'CHASE'}, {'first_name': 'JENNIFER', 'last_name': 'DAVIS'}, {'first_name': 'JOHNNY', 'last_name': 'LOLLOBRIGIDA'}, {'first_name': 'BETTE', 'last_name': 'NICHOLSON'}, {'first_name': 'GRACE', 'last_name': 'MOSTEL'}, {'first_name': 'MATTHEW', 'last_name': 'JOHANSSON'}, {'first_name': 'JOE', 'last_name': 'SWANK'}, {'first_name': 'CHRISTIAN', 'last_name': 'GABLE'}, {'first_name': 'ZERO', 'last_name': 'CAGE'}, {'first_name': 'KARL', 'last_name': 'BERRY'}, {'first_name': 'UMA', 'last_name': 'WOOD'}, {'first_name': 'VIVIEN', 'last_name': 'BERGEN'}, {'first_name': 'CUBA', 'last_name': 'OLIVIER'}, {'first_name': 'FRED', 'last_name': 'COSTNER'}, {'first_name': 'HELEN', 'last_name': 'VOIGHT'}, {'first_name': 'DAN', 'last_name': 'TORN'}, {'first_name': 'BOB', 'last_name': 'FAWCETT'}, {'first_name': 'LUCILLE', 'last_name': 'TRACY'}, '...(remaining elements truncated)...']>

```
### Query 4: Limit the number of columns and rows returned

```
>>> qset = Actor.objects.all().values('first_name','last_name')[:3]
>>> print(qset.query)
SELECT "actor"."first_name", "actor"."last_name" FROM "actor" LIMIT 3
>>> print(qset.values('first_name', 'last_name'))
<QuerySet [{'first_name': 'PENELOPE', 'last_name': 'GUINESS'}, {'first_name': 'NICK', 'last_name': 'WAHLBERG'}, {'first_name': 'ED', 'last_name': 'CHASE'}]>

```


