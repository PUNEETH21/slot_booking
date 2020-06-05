import datetime
import pytest
from typing import List
from slot_booking.constants.constants import DAY_CHOICES
from slot_booking.dtos.dtos import (
    TimeSlotDto, PreviousSlotDto, PreviousSlotsDto, 
    WashingMachineSlotsDto, UpcomingSlotDto, UserAuthTokensDto,
    WashingMachineDetailsDto
)
from slot_booking.models.user import User

pytestmark = pytest.mark.django_db
@pytest.fixture
def user():
    User.objects.bulk_create([
        User(name='u1', username='username', password="password"),
        User(name='u2', username='username1', password="password"),
        User(name='u3', username='username2', password="password"),
        ])
    users_objects = User.objects.all()
    return users_objects


@pytest.fixture()
def user_auth_tokens_dto():
    user_auth_tokens_dto = UserAuthTokensDto(
                user_id = 1,
                access_token = 'edsas34t43w',
                refresh_token = 'adsfalfj343',
                expires_in = "2020-05-24",
                )

    return user_auth_tokens_dto


@pytest.fixture()
def washing_machine_slots_dtos():
    washing_machine_slots_dtos = [
            TimeSlotDto(
                start_time="19:22:46.810366",
                end_time="20:22:46.810366",
            ),
            TimeSlotDto(
                start_time="20:22:46.810366",
                end_time="21:22:46.810366",
            )
    ]

    return washing_machine_slots_dtos

@pytest.fixture()
def previous_slots_dtos():
    previous_slots_dtos = [
            PreviousSlotDto(
                date = "29-05-2020",
                start_time = "19:22:46.810366",
                end_time = "20:22:46.810366",
                washing_machine_id = "wm1"
            ),
            PreviousSlotDto(
                date = "28-05-2020",
                start_time = "19:22:46.810366",
                end_time = "20:22:46.810366",
                washing_machine_id = "wm2"
            )
        ]

    return previous_slots_dtos

@pytest.fixture()
def upcoming_slots_dtos():
    upcoming_slots_dtos = [
            UpcomingSlotDto(
                date = "2020-08-10",
                start_time = "19:22:46.810366",
                end_time = "20:22:46.810366",
                washing_machine_id = "wm1"
            ),
            UpcomingSlotDto(
                date = "2020-08-18",
                start_time = "19:22:46.810366",
                end_time = "20:22:46.810366",
                washing_machine_id = "wm2"
            )
        ]

    return upcoming_slots_dtos

@pytest.fixture()
def washing_machine_details_dto():
    washing_machine_details_dto = WashingMachineDetailsDto(
        washing_machine_id = "wm1",
        is_active = True
    )

    return washing_machine_details_dto

