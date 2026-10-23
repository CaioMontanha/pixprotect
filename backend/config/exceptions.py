from rest_framework.views import exception_handler

def api_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        detail = response.data
        if isinstance(detail, dict):
            message = "; ".join(f"{key}: {', '.join(map(str, value)) if isinstance(value, list) else value}" for key, value in detail.items())
        elif isinstance(detail, list):
            message = "; ".join(map(str, detail))
        else:
            message = str(detail)
        response.data = {"erro": "request_error", "mensagem": message}
    return response
