import sys
import pandas as pd
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

class DataPlotter(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("REPORT--SUJIT")
        self.setGeometry(100, 100, 1000, 600)
        self.setStyleSheet(self.load_stylesheet("styles.css"))
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.main_layout = QVBoxLayout(self.central_widget)

        self.header_label = QLabel("Plot to PDF Application")
        self.header_label.setAlignment(Qt.AlignCenter)
        self.header_label.setStyleSheet("font-size: 30px; font-weight: bold;")
        self.main_layout.addWidget(self.header_label)

        self.button_layout = QHBoxLayout()

        self.load_button = QPushButton("Load Data File", self)
        self.load_button.clicked.connect(self.load_data)
        self.button_layout.addWidget(self.load_button)

        self.select_image_button = QPushButton("Select Images", self)
        self.select_image_button.clicked.connect(self.select_images)
        self.button_layout.addWidget(self.select_image_button)
        
        self.main_layout.addLayout(self.button_layout)

        self.x_axis_label = QLabel("Select X-axis:")
        self.main_layout.addWidget(self.x_axis_label)
        
        self.x_axis_combobox = QComboBox(self)
        self.main_layout.addWidget(self.x_axis_combobox)
    
        self.content_layout = QHBoxLayout()
        
        self.y_axis_layout = QVBoxLayout()
        
        self.y_axis_label = QLabel("Select Y-axis (Which Graph You Want):")
        self.y_axis_layout.addWidget(self.y_axis_label)
        
        self.columns_layout = QVBoxLayout()
        self.columns_widget = QWidget()
        self.columns_widget.setLayout(self.columns_layout)
        self.scroll = QScrollArea()
        self.scroll.setWidget(self.columns_widget)
        self.scroll.setWidgetResizable(True)
        self.scroll.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.y_axis_layout.addWidget(self.scroll)
        
        self.content_layout.addLayout(self.y_axis_layout)
        
        self.right_group_box = QGroupBox("PDF First Page")
        self.right_layout = QVBoxLayout()
        
        self.pdf_title_label = QLabel("Artical Name:")
        self.right_layout.addWidget(self.pdf_title_label)
        self.pdf_title_input = QLineEdit(self)
        self.right_layout.addWidget(self.pdf_title_input)

        self.pdf_author_label = QLabel("Check Name:")
        self.right_layout.addWidget(self.pdf_author_label)
        self.pdf_author_input = QLineEdit(self)
        self.right_layout.addWidget(self.pdf_author_input)

        self.pdf_date_label = QLabel("Checks Date:")
        self.right_layout.addWidget(self.pdf_date_label)
        self.pdf_date_input = QLineEdit(self)
        self.right_layout.addWidget(self.pdf_date_input)
        
        self.right_group_box.setLayout(self.right_layout)
        self.right_group_box.setStyleSheet("QGroupBox { font-weight: bold; }")
        self.right_group_box.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        self.content_layout.addWidget(self.right_group_box)
      
        self.main_layout.addLayout(self.content_layout)
 
        self.save_button = QPushButton("Save Plots and Images to PDF", self)
        self.save_button.clicked.connect(self.save_plots_and_images)
        self.main_layout.addWidget(self.save_button)

        self.status_label = QLabel("")
        self.main_layout.addWidget(self.status_label)
        
        self.data = None
        self.checkboxes = []
        self.selected_images = []

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
    
    def select_images(self):
        file_names, _ = QFileDialog.getOpenFileNames(self, "Select Images", "", "Image Files (*.png *.jpg *.bmp);;All Files (*)")
        if file_names:
            self.selected_images = file_names
            self.status_label.setText(f"Selected {len(file_names)} images.")
    
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
    
    def save_plots_and_images(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Save PDF", "", "PDF Files (*.pdf);;All Files (*)")
        if file_name:
            with PdfPages(file_name) as pdf:
                title = self.pdf_title_input.text()
                author = self.pdf_author_input.text()
                date = self.pdf_date_input.text()

                plt.figure(figsize=(8.5, 11))
                plt.text(0.5, 0.8, f"Artical Name: {title}", fontsize=25, ha='center')
                plt.text(0.5, 0.6, f"Check Name: {author}", fontsize=20, ha='center')
                plt.text(0.5, 0.5, f"Checks Date: {date}", fontsize=20, ha='center')
                plt.axis('off')
                pdf.savefig()
                plt.close()
                
                x_column = self.x_axis_combobox.currentText()
                for checkbox in self.checkboxes:
                    if checkbox.isChecked():
                        fig, ax = plt.subplots()
                        ax.plot(self.data[x_column], self.data[checkbox.text()], label=checkbox.text())
                        ax.set_xlabel(x_column)
                        ax.legend()
                        pdf.savefig(fig)
                        plt.close(fig)
                
                # Add the selected images to the PDF
                for image_path in self.selected_images:
                    img = mpimg.imread(image_path)
                    plt.figure(figsize=(8.5, 11))
                    plt.imshow(img)
                    plt.axis('off')
                    pdf.savefig()
                    plt.close()
                
                self.status_label.setText(f"Plots and images saved to PDF.")#{file_name}

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DataPlotter()
    window.show()
    sys.exit(app.exec_())
