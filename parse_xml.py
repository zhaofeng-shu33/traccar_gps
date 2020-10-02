from bs4 import BeautifulSoup
def get_coordinate_list(file_name):
    with open(file_name) as f:
        st = f.read()
    soup = BeautifulSoup(st, "lxml")
    Ls = []
    for i in soup.find_all("trkpt"):
        Ls.append([float(i['lon']), float(i['lat'])])
    return Ls
