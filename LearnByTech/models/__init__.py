from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import User
from .course import Course
from .video import Video
from .enrollment import Enrollment