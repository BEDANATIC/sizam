import dataclasses

from ..services.consts import UntiCourseStatus


@dataclasses.dataclass
class UntiSetStatusDTO:
    unti_id: int
    course_id: int
    status: UntiCourseStatus
