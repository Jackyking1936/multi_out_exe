import sys 
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QSizePolicy, QPlainTextEdit
from PySide6.QtGui import QIcon, QFont, QRegularExpressionValidator
from PySide6.QtCore import Qt, Signal, QObject, QRegularExpression

class main_ui(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Python多次分比例出場(教學範例，僅供參考)")
        self.resize(1200, 700)

        # 製作上下排列layout上為庫存表，下為log資訊
        layout = QVBoxLayout()

        title_font_size = "20px"
        
        # 製作上下排列layout上為庫存表，下為log資訊
        layout = QVBoxLayout()
        # 庫存表表頭
        self.table_header = ['股票名稱', '股票代號', '昨日股數', '庫存均價', '基準價', '現價', '基準漲幅(%)', '出場階段', '觸發股數', '成交股數']
        
        self.tablewidget = QTableWidget(0, len(self.table_header))
        self.tablewidget.setHorizontalHeaderLabels([f'{item}' for item in self.table_header])
        
        # 讀取區
        layout_table_read = QHBoxLayout()

        label_table_read = QLabel('庫存基準表:')
        label_table_read.setStyleSheet(f"QLabel {{ font-size: {title_font_size}; font-weight: bold; }}")
        label_table_read.setAlignment(Qt.AlignLeft)
        layout_table_read.addWidget(label_table_read)

        self.lineEdit_table_read = QLineEdit()
        layout_table_read.addWidget(self.lineEdit_table_read, 6)

        self.folder_btn = QPushButton('')
        self.folder_btn.setIcon(QIcon('folder.png'))
        self.folder_btn.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)  # 設定尺寸策略
        layout_table_read.addWidget(self.folder_btn)

        self.table_read_btn = QPushButton('讀取')
        self.table_read_btn.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)  # 設定尺寸策略
        layout_table_read.addWidget(self.table_read_btn, 1)

        label_dummy = QLabel("   ")
        layout_table_read.addWidget(label_dummy, 3)

        # 整個設定區layout
        layout_condition = QGridLayout()

        # 監控區layout設定
        label_monitor = QLabel('參數設定')
        label_monitor.setStyleSheet(f"QLabel {{ font-size: {title_font_size}; font-weight: bold; }}")
        label_monitor.setAlignment(Qt.AlignLeft)
        layout_condition.addWidget(label_monitor, 0, 0)

        # 建立 QDoubleValidator 物件
        regex = QRegularExpression(r"^\d+(\.\d+)?$")
        validator = QRegularExpressionValidator(regex)

        label_tp1 = QLabel('\t階段 1，觸發漲幅(%):')
        layout_condition.addWidget(label_tp1, 1, 0)
        self.lineEdit_default_tp1 = QLineEdit()
        self.lineEdit_default_tp1.setText(str(5))
        layout_condition.addWidget(self.lineEdit_default_tp1, 1, 1)
        label_tp1_post = QLabel('%')
        layout_condition.addWidget(label_tp1_post, 1, 2)

        tp1_base_idx = 3
        label_tp1_out_pct = QLabel('，出場比例(%):')
        layout_condition.addWidget(label_tp1_out_pct, 1, 0+tp1_base_idx)
        self.lineEdit_tp1_out_pct = QLineEdit()
        self.lineEdit_tp1_out_pct.setText(str(25))
        layout_condition.addWidget(self.lineEdit_tp1_out_pct, 1, 1+tp1_base_idx)
        label_tp1_out_pct_post = QLabel('%')
        layout_condition.addWidget(label_tp1_out_pct_post, 1, 2+tp1_base_idx)

        label_tp2 = QLabel('\t階段 2，觸發漲幅(%):')
        layout_condition.addWidget(label_tp2, 2, 0)
        self.lineEdit_default_tp2 = QLineEdit()
        self.lineEdit_default_tp2.setText(str(7))
        layout_condition.addWidget(self.lineEdit_default_tp2, 2, 1)
        label_tp2_post = QLabel('%')
        layout_condition.addWidget(label_tp2_post, 2, 2)

        tp2_base_idx = 3
        label_tp2_out_pct = QLabel('，出場比例(%):')
        layout_condition.addWidget(label_tp2_out_pct, 2, 0+tp2_base_idx)
        self.lineEdit_tp2_out_pct = QLineEdit()
        self.lineEdit_tp2_out_pct.setText(str(50))
        layout_condition.addWidget(self.lineEdit_tp2_out_pct, 2, 1+tp2_base_idx)
        label_tp2_out_pct_post = QLabel('%')
        layout_condition.addWidget(label_tp2_out_pct_post, 2, 2+tp2_base_idx)

        label_tp3 = QLabel('\t階段 3，觸發漲幅(%):')
        layout_condition.addWidget(label_tp3, 3, 0)
        self.lineEdit_default_tp3 = QLineEdit()
        self.lineEdit_default_tp3.setText(str(9))
        layout_condition.addWidget(self.lineEdit_default_tp3, 3, 1)
        label_tp3_post = QLabel('%')
        layout_condition.addWidget(label_tp3_post, 3, 2)

        tp3_base_idx = 3
        label_tp3_out_pct = QLabel('，出場比例(%):')
        layout_condition.addWidget(label_tp3_out_pct, 3, 0+tp3_base_idx)
        self.lineEdit_tp3_out_pct = QLineEdit()
        self.lineEdit_tp3_out_pct.setText(str(100))
        layout_condition.addWidget(self.lineEdit_tp3_out_pct, 3, 1+tp3_base_idx)
        label_tp3_out_pct_post = QLabel('%')
        layout_condition.addWidget(label_tp3_out_pct_post, 3, 2+tp3_base_idx)

        self.lineEdit_default_tp1.setValidator(validator)
        self.lineEdit_default_tp2.setValidator(validator)
        self.lineEdit_default_tp3.setValidator(validator)
        self.lineEdit_tp1_out_pct.setValidator(validator)
        self.lineEdit_tp2_out_pct.setValidator(validator)
        self.lineEdit_tp3_out_pct.setValidator(validator)

        # 啟動按鈕
        self.button_start = QPushButton('開始監控')
        self.button_start.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        self.button_start.setStyleSheet("QPushButton { font-size: 24px; font-weight: bold; }")
        layout_condition.addWidget(self.button_start, 1, 6, 3, 1)

        # 停止按鈕
        self.button_stop = QPushButton('停止監控')
        self.button_stop.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        self.button_stop.setStyleSheet("QPushButton { font-size: 24px; font-weight: bold; }")
        layout_condition.addWidget(self.button_stop, 1, 6, 3, 1)
        self.button_stop.setVisible(False)
        
        layout_log = QVBoxLayout()
        # 監控區layout設定
        label_log_text = QLabel('執行日誌')
        label_log_text.setStyleSheet(f"QLabel {{ font-size: {title_font_size}; font-weight: bold; }}")
        label_log_text.setAlignment(Qt.AlignLeft)
        layout_log.addWidget(label_log_text, 0)

        self.log_text = QPlainTextEdit()
        self.log_text.setReadOnly(True)
        layout_log.addWidget(self.log_text, 1)

        layout.addWidget(self.tablewidget, stretch=10)
        # layout.addLayout(layout_table_read)
        layout.addLayout(layout_condition, stretch=1)
        layout.addLayout(layout_log, stretch=5)
        self.setLayout(layout)

if __name__ == "__main__":

    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()

    multi_out_ui = main_ui()
    font = QFont("Microsoft JhengHei", 12)  # 字體名稱和大小
    app.setFont(font)
    multi_out_ui.show()

    sys.exit(app.exec())