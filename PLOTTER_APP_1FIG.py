import sys
import pandas as pd
from PyQt5.QtWidgets import*
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar  # Import NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np

class DataPlotterApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('MATPLOTLIB---SUJIT')

        self.setStyleSheet(self.load_stylesheet("styles.css"))


        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()
        self.central_widget.setLayout(layout)

        # Widgets for file browsing
        self.browse_buttons = []
        self.file_layouts = []
        self.x_axis_listboxes = []  
        self.y_axis_listboxes = []  
        self.df = []

        for i in range(2):
            file_layout = QVBoxLayout()
            layout.addLayout(file_layout)
            self.file_layouts.append(file_layout)

            button = QPushButton(f"Browse File {i+1}")
            button.clicked.connect(lambda _, index=i: self.browse_files(index))
            file_layout.addWidget(button)
            self.browse_buttons.append(button)

            axis_layout = QHBoxLayout()
            file_layout.addLayout(axis_layout)

            x_axis_label = QLabel("X-axis:")
            axis_layout.addWidget(x_axis_label)

            x_axis_listbox = QListWidget()
            axis_layout.addWidget(x_axis_listbox)
            self.x_axis_listboxes.append(x_axis_listbox)

            # self.x_axis_comboboxes = QComboBox()
            # axis_layout.addWidget(self.x_axis_listboxes)

            y_axis_label = QLabel("Y-axis:")
            axis_layout.addWidget(y_axis_label)

            y_axis_listbox = QListWidget()
            axis_layout.addWidget(y_axis_listbox)
            self.y_axis_listboxes.append(y_axis_listbox)

        # Plot button
        plot_button = QPushButton("Plot")
        plot_button.clicked.connect(self.plot_data)
        layout.addWidget(plot_button)

         #figure for plotting
        self.figure = Figure(figsize=(100, 10))
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        self.toolbar = NavigationToolbar(self.canvas, self)
        layout.addWidget(self.toolbar)

        self.ax = self.figure.add_subplot(111) 
    
    def load_stylesheet(self, filename):
        with open(filename, "r") as file:
            return file.read()

    def browse_files(self, index):
        filename, _ = QFileDialog.getOpenFileName(self, f"Select data file {index+1}", "", "Text files (*.txt)")
        if filename:
            self.process_file(filename, index)

    def process_file(self, filename, index):
        try:
            df = pd.read_csv(filename, header=0, delimiter="\t")
            
            f = open(filename)
            self.header = f.readline()
            f.close()
            self.col_name = self.header.split('\n')[0]
            self.col_name = self.col_name.split('\t')
            
            for i in range(len(self.col_name)):
                self.x_axis_listboxes[index].addItem(self.col_name[i])
                self.y_axis_listboxes[index].addItem(self.col_name[i])

            self.df.append(df)
        except pd.errors.EmptyDataError:
            QMessageBox.critical(self, "Error", f"File {filename} is empty.")
        except pd.errors.ParserError:
            QMessageBox.critical(self, "Error", f"Parsing error in file {filename}.")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def plot_data(self):
        self.ax.clear()

        for i in range(len(self.df)):
            x_variable = self.x_axis_listboxes[i].currentItem().text()
            y_variable = self.y_axis_listboxes[i].currentItem().text()

            self.ax.plot(self.df[i][x_variable], self.df[i][y_variable], label=f"File {i+1}: {x_variable} vs {y_variable}")

        self.ax.legend()
        self.ax.set_xlabel("X-axis")
        self.ax.set_ylabel("See Legend")
        self.ax.set_title("Data Plots")
        # self.ax.set_title(f"Figure Title: {x_variable} vs {', '.join(y_variable)}")
        self.ax.grid(True, which='both')
        self.figure.tight_layout()
        self.canvas.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DataPlotterApp()
    window.resize(2000, 1000)
    window.show()
    sys.exit(app.exec_())
