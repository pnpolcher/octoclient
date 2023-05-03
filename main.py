from octoclient.octoclient import OctoprintClient


API_KEY = "<YOUR-API-KEY-HERE>"

if __name__ == '__main__':
    client = OctoprintClient('localhost', 5000, API_KEY)
    client.connect()
    print(client.get_connection_status())
    client.disconnect()
