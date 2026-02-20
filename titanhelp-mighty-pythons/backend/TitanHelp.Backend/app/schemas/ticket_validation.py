##this is where you will put the validation checks
## todo: ?? def validate_ticket_payload(payload: dict) -> dict:

ALLOWED_PRIORITIES = {"Low", "Medium", "High"}

def validate_create_ticket(payload: dict) -> dict:
    errors = {}

    name = (payload.get("name") or "").strip()
    if not name or len(name) > 100:
        errors["name"] = "Name is required and must be <= 100 chars."

    desc = (payload.get("problem_description") or "").strip()
    if not desc or len(desc) > 1000:
        errors["problem_description"] = "Problem description is required and must be <= 1000 chars."

    priority = payload.get("priority")
    if priority not in ALLOWED_PRIORITIES:
        errors["priority"] = "Priority must be Low, Medium, or High."

    return errors