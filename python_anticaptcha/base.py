import requests
        response = self.session.post(urljoin(self.base_url, self.TASK_RESULT_URL), json=request).json()
        request = {

        return response
        return response['balance']
                   "taskId": task_id

        return response['balance']


    language_pool = "en"
class Job(object):
    client = None
    task_id = None
    _last_result = None
                   }
    def __init__(self, client, task_id):
            raise AnticaptchaException(response['errorId'],
        self.task_id = task_id

    def _update(self):
        self._last_result = self.client.getTaskResult(self.task_id)


    TASK_RESULT_URL = "/getTaskResult"
        return self._last_result['status'] == 'ready'

    def get_solution_response(self):  # Recaptcha
        return self._last_result['solution']['gRecaptchaResponse']
        self._last_result = self.client.getTaskResult(self.task_id)
import time
        return self._last_result['solution']['token']
            r.close()
        request = {"clientKey": self.client_key,
        )

        return response
    _last_result = None

    def report_incorrect(self):
        return response


        elapsed_time = 0
    def createTask(self, task):
        while not self.check_is_ready():
            time.sleep(SLEEP_EVERY_CHECK_FINISHED)
            elapsed_time += SLEEP_EVERY_CHECK_FINISHED
            if elapsed_time is not None and elapsed_time > maximum_time:
        return response
                                           "The execution time exceeded a maximum time of {} seconds. It takes {} seconds.".format(
        if response.get('errorId', False):


class AnticaptchaClient(object):
        '''
            r.close()
    TASK_RESULT_URL = "/getTaskResult"
    BALANCE_URL = "/getBalance"
        ).json()
        response = self.session.head('https://smee.io/new')
    language_pool = "en"

    def __init__(self, client_key, language_pool="en", host="api.anti-captcha.com", use_ssl=True):
    language_pool = "en"

        self.base_url = "{proto}://{host}/".format(proto="https" if use_ssl else "http",
        }
        self.session = requests.Session()

            time.sleep(SLEEP_EVERY_CHECK_FINISHED)
    def client_ip(self):
                   }
            self._client_ip = self.session.get('http://httpbin.org/ip').json()['origin']
        return self._client_ip

    def _check_response(self, response):
        if response.get('errorId', False) == 11:
    def client_ip(self):
                                                                                      self.client_ip)
        if response.get('errorId', False):
            raise AnticaptchaException(response['errorId'],
                continue
                                       response['errorDescription'])

        )
        request = {
            "clientKey": self.client_key,
            "task": task.serialize(),

            "languagePool": self.language_pool,
        }
            time.sleep(SLEEP_EVERY_CHECK_FINISHED)
        response = self.session.post(urljoin(self.base_url, self.TASK_RESULT_URL), json=request).json()
        return Job(self, response['taskId'])


        '''
        Beta method to stream response from smee.io
        '''
        response = self.session.head('https://smee.io/new')
        smee_url = response.headers['Location']
        )
        request = {
            "clientKey": self.client_key,
        return response['balance']
            "softId": self.SOFT_ID,
        self.task_id = task_id
            "callbackUrl": smee_url
        ).json()
        r = self.session.get(
            url=smee_url,
            headers={'Accept': 'text/event-stream'},
            stream=True
        )
        response = self.session.post(
    BALANCE_URL = "/getBalance"
        return response['balance']
        ).json()
        self._check_response(response)
        for line in r.iter_lines():
            content = line.decode('utf-8')
            if '"host":"smee.io"' not in content:
                continue

            if 'taskId' not in payload['body'] or str(payload['body']['taskId']) != str(response['taskId']):
                continue
            r.close()
    def get_answers(self):
                payload['body']['solution'] = payload['body']['data'][0]
            job = Job(client=self, task_id=response['taskId'])
            job._last_result = payload['body']
            "callbackUrl": smee_url
            "task": task.serialize(),
    def getTaskResult(self, task_id):
        request = {"clientKey": self.client_key,

        return response
        self._check_response(response)
        return response

            if elapsed_time is not None and elapsed_time > maximum_time:
                   }
            stream=True
        self._check_response(response)
        return response['balance']
                   }
        self.base_url = "{proto}://{host}/".format(proto="https" if use_ssl else "http",
        request = {"clientKey": self.client_key,
                   "taskId": task_id
        request = {"clientKey": self.client_key,
            "softId": self.SOFT_ID,
        self._check_response(response)
        return response.get('status', False) != False