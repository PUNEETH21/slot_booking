from datetime import datetime
from typing import List, Optional
from django_swagger_utils.drf_server.exceptions import NotFound, Forbidden
from slot_booking.interactors.storages.user_slot_storage_interface \
    import UserSlotStorageInterface
from slot_booking.models.user_slot import UserSlot
from slot_booking.dtos.dtos import (
    UpcomingSlotDto, PreviousSlotDto, TimeRangeCountDto
)

from django.db.models import Count

class UserSlotStorageImplementation(UserSlotStorageInterface):

    def get_previous_slots(self, user_id: int, off_set: int, limit: int):
        today_date = datetime.now().date()
        present_time = datetime.now().time()
        user_slot_objects = UserSlot.objects.filter(
            user_id=user_id, date__lte=today_date
        )[off_set:limit]

        user_slot_dto_list = []
        if user_slot_objects:
            for user_slot_object in user_slot_objects:
                user_slot_dto_list.append(
                    PreviousSlotDto(
                        date = str(user_slot_object.date),
                        start_time = str(user_slot_object.start_time),
                        end_time = str(user_slot_object.end_time),
                        washing_machine_id=user_slot_object.washing_machine_id
                        )
                )

        return user_slot_dto_list

    def get_upcoming_slots(self, user_id: int):
        today_date = datetime.now().date()
        user_slot_objects = UserSlot.objects.filter(
            user_id=user_id, date__gte=today_date
        )

        user_slot_dto_list = []
        if user_slot_objects:
            for user_slot_object in user_slot_objects:
                user_slot_dto_list.append(
                    UpcomingSlotDto(
                        date = str(user_slot_object.date),
                        start_time = str(user_slot_object.start_time),
                        end_time = str(user_slot_object.end_time),
                        washing_machine_id=user_slot_object.washing_machine_id
                        )
                )

        return user_slot_dto_list


    def cannot_book_in_date(self, user_id: int, present_date: str,
        book_days_after: int
    ):
        last_date = UserSlot.objects.filter(user_id=user_id).last()
        if last_date:
            difference = present_date-last_date.date
            days = difference.days
            user_valid_to_book_in_date = book_days_after <= days
            if user_valid_to_book_in_date:
                return True
            else:
                return False
        else:
            return True



    def available_washing_machine(self, user_slot_wm_ids, washing_machines):
        for wm_id in washing_machines:
            user_wm_id = wm_id not in user_slot_wm_ids
            if user_wm_id:
                return wm_id


    def create_slot(self, date: str, start_time: str, 
        end_time: str, washing_machine_id: str, user_id: int
    ):
        UserSlot.objects.create(date=date, start_time=start_time,
            end_time=end_time, washing_machine_id=washing_machine_id,
            user_id=user_id
        )

    def create_user_slot(self, user_id: int, date: str, start_time: str, 
        end_time: str, washing_machines: List[int]
    ):
        user_slot_wm_ids = UserSlot.objects.filter(
            date=date, start_time=start_time, end_time=end_time).values_list(
            'washing_machine_id', flat=True)

        if user_slot_wm_ids:
            washing_machine_id = self.available_washing_machine(
                user_slot_wm_ids,
                washing_machines
            )
            if washing_machine_id:
                self.create_slot(date=date, start_time=start_time,
                    end_time=end_time, 
                    washing_machine_id=washing_machine_id,
                    user_id=user_id
                )
                return True
            else:
                return False

        else:
            washing_machine_id = washing_machines[0]
            self.create_slot(date=date, start_time=start_time,
                end_time=end_time, washing_machine_id=washing_machine_id,
                user_id=user_id
            )
            return True

    def get_date_slots(self, date: str):
        user_slots_list = UserSlot.objects.filter(
            date=date).values("start_time", "end_time").annotate(
                count = Count("start_time")).values_list(
                    "start_time", "end_time", "count")

        user_slots_dtos_list = []
        for user_slot in user_slots_list:
            user_slots_dtos_list.append(
                TimeRangeCountDto(
                    start_time = str(user_slot[0]),
                    end_time = str(user_slot[1]),
                    count = user_slot[2]
                )
            )

        return user_slots_dtos_list
    
    def last_booked_date(self, user_id: int):
        user_obj = UserSlot.objects.filter(user_id=user_id).last()
        if user_obj:
            user_last_slot_date = user_obj.date
            return user_last_slot_date

    
    
    
    
    
    
    
    








