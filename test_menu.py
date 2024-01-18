import sys
import os

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('menu.ui', self)
        self.start_btn.clicked.connect(self.run)
    
    def run(self):
        data_ro_0 = self.data_ro_0.text()
        data_bett = self.data_bett.text()
        data_mu = self.data_mu.text()
        data_g = self.data_g.text()
        data_ro_w = self.data_ro_w.text()
        data_V_0 = self.data_V_0.text()
        data_h = self.data_h.text()
        data_d_h = self.data_d_h.text()
        ro_a = self.data_ro_a.text()
        C_d = self.data_C_d.text()
        W_x = self.data_W_x.text()
        scale = self.data_scale.text()
        
        with open('file.txt', 'w') as f:
            f.write(
                f'ro_0={data_ro_0}\nbett={data_bett}\nmu={data_mu}\ng={data_g}\nro_w={data_ro_w}\nV_0={data_V_0}\nh={data_h}\nd_h={data_d_h}\nro_a={ro_a}\nC_d={C_d}\nW_x={W_x}\nscale={scale}')
        f.close()
        exec(open('main.py').read())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
