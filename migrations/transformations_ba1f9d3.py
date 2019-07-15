from obj_model.migrate import MigrationWrapper


class NullWrapper(MigrationWrapper):

    # make a wrapper with prepare_existing_models & modify_migrated_models that do nothing
    def prepare_existing_models(self, migrator, existing_models):
        pass

    def modify_migrated_models(self, migrator, migrated_models):
        pass

transformations = NullWrapper()
