import logging

import azure.functions as func

from scraper import scrape

def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(scrape(name, 1))
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name of a facebook page in the query string to find it's haters.",
             status_code=200
        )
