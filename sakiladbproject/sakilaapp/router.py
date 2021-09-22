class SakilaRouter:
    """
    A router to control all database operations on models in the
    auth and contenttypes applications.
    """
    route_app_labels = {'sakilaapp',}


    def db_for_read(self, model, **hints):
        """
        Attempts to read sakilaapp models go to sakiladb.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'sakiladb'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write sakilaapp models go to sakiladb.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'sakiladb'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the sakilaapp app is
        involved.
        """
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the sakila app only appear in the
        'sakiladb' database.
        """
        if app_label in self.route_app_labels:
            return db == 'sakiladb'
        return None