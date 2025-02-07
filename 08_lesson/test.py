import requests


base_url = "https://ru.yougile.com/api-v2"
headers = {
  "Content-Type": "application/json","Authorization": "Bearer --"
}


def test_get_projects():
   response = requests.get(base_url + "/projects", headers=headers)
   assert response.status_code == 200


def test_creat_project():
   body = {
       "title": "Sky pro"
   }
   response = requests.post(
       base_url + "/projects", headers=headers, json=body)
   assert response.status_code == 201
   json_response = response.json()
   assert "id" in json_response


def test_change_project():
   body = {
      "title": "Sky pro",
   }
   response = requests.post(
       base_url + "/projects", headers=headers, json=body)
   body = response.json()
   change_body = {
       "title": "Home work 8"
   }
   response2 = requests.put(
       base_url + '/projects/' + body['id'],
       json=change_body,
       headers=headers
   )
   assert response2.status_code == 200


def test_get_id():
   body = {
      "title": "Sky pro",
      }
   response = requests.post(
       base_url + '/projects', headers=headers, json=body)
   body = response.json()
   response2 = requests.get(
       base_url + '/projects/'+body['id'], headers=headers)
   assert response2.status_code == 200

