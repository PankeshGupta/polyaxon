from django.test import override_settings

from experiment_groups.models import ExperimentGroup
from experiment_groups.serializers import ExperimentGroupDetailSerializer, ExperimentGroupSerializer
from factories.factory_experiment_groups import ExperimentGroupFactory
from tests.utils import BaseTest


@override_settings(DEPLOY_RUNNER=False)
class TestExperimentGroupSerializer(BaseTest):
    serializer_class = ExperimentGroupSerializer
    model_class = ExperimentGroup
    factory_class = ExperimentGroupFactory
    expected_keys = {
        'uuid', 'sequence', 'unique_name', 'description', 'project', 'project_name',
        'user', 'created_at', 'updated_at', 'concurrency', 'num_experiments', 'last_status',
        'search_algorithm', 'num_pending_experiments', 'num_running_experiments', }

    def setUp(self):
        super().setUp()
        self.obj1 = self.factory_class()
        self.obj2 = self.factory_class()

    def test_serialize_one(self):
        data = self.serializer_class(self.obj1).data

        assert set(data.keys()) == self.expected_keys
        data.pop('created_at')
        data.pop('updated_at')
        assert data.pop('uuid') == self.obj1.uuid.hex
        assert data.pop('project') == self.obj1.project.uuid.hex
        assert data.pop('project_name') == self.obj1.project.unique_name
        assert data.pop('user') == self.obj1.user.username
        assert data.pop('num_experiments') == self.obj1.experiments.count()
        assert data.pop('num_pending_experiments') == self.obj1.pending_experiments.count()
        assert data.pop('num_running_experiments') == self.obj1.running_experiments.count()
        assert data.pop('last_status') == self.obj1.last_status
        assert data.pop('search_algorithm') == self.obj1.search_algorithm

        for k, v in data.items():
            assert getattr(self.obj1, k) == v

    def test_serialize_many(self):
        data = self.serializer_class(self.model_class.objects.all(), many=True).data
        assert len(data) == 2
        for d in data:
            assert set(d.keys()) == self.expected_keys


@override_settings(DEPLOY_RUNNER=False)
class TestExperimentGroupDetailSerializer(BaseTest):
    serializer_class = ExperimentGroupDetailSerializer
    model_class = ExperimentGroup
    factory_class = ExperimentGroupFactory
    expected_keys = {
        'uuid', 'sequence', 'unique_name', 'description', 'content',
        'params', 'project', 'project_name', 'user',
        'created_at', 'updated_at', 'started_at', 'finished_at',
        'concurrency', 'num_experiments', 'last_status', 'current_iteration', 'search_algorithm',
        'num_pending_experiments', 'num_running_experiments', 'num_scheduled_experiments',
        'num_succeeded_experiments', 'num_failed_experiments', 'num_stopped_experiments'}

    def setUp(self):
        super().setUp()
        self.obj1 = self.factory_class()
        self.obj2 = self.factory_class()

    def test_serialize_one(self):
        data = self.serializer_class(self.obj1).data

        assert set(data.keys()) == self.expected_keys
        data.pop('created_at')
        data.pop('updated_at')
        data.pop('started_at')
        data.pop('finished_at')
        assert data.pop('uuid') == self.obj1.uuid.hex
        assert data.pop('project') == self.obj1.project.uuid.hex
        assert data.pop('project_name') == self.obj1.project.unique_name
        assert data.pop('user') == self.obj1.user.username
        assert data.pop('num_experiments') == self.obj1.experiments.count()
        assert data.pop('num_pending_experiments') == self.obj1.pending_experiments.count()
        assert data.pop('num_running_experiments') == self.obj1.running_experiments.count()
        assert data.pop('num_scheduled_experiments') == self.obj1.scheduled_experiments.count()
        assert data.pop('num_succeeded_experiments') == self.obj1.succeeded_experiments.count()
        assert data.pop('num_failed_experiments') == self.obj1.failed_experiments.count()
        assert data.pop('num_stopped_experiments') == self.obj1.stopped_experiments.count()
        assert data.pop('last_status') == self.obj1.last_status
        assert data.pop('current_iteration') == self.obj1.current_iteration
        assert data.pop('search_algorithm') == self.obj1.search_algorithm

        for k, v in data.items():
            assert getattr(self.obj1, k) == v

    def test_serialize_many(self):
        data = self.serializer_class(self.model_class.objects.all(), many=True).data
        assert len(data) == 2
        for d in data:
            assert set(d.keys()) == self.expected_keys