'''
    def get_alloted_slots(self, day: str, washing_machine_id: str):
        wm_objs = WashingmachineSlot.objects.filter(
            day=day, washing_machine_id=washing_machine_id)

        time_slot_list = []
        if wm_objs:
            for wm_obj in wm_objs:
                time_slot_list.append(
                    TimeSlotDto(
                        start_time=wm_obj.start_time,
                        end_time=wm_obj.end_time
                    )
                )

        time_slot_dto =  TimeSlotsDtos(
            time_slots = time_slot_list
        )

        return time_slot_dto
    

    def get_create_comment_response(self, comment_id: int):
        return {
            "comment_id": comment_id
        }

    def get_response_for_get_total_reactions_count(self, reactions_count: int):
        return {
            "reactions_count": reactions_count
        }

    def get_create_post_response(self, post_id: int):
        return {
            "post_id": post_id
        }

    def get_response_for_get_posts_with_more_positive_reaction(
            self,
            post_ids: List[int]):
        return {
            "post_ids": post_ids
        }

    def get_response_for_get_post_reactions(
            self,
            post_reaction_dtos: PostReactionCompleteDetailsDto):
        post_reactions = []
        user_dto_dict = {}

        for user in post_reaction_dtos.user_dtos:
            user_dto_dict[user.user_id] = user

        for reaction in post_reaction_dtos.reaction_dtos:
            user_details_dict = self._get_user_details(
                user_dto_dict[reaction.user_id])
            user_details_dict["reaction_type"] = reaction.reaction_type
            post_reactions.append(user_details_dict)

        return post_reactions

    def get_response_for_get_post_details(self, get_post_dto: PostCompleteDetailsDto):
        users_dtos_dict = self._get_user_dtos_dict(get_post_dto)

        comments_dto_dict, reply_dtos_dict = self._get_comments_and_replies_dto_dict(
            get_post_dto)

        post_reaction_dtos_dict, comment_reaction_dtos_dict = \
            self._get_post_and_comment_reactions_dto_dict(get_post_dto)

        post_complete_details = self._get_post_details(
            users_dtos_dict,
            post_reaction_dtos_dict,
            comment_reaction_dtos_dict,
            reply_dtos_dict,
            get_post_dto.post_dto,
            comments_dto_dict)
        return post_complete_details

    def _convert_comment_to_dict(self, reply, user_dto_dict):
        comment_details = {
            "comment_id": reply.comment_id,
            "commenter": self._get_user_details(user_dto_dict[reply.user_id]),
            "commented_at": self._get_date_format(reply.pub_date_time),
            "comment_content": reply.comment_content
        }
        return comment_details

    def _get_post_reactions_dict(self, post_id, post_reaction_dto_dict):
        post_reactions = []
        post_reactions_count = 0

        for reaction in post_reaction_dto_dict.values():
            if self._is_reaction_post_id_equal_to_given_post_id(
                    reaction.post_id, post_id):
                post_reactions.append(reaction.reaction_type)
                post_reactions_count += 1

        post_reactions_dict = self._get_reaction_dict(post_reactions_count,
                                                      post_reactions)
        return post_reactions_dict

    def _get_post_details(self, user_dtos_dict,
                          post_reaction_dto_dict,
                          comment_reaction_dto_dict, reply_dto_dict,
                          post_dto, comments_dto_dict):

        comments, comments_count = self._get_comment_details(
            comment_reaction_dto_dict,
            reply_dto_dict,
            comments_dto_dict,
            user_dtos_dict)

        user_id = post_dto.user_id
        user_dto = user_dtos_dict[user_id]
        post_details = {
            "post_id": post_dto.post_id,
            "posted_by": self._get_user_details(user_dto),
            "posted_at": self._get_date_format(post_dto.pub_date_time),
            "post_content": post_dto.post_content,
            "reactions": self._get_post_reactions_dict(post_dto.post_id,
                                                       post_reaction_dto_dict),
            "comments": comments,
            "comments_count": comments_count
        }
        return post_details

    def _get_comment_reactions_dict(self, comment, comment_reaction_dto_dict):
        comment_reactions = []
        comment_reactions_count = 0

        for reaction in comment_reaction_dto_dict.values():
            if self._is_reaction_comment_id_equal_to_given_comment_id(
                    reaction.comment_id, comment.comment_id):
                comment_reactions.append(reaction.reaction_type)
                comment_reactions_count += 1

        comment_reactions_dict = self._get_reaction_dict(
            comment_reactions_count,
            comment_reactions)
        return comment_reactions_dict

    def _get_comment_details(self, comment_reaction_dto_dict, reply_dto_dict,
                             comment_dtos_dict, users_dto_dict):
        comments = []
        comments_count = 0
        for comment in comment_dtos_dict.values():
            comments_dict = self._get_comment_data(
                comment, users_dto_dict, reply_dto_dict,
                comment_reaction_dto_dict)
            comments.append(comments_dict)
            comments_count += 1
        return comments, comments_count

    def _get_comment_data(self, comment, users_dto_dict, reply_dto_dict,
                          comment_reaction_dto_dict):

        comments_dict = self._convert_comment_to_dict(comment, users_dto_dict)

        comments_dict["reactions"] = self._get_comment_reactions_dict(
            comment,
            comment_reaction_dto_dict)

        comments_dict["replies_count"], comments_dict["replies"] = \
            self._get_comment_replies(comment,
                                      users_dto_dict,
                                      reply_dto_dict,
                                      comment_reaction_dto_dict)
        return comments_dict

    def _get_comment_replies(self, comment, users_dto_dict, reply_dto_dict,
                             comment_reaction_dto_dict):
        replies_count = 0
        replies = []
        for reply in reply_dto_dict.values():
            replies_dict = self._get_reply_details_dict(
                reply, comment, users_dto_dict, comment_reaction_dto_dict)
            replies.append(replies_dict)
            replies_count += 1

        return replies_count, replies

    def _get_reply_details_dict(self, reply, comment, users_dto_dict,
                                comment_reaction_dto_dict):
        replies_count = 0
        reply_details_dict = {}
        is_reply = comment.comment_id is reply.parent_comment

        if is_reply:
            reply_details_dict = self._convert_comment_to_dict(reply, users_dto_dict)
            reply_details_dict["reactions"] = self._get_comment_reactions_dict(
                reply, comment_reaction_dto_dict)
            replies_count += 1
        return reply_details_dict

    def _get_comments_and_replies_dto_dict(self, post_details_dto):
        comments_dto_dict = {}
        reply_dto_dict = {}
        for comment in post_details_dto.comments_dto:
            if self._is_parent_comment_is_none(comment):
                comments_dto_dict[comment.comment_id] = comment
            else:
                reply_dto_dict[comment.comment_id] = comment
        return comments_dto_dict, reply_dto_dict

    def _get_post_and_comment_reactions_dto_dict(self, post_details_dto):
        post_reaction_dto_dict = {}
        comment_reaction_dto_dict = {}
        for reaction in post_details_dto.reactions_dto:
            if self._is_comment_reaction_is_none(reaction):
                post_reaction_dto_dict[reaction.reaction_id] = reaction
            else:
                comment_reaction_dto_dict[reaction.reaction_id] = reaction
        return post_reaction_dto_dict, comment_reaction_dto_dict

    @staticmethod
    def _is_reaction_comment_id_equal_to_given_comment_id(reaction_comment_id,
                                                          comment_id):
        post_id_equal_or_not = reaction_comment_id is comment_id
        return post_id_equal_or_not

    @staticmethod
    def _is_reaction_post_id_equal_to_given_post_id(reaction_post_id,
                                                    post_id):
        post_id_equal_or_not = reaction_post_id is post_id
        return post_id_equal_or_not

    @staticmethod
    def _get_reaction_dict(reaction_count, reactions_list):
        reaction_dict = {
            "count": reaction_count,
            "type": reactions_list
        }
        return reaction_dict

    @staticmethod
    def _is_comment_reaction_is_none(reaction):
        comment_reaction = reaction.comment_id
        is_comment_reaction_is_none = comment_reaction is None
        return is_comment_reaction_is_none

    @staticmethod
    def _is_parent_comment_is_none(comment):
        parent_comment = comment.parent_comment
        is_parent_comment_is_none = parent_comment is None
        return is_parent_comment_is_none

    @staticmethod
    def _get_user_details(user_dto):
        user_details_dict = {
            "user_id": user_dto.user_id,
            "name": user_dto.username,
            "profile_pic": user_dto.profile_pic
        }
        return user_details_dict

    @staticmethod
    def _get_user_dtos_dict(post_details_dto):
        users_dto_dict = {}
        for user in post_details_dto.users_dto:
            user_id = user.user_id
            users_dto_dict[user_id] = user
        return users_dto_dict

    @staticmethod
    def _get_date_format(date):
        date = date.strftime("%m-%d-%Y,%H:%M:%s.%f")
        return date
'''