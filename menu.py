import sys
import os
from PyQt5 import QtGui
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from main import simulation


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('menu.ui', self)
        self.start_btn.clicked.connect(self.run)
        self.setWindowIcon(QtGui.QIcon('logo.png'))


    def is_number(self, s):
        try:
            float(s)
            return True
        except:
            return False

    def run(self):

        spi = []
        ro_w = self.data_ro_w.text()
        ro_0 = self.data_ro_0.text()
        mu = self.data_mu.text()
        g = self.data_g.text()
        kin_vis_w = self.data_kin_vis_w.text()
        kin_vis_0 = self.data_kin_vis_0.text()
        v_0 = self.data_v_0.text()
        p_a = self.data_p_a.text()
        W_x = self.data_W_x.text()
        W_y = self.data_W_y.text()
        horseshoe = self.data_horseshoe.text()
        fi = self.data_fi.text()
        u_w = self.data_u_w.text()
        v_w = self.data_v_w.text()
        scale = self.data_scale.text()
        C_d = self.data_C_d.text()
        time = self.data_time.text()

        spi = [ro_w, ro_0, mu, g, kin_vis_w, kin_vis_0, v_0, p_a, W_x, W_y, horseshoe, fi, u_w, v_w, scale, C_d, time]
        flag = False
        for i in spi:
            if not self.is_number(i):
                flag = True
        if flag:
            self.label_ne_pizdi_mne.setText(
                '<h1 style="color: rgb(250, 55, 55);">Ошибка: Введено недопустимое значение</h1>')
        else:
            self.label_ne_pizdi_mne.setText('')
            # self.start_btn.setEnabled(False)
            with open('variables.txt', 'w') as f:
                f.write(
                    f'time={time}\nstart={1}\nro_w={ro_w}\nro_0={ro_0}\nmu={mu}\ng={g}\nkin_vis_w={kin_vis_w}\nkin_vis_0={kin_vis_0}\nv_0={v_0}\np_a={p_a}\nW_x={W_x}\nW_y={W_y}\nhorseshoe={horseshoe}\nfi={fi}\nu_w={u_w}\nv_w={v_w}\nscale={scale}\nC_d={C_d}\n')
            f.close()

            simulation()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
