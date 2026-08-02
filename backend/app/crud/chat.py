from sqlalchemy.orm import Session

from app.models.chat import ChatHistory


def create_chat(
    db: Session,
    user_id,
    report_id,
    question: str,
    answer: str,
):
    chat = ChatHistory(
        user_id=user_id,
        report_id=report_id,
        question=question,
        answer=answer,
    )

    db.add(chat)
    db.commit()
    db.refresh(chat)

    return chat


def get_chat_history(
    db: Session,
    user_id,
    report_id,
):
    return (
        db.query(ChatHistory)
        .filter(
            ChatHistory.user_id == user_id,
            ChatHistory.report_id == report_id,
        )
        .order_by(ChatHistory.created_at.asc())
        .all()
    )