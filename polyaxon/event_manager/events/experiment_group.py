from event_manager.event import Event, Attribute

EXPERIMENT_GROUP_CREATED = 'experiment_group.created'
EXPERIMENT_GROUP_UPDATED = 'experiment_group.updated'
EXPERIMENT_GROUP_DELETED = 'experiment_group.deleted'
EXPERIMENT_GROUP_VIEWED = 'experiment_group.viewed'
EXPERIMENT_GROUP_STOPPED = 'experiment_group.stopped'
EXPERIMENT_GROUP_RESUMED = 'experiment_group.resumed'
EXPERIMENT_GROUP_FINISHED = 'experiment_group.finished'
EXPERIMENT_GROUP_EXPERIMENTS = 'experiment_group.experiments'
EXPERIMENT_GROUP_ITERATION = 'experiment_group.iteration'
EXPERIMENT_GROUP_RANDOM = 'experiment_group.random'
EXPERIMENT_GROUP_GRID = 'experiment_group.grid'
EXPERIMENT_GROUP_HYPERBAND = 'experiment_group.hyperband'
EXPERIMENT_GROUP_BO = 'experiment_group.bo'


class ExperimentGroupCreatedEvent(Event):
    type = EXPERIMENT_GROUP_CREATED
    attributes = (
        Attribute('id'),
        Attribute('sequence'),
        Attribute('project.id'),
        Attribute('project.user.id'),
        Attribute('user.id'),
        Attribute('created_at', is_datetime=True),
        Attribute('concurrency'),
        Attribute('search_algorithm'),
        Attribute('has_early_stopping', attr_type=bool),
        Attribute('has_description', attr_type=bool),
        Attribute('is_resume', attr_type=bool),
        Attribute('is_restart', attr_type=bool),
    )


class ExperimentGroupUpdatedEvent(Event):
    type = EXPERIMENT_GROUP_UPDATED
    attributes = (
        Attribute('id'),
        Attribute('sequence'),
        Attribute('project.id'),
        Attribute('project.user.id'),
        Attribute('user.id'),
        Attribute('actor_id'),
        Attribute('updated_at', is_datetime=True),
        Attribute('concurrency'),
        Attribute('search_algorithm'),
        Attribute('has_early_stopping', attr_type=bool),
        Attribute('has_description', attr_type=bool),
        Attribute('is_resume', attr_type=bool),
        Attribute('is_restart', attr_type=bool),
        Attribute('status'),
    )


class ExperimentGroupDeletedEvent(Event):
    type = EXPERIMENT_GROUP_DELETED
    attributes = (
        Attribute('id'),
        Attribute('sequence'),
        Attribute('project.id'),
        Attribute('project.user.id'),
        Attribute('user.id'),
        Attribute('actor_id'),
        Attribute('updated_at', is_datetime=True),
        Attribute('concurrency'),
        Attribute('search_algorithm'),
        Attribute('has_early_stopping', attr_type=bool),
        Attribute('has_description', attr_type=bool),
        Attribute('is_resume', attr_type=bool),
        Attribute('is_restart', attr_type=bool),
        Attribute('status'),
    )


class ExperimentGroupViewedEvent(Event):
    type = EXPERIMENT_GROUP_VIEWED
    attributes = (
        Attribute('id'),
        Attribute('sequence'),
        Attribute('project.id'),
        Attribute('project.user.id'),
        Attribute('user.id'),
        Attribute('actor_id'),
        Attribute('updated_at', is_datetime=True),
        Attribute('concurrency'),
        Attribute('search_algorithm'),
        Attribute('has_early_stopping', attr_type=bool),
        Attribute('has_description', attr_type=bool),
        Attribute('is_resume', attr_type=bool),
        Attribute('is_restart', attr_type=bool),
        Attribute('status'),
    )


class ExperimentGroupStoppedEvent(Event):
    type = EXPERIMENT_GROUP_STOPPED
    attributes = (
        Attribute('id'),
        Attribute('sequence'),
        Attribute('project.id'),
        Attribute('project.user.id'),
        Attribute('user.id'),
        Attribute('actor_id'),
        Attribute('updated_at', is_datetime=True),
        Attribute('concurrency'),
        Attribute('search_algorithm'),
        Attribute('has_early_stopping', attr_type=bool),
        Attribute('has_description', attr_type=bool),
        Attribute('is_resume', attr_type=bool),
        Attribute('is_restart', attr_type=bool),
        Attribute('status'),
    )


class ExperimentGroupResumedEvent(Event):
    type = EXPERIMENT_GROUP_RESUMED
    attributes = (
        Attribute('id'),
        Attribute('sequence'),
        Attribute('project.id'),
        Attribute('project.user.id'),
        Attribute('user.id'),
        Attribute('actor_id'),
        Attribute('updated_at', is_datetime=True),
        Attribute('concurrency'),
        Attribute('search_algorithm'),
        Attribute('has_early_stopping', attr_type=bool),
        Attribute('has_description', attr_type=bool),
        Attribute('is_resume', attr_type=bool),
        Attribute('is_restart', attr_type=bool),
        Attribute('status'),
    )


class ExperimentGroupFinishedEvent(Event):
    type = EXPERIMENT_GROUP_FINISHED
    attributes = (
        Attribute('id'),
        Attribute('sequence'),
        Attribute('project.id'),
        Attribute('project.user.id'),
        Attribute('user.id'),
        Attribute('actor_id'),
        Attribute('updated_at', is_datetime=True),
        Attribute('concurrency'),
        Attribute('search_algorithm'),
        Attribute('has_early_stopping', attr_type=bool),
        Attribute('has_description', attr_type=bool),
        Attribute('is_resume', attr_type=bool),
        Attribute('is_restart', attr_type=bool),
        Attribute('status'),
    )


class ExperimentGroupIterationEvent(Event):
    type = EXPERIMENT_GROUP_ITERATION
    attributes = (
        Attribute('id'),
        Attribute('sequence'),
        Attribute('project.id'),
        Attribute('project.user.id'),
        Attribute('user.id'),
        Attribute('actor_id'),
        Attribute('updated_at', is_datetime=True),
        Attribute('concurrency'),
        Attribute('search_algorithm'),
        Attribute('has_early_stopping', attr_type=bool),
        Attribute('has_description', attr_type=bool),
        Attribute('is_resume', attr_type=bool),
        Attribute('is_restart', attr_type=bool),
        Attribute('status'),
    )


class ExperimentGroupExperimentsViewedEvent(Event):
    type = EXPERIMENT_GROUP_EXPERIMENTS
    attributes = (
        Attribute('id'),
        Attribute('sequence'),
        Attribute('project.id'),
        Attribute('project.user.id'),
        Attribute('user.id'),
        Attribute('actor_id'),
        Attribute('updated_at', is_datetime=True),
        Attribute('concurrency'),
        Attribute('search_algorithm'),
        Attribute('has_early_stopping', attr_type=bool),
        Attribute('has_description', attr_type=bool),
        Attribute('is_resume', attr_type=bool),
        Attribute('is_restart', attr_type=bool),
        Attribute('status'),
    )


class ExperimentGroupRandomEvent(Event):
    type = EXPERIMENT_GROUP_RANDOM


class ExperimentGroupGridEvent(Event):
    type = EXPERIMENT_GROUP_GRID


class ExperimentGroupHyperbandEvent(Event):
    type = EXPERIMENT_GROUP_HYPERBAND


class ExperimentGroupBOEvent(Event):
    type = EXPERIMENT_GROUP_BO