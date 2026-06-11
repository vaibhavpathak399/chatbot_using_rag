import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from app.db.database import engine
from app.db.models import Base

Base.metadata.create_all(
    bind=engine
)

print(
    "Tables Created Successfully"
)