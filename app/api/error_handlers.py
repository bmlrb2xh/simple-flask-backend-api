from  werkzeug.exceptions import HTTPException, NotFound

def unknown_error_handler(ex: Exception):
    return {
        'status': 'error',
        'message': 'An unknown error occured'
    }

def page_not_found_handler(ex: NotFound):
    return {
        'status': 'error',
        'message': 'Page not found'
    }

ERROR_HANDLERS = {
    HTTPException: unknown_error_handler,
    NotFound: page_not_found_handler
}
