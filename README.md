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


