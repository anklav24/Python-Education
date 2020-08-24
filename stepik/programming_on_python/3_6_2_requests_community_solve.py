import requests

with open('D:\\dataset_3378_2.txt') as file_in, open('D:\\result.txt', 'w') as file_out:
    url = file_in.readline().strip()
    r = requests.get(url)
    result = str(len(r.text.splitlines()))
    file_out.write(result)