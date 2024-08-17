This PyQt5-based desktop application serves as a data plotting and visualization tool designed for the Range System Division (RSD). It features a graphical user interface (GUI) for selecting and executing various plotting applications. The application is tailored to handle one-file and two-file plotting, as well as exporting plots and images to PDF.

# Features
Two File Plot Compression App: Plots data from two files and compresses the results.
<br>
One File Plotting App: Plots data from a single file.
<br>
Plot and Image to PDF App: Generates plots and exports them, along with images, to a PDF file.

# Dynamic Layout:
The layout is built with a scrollable area for responsiveness.
Push buttons trigger different plotting applications based on user selection.
<br>
# Components
Header: Contains a logo, application title, and subtitle for visual identity.
<br>
Buttons: Three main buttons allow the user to select different plotting applications.
<br>
Footer: Displays development credits.
<br>
Scroll Area: Scrollable interface for a clean, flexible design.
<br>
# Files
PLOTTER_APP_1FIG_OFFSET.py: The script for the "Two File Plot Compression App."
<br>
PLOTTER_APP_D3.py: The script for the "One File Plotting App."
<br>
PDF_GE_NEW.py: The script for the "Plot and Image to PDF App."

# Requirements
  1. Python 3.x

  2. PyQt5
  <br>
  3. Matplotlib
  <br>
  4.Subprocess Module: Used to run external Python scripts for plotting.
