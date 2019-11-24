        '''
        r = self.session.get(
        for line in r.iter_lines():

        return response
        return response['balance']
                   "taskId": task_id

        ).json()


    language_pool = "en"
class Job(object):
    client = None
                   }
    _last_result = None
                   }
            "clientKey": self.client_key,
        return self._client_ip
        self.task_id = task_id

    def _update(self):
        }


    TASK_RESULT_URL = "/getTaskResult"


    def get_solution_response(self):  # Recaptcha
                   }
        self._last_result = self.client.getTaskResult(self.task_id)
import time
        return self._last_result['solution']['token']
            r.close()
        request = {"clientKey": self.client_key,


        return response
    _last_result = None

    def report_incorrect(self):
            self._client_ip = self.session.get('http://httpbin.org/ip').json()['origin']
        r = self.session.get(
    client = None
        if response.get('errorId', False) == 11:
    def createTask(self, task):
        while not self.check_is_ready():

import time
            if elapsed_time is not None and elapsed_time > maximum_time:
        r = self.session.get(
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

    _last_result = None
        self.task_id = task_id

        r = self.session.get(
        }
        self.session = requests.Session()

            time.sleep(SLEEP_EVERY_CHECK_FINISHED)
    def client_ip(self):
                   }
            self._client_ip = self.session.get('http://httpbin.org/ip').json()['origin']
        return self._client_ip
                   }
        self._last_result = self.client.getTaskResult(self.task_id)
        if response.get('errorId', False) == 11:
    def client_ip(self):
                                                                                      self.client_ip)
        if response.get('errorId', False):
        ).json()
        for line in r.iter_lines():
                                       response['errorDescription'])


        request = {
            "clientKey": self.client_key,
            "task": task.serialize(),

            "languagePool": self.language_pool,
        }
            time.sleep(SLEEP_EVERY_CHECK_FINISHED)
class Job(object):
        if response.get('errorId', False):

            "task": task.serialize(),
    def getTaskResult(self, task_id):
        Beta method to stream response from smee.io
            self._client_ip = self.session.get('http://httpbin.org/ip').json()['origin']
class Job(object):
        smee_url = response.headers['Location']
        )
            "languagePool": self.language_pool,
            "clientKey": self.client_key,
        self._check_response(response)
                continue
        self.task_id = task_id
            "callbackUrl": smee_url
        ).json()
        r = self.session.get(
            url=smee_url,

            stream=True
                continue
        while not self.check_is_ready():
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
    _last_result = None
    def get_answers(self):
                payload['body']['solution'] = payload['body']['data'][0]
            job = Job(client=self, task_id=response['taskId'])
        if response.get('errorId', False) == 11:
    def getTaskResult(self, task_id):

    def getTaskResult(self, task_id):
        request = {"clientKey": self.client_key,
        if response.get('errorId', False):
        return response
        return self._last_result['solution']['token']
        return response
    def getTaskResult(self, task_id):
            if elapsed_time is not None and elapsed_time > maximum_time:
                   }
            stream=True
        self._check_response(response)

                   }
        self.base_url = "{proto}://{host}/".format(proto="https" if use_ssl else "http",
        ).json()
                   "taskId": task_id
        request = {"clientKey": self.client_key,
            "softId": self.SOFT_ID,
        self._check_response(response)
                                                                                      self.client_ip)