'''

@pytest.fixture()
def available_slots_dto():
    available_slots_dto = AvailableSlotDto(
            date="2019-05-27",
            start_time="19:22:46.810366",
            end_time="20:22:46.810366",
            is_available =False
    )

    return available_slots_dto



@pytest.fixture()
def available_slots_dtos():
    available_slots_dtos = AvailableSlotsDto(
        [
            AvailableSlotDto(
                date="2019-05-27",
                start_time=["19:22:46.810366"],
                end_time=["20:22:46.810366"],
                is_available =[True]
            ),
            AvailableSlotDto(
                date="2019-05-27",
                start_time=["20:22:46.810366"],
                end_time=["21:22:46.810366"],
                is_available =[False]
            )
        ]
    )

    return available_slots_dtos



@pytest.fixture()
def user_dto():
    user_dto = UserDto(
        user_id=1,
        name="rohit",
        profile_pic="https://www.google.com"
    )
    return user_dto


@pytest.fixture()
def user_dtos():
    user_dtos = [UserDto(
        user_id=1,
        name="rohit",
        profile_pic="https://www.google.com"
    ),
    UserDto(
        user_id=2,
        name="rana",
        profile_pic="https://www.google.com"
    )]
    return user_dtos


@pytest.fixture()
def post_dto():
    post_dto = PostDto(
        post_id=1,
        content='yah',
        posted_at="2019-05-21 20:22:46.810366",
        posted_by_id=1,
    )
    return post_dto

@pytest.fixture()
def post_dtos():
    post_dtos = [
        PostDto(
            post_id=1,
            content='yah',
            posted_at="2019-05-21 20:22:46.810366",
            posted_by_id=1,
        ),
        PostDto(
            post_id=2,
            content='yah',
            posted_at="2019-05-21 20:22:46.810366",
            posted_by_id=1,
        )
    ]

    return post_dtos


@pytest.fixture()
def comment_dto():
    comment_dto = CommentDto(
        comment_id=2,
        post_id=2,
        commented_by_id=1,
        commented_at="2019-05-21 20:22:46.810366",
        parent_comment_id=None,
        content="usrt"
    )
    return comment_dto

@pytest.fixture()
def comment_dtos():
    comment_dtos =[
         CommentDto(
            comment_id=1,
            post_id=1,
            commented_by_id=1,
            commented_at="2019-05-21 20:22:46.810366",
            parent_comment_id=None,
            content="usrt"
        ),
         CommentDto(
            comment_id=2,
            post_id=2,
            commented_by_id=1,
            commented_at="2019-05-21 20:22:46.810366",
            parent_comment_id=1,
            content="usrt"
        )
    ]
    return comment_dtos



@pytest.fixture()
def comment_replies_dto():
    comment_replies_dto = [CommentRepliesDto(
        comment_id=2,
        commenter=user_dto(),
        commented_at="2019-05-21 20:22:46.810366",
        comment_content="thanws"
        )]
    return comment_replies_dto

@pytest.fixture()
def replies_dtos():
    replies_dtos = [
        CommentDto(
            comment_id=2,
            post_id=2,
            commented_by_id=1,
            commented_at="2019-05-21 20:22:46.810366",
            parent_comment_id=None,
            content='thanws'
        )
    ]
    return replies_dtos

@pytest.fixture()
def reaction_dtos():
    reaction_dtos = [
            ReactionDto(
                reaction_id=1,
                reacted_by_id=1,
                post_id=None,
                comment_id=1,
                reacted_at="2019-05-21 20:22:46.810366",
                reaction=ReactionType.WOW.value
            ),
            ReactionDto(
                reaction_id=1,
                reacted_by_id=1,
                post_id=None,
                comment_id=1,
                reacted_at="2019-05-21 20:22:46.810366",
            reaction=ReactionType.WOW.value
            ) ,
            ReactionDto(
                reaction_id=1,
                reacted_by_id=1,
                post_id=None,
                comment_id=2,
                reacted_at="2019-05-21 20:22:46.810366",
                reaction=ReactionType.WOW.value
            )  
    ]
    return reaction_dtos

@pytest.fixture()
def comment_reaction_metrics_dtos():
    comment_reaction_metrics_dtos = [
        CommentReactionMetricsDto(
            comment_id=1,
            reaction_type = ["WOW"],
            count=2
        ),
        CommentReactionMetricsDto(
            comment_id=2,
            reaction_type = ["WOW"],
            count=1
        )
    ]
    return comment_reaction_metrics_dtos

@pytest.fixture()
def post_reaction_metrics_dtos():
    reaction_dtos = PostReactionMetricsDto(
            post_id=1,
            reaction_type = [],
            count= 0
        )
    return reaction_dtos

@pytest.fixture()
def comment_replies_dtos():
    reaction_dtos = [CommentsRepliesDto(
            comment_id=1,
            count= 1
        )]
    return reaction_dtos


@pytest.fixture()
def post_comments_count_dtos():
    post_comments_count_dtos = [
        PostCommentsCountDto(
            post_id=1,
            count= 1
        ),
        PostCommentsCountDto(
            post_id=2,
            count= 0
        )
    ]
    return post_comments_count_dtos


#comment_reaction_metrics_dtos, post_reaction_metrics_dtos, comment_replies_dtos
 





@pytest.fixture()
def reaction_metrics_dto():
    reaction_metrics_dto = ReactionsCountDto(
        reaction_type=ReactionType.WOW.value,
        count=2
    )
    return reaction_metrics_dto


post_dict = {
        'post_content': 'NEW POST',
        'post_id': 1,
        'posted_at': '13-12-2019,00:00:1568140200.00',
        'posted_by': {
            'name': 'James',
            'profile_pic': 'https://www.google.com',
            'user_id': 1
        },
        'reactions': {
            'count': 1,
            'type': [
                ReactionType.HAHA.value
            ]
        },
        'comments': [
            {
                'comment_content': 'nice post',
                'comment_id': 1,
                'commented_at': '13-12-2019,00:00:1568140200.00',
                'commenter': {
                    'name': 'James',
                    'profile_pic': 'https://www.google.com',
                    'user_id': 2
                },
                'reactions': {
                    'count': 1,
                    'type': [
                        ReactionType.SAD.value
                    ]
                },
                'replies': [
                    {
                        'comment_content': 'nice post',
                        'comment_id': 2,
                        'commented_at': '13-12-2019,00:00:1568140200.00',
                        'commenter': {
                            'name': 'James',
                            'profile_pic': 'https://www.google.com',
                            'user_id': 2
                        }
                    },
                    {
                        'count': 1,
                        'type': [
                            ReactionType.LIT.value
                        ]
                    }
                ],
                'replies_count': 1
            }

        ],
        "comments_count": 1

}
    

@pytest.fixture()
def get_post_response():
    get_post_response = post_dict
    return get_post_response

@pytest.fixture()
def get_user_posts_response():
    get_user_posts_response = [post_dict]
    return get_user_posts_response

'''