#.................StyleSheet.......................#
class StyleSheet:
  def __init__(self):
    self.App_style= '''
       #Custom_Widget {
                            background: #bbd2d4;
                            border-radius: 20px;
                            opacity: 100;
                            border: 2px solid #ff2025;
                            padding:0px;
                                               
                        }'''

    self.App_style_2='''
            
            background-color:#65989c;
            border-radius:10px;


            '''

    self.All_Tab='''
                QTabBar::tab {
                            background-color: #193580;
                            border-radius: 15px;
                            padding:5px;
                            font: 18px bold;
                            min-width: 15ex;
                            min-height: 1ex;
                        }


                QTabBar::tab:selected {
                    background-color:#193580;
                    }


                QTabWidget::pane { 
                                    border-top: 0px solid #C2C7CB;
                                }

                QTabWidget::tab-bar {
                            left: 1px;
                        }

            '''
    self.LOGO_frame_style='''
            QFrame{
                    background-color:#bbd2d4 ; 
                    border-radius:20px;  
                    font:bold; font-family: bold"Times New Roman"
                    }

            QLabel{font-size: 40px; 
                    color:#d4ffe6;  
                    font:bold; 
                    font-family: bold"Times New Roman"
                    }            


             '''
    stylesheet = """
                QWidget {
                background-color: #ffffff;
                color: #000000;
                }

                QLineEdit {
                background-color: #eeeeee;
                border: 2px solid #cccccc;
                }

                QPushButton {
                background-color: #4375ac;
                border: 1px solid #cccccc;
                padding: 5px;
                }
                """
                # app.setStyleSheet(stylesheet)
    self.buttonstyle = ("""
                QPushButton {
                        font-size: 20px;
                        background-color: #4375ac;
                        color: white;
                        border: 2px solid #4375ac;
                        border-radius: 10px;
                        padding: 10px 20px;
                }
                QPushButton:hover {
                        background-color: #39698a;
                        border-color: #39698a;
                }
                QPushButton:pressed {
                        background-color: #2c4c6c;
                        border-color: #2c4c6c;
                }
                """)
    
    self.footr = ("""
            QFrame {
                background-color: #2c3e50;
                color: white;
                padding: 10px;
                text-align: center;
                border-top: 1px solid #34495e;
            }
        """)