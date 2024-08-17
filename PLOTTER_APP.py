import sys
import pandas as pd
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QCheckBox, QComboBox, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QFileDialog, QMessageBox, QListWidget, QListWidgetItem)
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
class DataPlotterApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Application--RSD--SUJIT')

        self.setStyleSheet(self.load_stylesheet("styles.css"))

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()
        self.central_widget.setLayout(layout)

        file_label = QLabel("Select data files:")
        layout.addWidget(file_label)

        browse_button = QPushButton("Browse")
        browse_button.clicked.connect(self.browse_files)
        layout.addWidget(browse_button)

        axis_layout = QHBoxLayout()
        layout.addLayout(axis_layout)

        self.x_axis_label = QLabel("X-axis:")
        axis_layout.addWidget(self.x_axis_label)

        self.x_axis_combobox = QComboBox()
        axis_layout.addWidget(self.x_axis_combobox)

        self.y_axis_label = QLabel("Y-axis:")
        axis_layout.addWidget(self.y_axis_label)

        self.y_axis_listwidget = QListWidget()
        axis_layout.addWidget(self.y_axis_listwidget)

        self.select_bit_label = QLabel("Get Bit:")
        axis_layout.addWidget(self.select_bit_label)

        self.y_axis_checkbox = QCheckBox()
        axis_layout.addWidget(self.y_axis_checkbox)

        self.select_bit_label = QLabel("Select Y-Axis bit:")
        axis_layout.addWidget(self.select_bit_label)
        
        self.select_bit_combobox = QComboBox()
        self.select_bit_combobox.addItems([str(i) for i in range(16)])
        axis_layout.addWidget(self.select_bit_combobox)

        plot_button = QPushButton("Plot with Matplotlib")
        plot_button.clicked.connect(self.plot_data)
        layout.addWidget(plot_button)

        self.figure = Figure(figsize=(12, 8))
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        self.toolbar = NavigationToolbar(self.canvas, self)
        layout.addWidget(self.toolbar)
        self.ax = self.figure.add_subplot(111)

        self.web_view = QWebEngineView()
        layout.addWidget(self.web_view)

        self.df = None  

    def load_stylesheet(self, filename):
        with open(filename, "r") as file:
            return file.read()

    def browse_files(self):
        filenames, _ = QFileDialog.getOpenFileNames(self, "Select data files", "", "Text files (*.txt *.csv)")
        for filename in filenames:
            self.process_file(filename)

    def process_file(self, filename):
        try:
            df = pd.read_csv(filename, delimiter="\t")
            self.df = df
            self.x_axis_combobox.clear()
            self.y_axis_listwidget.clear()

            for col_name in df.columns:
                self.x_axis_combobox.addItem(col_name)
                item = QListWidgetItem(col_name)
                item.setCheckState(False) 
                self.y_axis_listwidget.addItem(item)

        except pd.errors.EmptyDataError:
            QMessageBox.critical(self, "Error", f"File {filename} is empty.")
        except pd.errors.ParserError:
            QMessageBox.critical(self, "Error", f"Parsing error in file {filename}.")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def get_bit(self, value, bit_num):
     return (value >> bit_num) & 1

    def plot_data(self):
        if self.df is None:
            QMessageBox.warning(self, "Warning", "Please select data files first.")
            return

        x_variable = self.x_axis_combobox.currentText()
        
        # Get Bit checkbox
        get_bit_status = self.y_axis_checkbox.isChecked()
        
        # Retrieve the selected bit numbers, if any
        selected_bits = [int(bit.strip()) for bit in self.select_bit_combobox.currentText().split(',')]
        
        self.ax.clear()

        y_variables = []
        for index in range(self.y_axis_listwidget.count()):
            item = self.y_axis_listwidget.item(index)
            if item.checkState() == 2:  # 2 means item is checked
                y_variables.append(item.text())

        if len(y_variables) == 0:
            QMessageBox.warning(self, "Warning", "Please select at least one Y-axis variable.")
            return

        colors = plt.cm.rainbow(np.linspace(0, 1, len(y_variables) * len(selected_bits)))

        color_index = 0
        for var in y_variables:
            y_data = self.df[var].values
            if get_bit_status:
                for bit in selected_bits:
                    y_bit_data = [self.get_bit(value, bit) for value in y_data]
                    self.ax.plot(self.df[x_variable], y_bit_data, label=f"{var} - Bit {bit}", color=colors[color_index], linewidth=1.5, linestyle='-')
                    color_index += 1
            else:
                self.ax.plot(self.df[x_variable], y_data, label=f"{var}", color=colors[color_index], linewidth=1.5, linestyle='-')
                color_index += 1

        self.ax.set_title(f"{x_variable} vs {', '.join(y_variables)}")
        self.ax.set_xlabel(x_variable)
        self.ax.set_ylabel("Values")
        self.ax.legend()
        self.figure.tight_layout()
        self.ax.grid(True, which='both')
        self.canvas.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DataPlotterApp()
    window.resize(2000, 1000)
    window.show()
    sys.exit(app.exec_())
