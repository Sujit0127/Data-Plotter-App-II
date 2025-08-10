import sys
import pandas as pd
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QFileDialog, QVBoxLayout, QWidget, 
    QCheckBox, QScrollArea, QComboBox, QLabel
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt

class DataPlotter(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Data Plotter")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet(self.load_stylesheet("styles.css"))
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.layout = QVBoxLayout(self.central_widget)
 
        self.header_label = QLabel("Plot to PDF Application")
        self.header_label.setAlignment(Qt.AlignCenter)
        self.header_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        self.layout.addWidget(self.header_label)
        
        self.load_button = QPushButton("Load Data File", self)
        self.load_button.clicked.connect(self.load_data)
        self.layout.addWidget(self.load_button)
        
        self.x_axis_label = QLabel("Select X-axis:")
        self.layout.addWidget(self.x_axis_label)
        
        self.x_axis_combobox = QComboBox(self)
        self.layout.addWidget(self.x_axis_combobox)
        
        self.y_axis_label = QLabel("Select Y-axis (Which Graph You Want):")
        self.layout.addWidget(self.y_axis_label)

        self.columns_layout = QVBoxLayout()
        self.columns_widget = QWidget()
        self.columns_widget.setLayout(self.columns_layout)
        self.scroll = QScrollArea()
        self.scroll.setWidget(self.columns_widget)
        self.scroll.setWidgetResizable(True)
        self.layout.addWidget(self.scroll)
        
        self.save_button = QPushButton("Save Plots to PDF", self)
        self.save_button.clicked.connect(self.save_plots)
        self.layout.addWidget(self.save_button)
 
        self.status_label = QLabel("")
        self.layout.addWidget(self.status_label)
        
        self.data = None
        self.checkboxes = []

    def load_stylesheet(self, filename):
        with open(filename, "r") as file:
            return file.read()

    def load_data(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Data File", "", "Text Files (*.txt);;All Files (*)")
        if file_name:
            self.data = pd.read_csv(file_name, delimiter='\t')
            self.create_column_checkboxes()
            self.populate_x_axis_combobox()
            self.status_label.setText(f"File loaded successfully.")
    
    def create_column_checkboxes(self):
        for checkbox in self.checkboxes:
            self.columns_layout.removeWidget(checkbox)
            checkbox.deleteLater()
        
        self.checkboxes = []
        for column in self.data.columns:
            checkbox = QCheckBox(column, self)
            self.checkboxes.append(checkbox)
            self.columns_layout.addWidget(checkbox)
    
    def populate_x_axis_combobox(self):
        self.x_axis_combobox.clear()
        self.x_axis_combobox.addItems(self.data.columns)
        self.x_axis_combobox.setCurrentIndex(0)
    
    def plot_data(self):
        if self.data is not None:
            plt.figure().clf()  # Clear any previous plots
            x_column = self.x_axis_combobox.currentText()
            selected_columns = [checkbox.text() for checkbox in self.checkboxes if checkbox.isChecked()]
            
            if selected_columns:
                fig, ax = plt.subplots()
                for column in selected_columns:
                    ax.plot(self.data[x_column], self.data[column], label=column)
                ax.set_xlabel(x_column)
                ax.legend()
                plt.show()
                self.status_label.setText("Plots generated successfully")
            else:
                self.status_label.setText("No columns selected for plotting")
        else:
            self.status_label.setText("No data loaded")
    
    def save_plots(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Save PDF", "", "PDF Files (*.pdf);;All Files (*)")
        if file_name:
            with PdfPages(file_name) as pdf:
                x_column = self.x_axis_combobox.currentText()
                for checkbox in self.checkboxes:
                    if checkbox.isChecked():
                        fig, ax = plt.subplots()
                        ax.plot(self.data[x_column], self.data[checkbox.text()], label=checkbox.text())
                        ax.set_xlabel(x_column)
                        ax.legend()
                        pdf.savefig(fig)
                        plt.close(fig)
                
                self.status_label.setText(f"Plots saved.")#{file_name}

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DataPlotter()
    window.show()
    sys.exit(app.exec_())
