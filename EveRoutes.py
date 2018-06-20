import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic

Ui_MainWindow, QtBaseClass = uic.loadUiType("erui.ui")
qtCreatorFile =  "erui.ui"

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
  def __init__(self):
    super(MyApp, self).__init__()
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)
    self.ui.get_route.clicked.connect(self.routeNames)

  def routeNames(self):
    import json
    import requests
    route = self.getRoute(self.getID())
    dataR = json.dumps(route)
    urlR = "https://esi.evetech.net/latest/universe/names/?datasource=tranquility"
    R = requests.post(url = urlR, data = dataR)
    routeN = R.json()
    routeO = []
    for ns in routeN:
      na = ns['name']
      routeO.append(na)
    final = ''
    for out in routeO:
      final += out + ' to '
    final = str(final)
    self.results.setText(final)

  def getID(self):
    oriname = str(self.ui.ori_box.toPlainText())
    destname = str(self.ui.dest_box.toPlainText())
    import json
    import requests
    urlI = "https://esi.evetech.net/latest/universe/ids/?datasource=tranquility"
    dataI = json.dumps([oriname,destname])
    I = requests.post(url = urlI, data = dataI)
    if I.status_code != 200:
      print('Status:', response.status_code, 'Problem with the request. Exiting.')
      exit()
    idobj = I.json()
    ids = []
    for on in idobj['systems']:
      ii = [on['id']]
      ids.append(ii)
    oriid = ids[0][0]
    destid = ids[1][0]
    locs = [str(oriid),str(destid)]
    print(locs)
    return locs

  def getRoute(x):
    import requests
    import string
    urlR="https://esi.evetech.net/latest/route/O/D/?datasource=tranquility&flag=shortest"
    urlR = urlR.replace('O', x[0])
    urlR = urlR.replace('D', x[1])
    response = requests.get(urlR, verify=True)
    if response.status_code != 200:
      print('Status:', response.status_code, 'Problem with the request. Exiting.')
      exit()
    data = response.json()
    return data

if __name__ == "__main__":
  app = QApplication(sys.argv)
  app.aboutToQuit.connect(app.deleteLater)
  window = MyApp()
  window.show()
  sys.exit(app.exec_())
