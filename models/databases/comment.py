import datetime

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.databases.base import Base
from models.databases.post import Post


class Comment(Base):
    __tablename__ = "Comment"

    comment_id: Mapped["Post"] = relationship(
        back_populates="comment_id"
    )
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int]
    post_id: Mapped[int]
    comment_data: datetime
    comment_info: Mapped[str | None] = mapped_column(String(10000))
