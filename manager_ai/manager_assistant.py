from sqlalchemy import text
from database.db import SessionLocal


def ask_manager(question):

    question = question.lower()

    db = SessionLocal()

    try:

            if "how many" in question and "bike claims" in question:

                result = db.execute(
                    text(
                        "SELECT COUNT(*) FROM claims "
                        "WHERE vehicle_type = 'bike'"
                    )
                ).scalar()

                return f"There are {result} bike claims submitted."

            if "how many" in question and "car claims" in question:

                result = db.execute(
                    text(
                        "SELECT COUNT(*) FROM claims "
                        "WHERE vehicle_type = 'car'"
                    )
                ).scalar()

                return f"There are {result} car claims submitted."

            if "how many" in question and "claims" in question:

                result = db.execute(
                    text("SELECT COUNT(*) FROM claims")
                ).scalar()

                return f"There are {result} total claims submitted."

            if "average payout" in question and "bike" in question:

                result = db.execute(
                    text(
                        "SELECT AVG(predicted_amount) FROM claims "
                        "WHERE vehicle_type = 'bike'"
                    )
                ).scalar()

                return f"The average payout for bike claims is ₹{round(result or 0, 2)}."

            if "average payout" in question and "car" in question:

                result = db.execute(
                    text(
                        "SELECT AVG(predicted_amount) FROM claims "
                        "WHERE vehicle_type = 'car'"
                    )
                ).scalar()

                return f"The average payout for car claims is ₹{round(result or 0, 2)}."

            if "approval probability below 40" in question:

                result = db.execute(
                    text(
                        "SELECT COUNT(*) FROM claims "
                        "WHERE approval_probability < 40"
                    )
                ).scalar()

                return (
                    f"There are {result} claims with approval probability below 40%. "
                    "These should be flagged for human review."
                )

            if "total quotations" in question or "how many quotations" in question:

                result = db.execute(
                    text("SELECT COUNT(*) FROM quotations")
                ).scalar()

                return f"The total number of quotations generated is {result}."

            if "average premium" in question:

                result = db.execute(
                    text("SELECT AVG(predicted_premium) FROM quotations")
                ).scalar()

                return f"The average quoted premium is ₹{round(result or 0, 2)}."

            if "top questions" in question or "top chatbot questions" in question:

                rows = db.execute(
                    text(
                        "SELECT question, COUNT(*) AS count "
                        "FROM chat_logs "
                        "GROUP BY question "
                        "ORDER BY count DESC "
                        "LIMIT 5"
                    )
                ).fetchall()

                if not rows:
                    return "No chatbot questions found yet."

                answer = "Top chatbot questions:\n"

                for row in rows:
                    answer += f"- {row.question}: {row.count} times\n"

                return answer

            if "recent claims" in question:

                rows = db.execute(
                    text(
                        "SELECT vehicle_type, predicted_amount, approval_probability, created_at "
                        "FROM claims "
                        "ORDER BY created_at DESC "
                        "LIMIT 5"
                    )
                ).fetchall()

                if not rows:
                    return "No recent claims found."

                answer = "Recent claims:\n"

                for row in rows:
                    answer += (
                        f"- {row.vehicle_type}: ₹{round(row.predicted_amount or 0, 2)}, "
                        f"approval {round(row.approval_probability or 0, 2)}%, "
                        f"{row.created_at}\n"
                    )

                return answer

            return (
                "I can answer manager questions about total claims, bike claims, "
            "car claims, average payout, approval probability below 40%, "
            "total quotations, average premium, top chatbot questions, and recent claims."
        )

    finally:

        db.close()