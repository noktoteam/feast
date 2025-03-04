from tests.integration.feature_repos.integration_test_repo_config import (
    IntegrationTestRepoConfig,
)
from tests.integration.feature_repos.universal.data_sources.spark_data_source_creator import (
    SparkDataSourceCreator,
)
from tests.integration.feature_repos.universal.data_sources.trino import (
    TrinoSourceCreator,
)

FULL_REPO_CONFIGS = [
    IntegrationTestRepoConfig(offline_store_creator=SparkDataSourceCreator),
    IntegrationTestRepoConfig(offline_store_creator=TrinoSourceCreator),
]
