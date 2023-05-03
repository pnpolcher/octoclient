from typing import Any, Dict, Optional

import urllib.parse
import requests


class OctoprintClient:

    def __init__(self, hostname: str, port: int, api_key: str):
        self.api_key = api_key
        self.base_url = f'http://{hostname}:{port}/api'

    def _get_headers(self):
        return {
            'X-Api-Key': self.api_key
        }

    def _post_headers(self):
        return {
            'Content-Type': 'application/json',
            'X-Api-Key': self.api_key,
        }

    def get_request(self, url_path: str, params: Optional[Dict[str, str]] = None):
        return requests.get(
            self.base_url + url_path,
            headers=self._get_headers(),
            params=params or {},
        ).json()

    def post_request(self, url_path: str, data: Any):
        response = requests.post(
            self.base_url + url_path,
            headers=self._post_headers(),
            json=data,
        )

        print(response.status_code, response.text)
        if 200 <= response.status_code < 300:
            try:
                return response.json()
            except requests.JSONDecodeError:
                return response.text
        else:
            return response

    def get_printer_status(self, history: bool = False, limit: Optional[int] = None):
        return self.get_request('/printer', params={
            'history': str(history).lower(),
            'limit': str(limit),
        })

    def get_tool_status(self, history: bool = False, limit: Optional[int] = None):
        return self.get_request('/printer/tool', params={
            'history': str(history).lower(),
            'limit': str(limit),
        })

    def get_bed_status(self, history: bool = False, limit: Optional[int] = None):
        return self.get_request('/printer/bed', params={
            'history': str(history).lower(),
            'limit': str(limit),
        })

    def get_connection_status(self):
        return self.get_request('/connection')

    def get_sd_card_status(self):
        return self.get_request('/printer/sd')

    def get_job_status(self):
        return self.get_request('/job')

    def start_job(self):
        return self.post_request('/job', {
            'command': 'start',
        })

    def cancel_job(self):
        return self.post_request('/job', {
            'command': 'cancel',
        })

    def restart_job(self):
        return self.post_request('/job', {
            'command': 'restart',
        })

    def pause_job(self):
        return self.post_request('/job', {
            'command': 'pause',
            'action': 'pause',
        })

    def resume_job(self):
        return self.post_request('/job', {
            'command': 'pause',
            'action': 'resume',
        })

    def toggle_job(self):
        return self.post_request('/job', {
            'command': 'pause',
            'action': 'toggle',
        })

    def select_file(self, location: str, path: str, print: Optional[bool] = False):
        return self.post_request(urllib.parse.quote(f'/files/{location}/{path}'), {
            'command': 'select',
            'print': str(print).lower(),
        })

    def unselect_file(self):
        return self.post_request('/files', {
            'command': 'unselect',
        })

    def connect(self, port: Optional[str] = None, baudrate: Optional[int] = None,
                printer_profile: Optional[str] = None, save: Optional[bool] = None,
                autoconnect: Optional[bool] = None):

        payload = {
            'command': 'connect'
        }

        if port is not None:
            payload['port'] = str(port)

        if baudrate is not None:
            payload['baudrate'] = str(baudrate)

        if printer_profile is not None:
            payload['printerProfile'] = printer_profile

        if save is not None:
            payload['save'] = str(save).lower()

        if autoconnect is not None:
            payload['autoconnect'] = str(autoconnect).lower()

        return self.post_request('/connection', payload)

    def disconnect(self):
        return self.post_request('/connection', {
            'command': 'disconnect',
        })
