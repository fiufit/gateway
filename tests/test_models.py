from src.models.metrics.get_metrics import GetMetricsRequest
from src.models.notifications.get_push import GetNotificationsRequest
from src.models.trainings.create_training_session import CreateTrainingSessionRequest
from src.models.trainings.get_training_sessions import GetTrainingSessionsRequest
from src.models.trainings.get_goals import GetGoalsRequest
from src.models.trainings.get_trainings import GetTrainingsRequest
from src.models.trainings.get_reviews import GetReviewsRequest
from src.models.users.get_users_request import GetUsersRequest
from src.models.users.get_users_request import GetClosestUsersRequest
from src.models.users.notify_request import NotifyLoginRequest


def test_get_metrics_request_to_query_string():
    get_metrics_request = GetMetricsRequest(
        type="type",
        subtype="subtype",
        fromDate="fromDate",
        to="to",
    )
    query_string = get_metrics_request.to_query_string()
    assert query_string == "type=type&subtype=subtype&from=fromDate&to=to"


def test_get_notifications_request_to_query_string():
    get_notifications_request = GetNotificationsRequest(
        read=True,
        limit=10,
        next_cursor="next_cursor",
    )
    query_string = get_notifications_request.to_query_string()
    assert query_string == "read=true&limit=10&next_cursor=next_cursor"


def test_create_training_request_to_query_string():
    create_training_request = CreateTrainingSessionRequest(
        training_id=1,
    )
    query_string = create_training_request.to_query_string()
    assert query_string == "training_id=1"


def test_get_training_sessions_request_to_query_string():
    get_training_sessions_request = GetTrainingSessionsRequest(
        training_id=1,
    )
    query_string = get_training_sessions_request.to_query_string()
    assert query_string == "training_id=1"


def test_get_goals_request_to_query_string():
    get_goals_request = GetGoalsRequest(
        type="type",
        subtype="subtype",
        deadline="deadline",
    )
    query_string = get_goals_request.to_query_string()
    assert query_string == "type=type&subtype=subtype&deadline=deadline"


def test_get_trainings_request_to_query_string():
    get_trainings_request = GetTrainingsRequest(
        name="training_name",
        description="training_description",
        difficulty="training_difficulty",
        trainer_id="trainer_id",
        user_id="user_id",
        tags=["tag1", "tag2"],
        min_duration=10,
        max_duration=20,
    )
    query_string = get_trainings_request.to_query_string()
    assert (
        query_string
        == """name=training_name&
        description=training_description&
        difficulty=training_difficulty&
        trainer_id=trainer_id&
        user_id=user_id&
        tags[]=tag1&
        tags[]=tag2&
        min_duration=10&
        max_duration=20""".replace(
            " ", ""
        ).replace(
            "\n", ""
        )
    )


def test_get_reviews_request_to_query_string():
    get_reviews_request = GetReviewsRequest(
        comment="comment",
        user_id="user_id",
        min_score=10,
        max_score=20,
    )
    query_string = get_reviews_request.to_query_string()
    assert query_string == "comment=comment&user_id=user_id&min_score=10&max_score=20"


def test_get_users_request_to_query_string():
    get_users_request = GetUsersRequest(
        name="name",
        nickname="nickname",
        is_verified=True,
        disabled=False,
        user_ids=["user_id1", "user_id2"],
    )
    query_string = get_users_request.to_query_string()
    assert (
        query_string
        == """name=name&
        nickname=nickname&
        is_verified=True&
        disabled=False&
        user_ids[]=user_id1&user_ids[]=user_id2""".replace(
            " ", ""
        ).replace(
            "\n", ""
        )
    )


def test_get_closest_users_request_to_query_string():
    get_closest_users_request = GetClosestUsersRequest(
        distance=10,
    )
    query_string = get_closest_users_request.to_query_string()
    assert query_string == "distance=10"


def test_notify_login_method_to_query_string():
    notify_login_request = NotifyLoginRequest(
        method="method",
    )
    query_string = notify_login_request.to_query_string()
    assert query_string == "method=method"
