from app.db.models import Message
from app.db.models import Feedback

def save_message(
    db,
    session_id,
    role,
    content
):

    message = Message(
        session_id=session_id,
        role=role,
        content=content
    )

    db.add(message)

    db.commit()


def get_messages(
    db,
    session_id
):

    messages = (
        db.query(Message)
        .filter(
            Message.session_id == session_id
        )
        .order_by(
            Message.id
        )
        .all()
    )

    return messages



def save_feedback(
    db,
    session_id,
    question,
    answer,
    feedback
):

    feedback_record = Feedback(
        session_id=session_id,
        question=question,
        answer=answer,
        feedback=feedback
    )

    db.add(
        feedback_record
    )

    db.commit()