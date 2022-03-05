

def success_response(status, data):
    """JSON Format for success response"""
    response = {
        "jsonrpc" : "2.0",
        "results" : {         
            "code" : status,
            "data" : data
        }
    }
    return response


def error_response(status, data):
    """JSON Format for error response"""
    response = {
        "code" : status,
        "error" : {
            "message" : data
        }
    }
    return response

def delete_success_response(status, data):
    """JSON Format for success response"""
    response = {
        "code" : status,
        "success" : {
            "message" : data
        }
    }
    return response
